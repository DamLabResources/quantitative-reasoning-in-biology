from glob import glob
import zipfile

rule notebook2md:
    input:
        '{stem}.ipynb'
    output:
        '{stem}.md'
    shell:
        "jupyter nbconvert {input} --to markdown --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags remove_cell"
        
rule valify:
    input:
        '{stem}.md'
    output:
        '{stem}.vale'
    shell:
        'vale --no-wrap --no-exit {input} > {output}'


checkpoint otter_assign:
    input:
        '{path}/{stem}.ipynb'
    output:
        stem = directory('{path}/_build/{stem}_otter/'),
        student_tests = directory('{path}/_build/{stem}_otter/student/tests'),
        student_notebook = '{path}/_build/{stem}_otter/student/{stem}.ipynb',
        grader_notebook = '{path}/_build/{stem}_otter/autograder/{stem}.ipynb',
        grader_tests = directory('{path}/_build/{stem}_otter/autograder/tests'),
    shell:
        'otter assign {input} {output.stem}'

def get_extra_paths(wildcards):
    data_files = glob_wildcards(f"content/{wildcards.module}/{{data_file}}.csv").data_file
    return expand(f"content/{wildcards.module}/{{data_file}}.csv", data_file=data_files)


def get_otter_tests(learning_activity, wildcards, scope='student'):
    mod = wildcards["module"]
    
    path = f'content/{mod}'
    stem = f'{mod}_{learning_activity}'
    checkpoints.otter_assign.get(path = path, stem=stem, **wildcards)
    
    if not os.path.exists(f'content/{mod}/_build/{mod}_{learning_activity}_otter'):
        print('found no things at:', f'content/{mod}/{mod}_{learning_activity}_otter')
        return []
    
    
    
    prefix = f'content/{mod}/_build/{mod}_{learning_activity}_otter'
    
    questions = glob_wildcards(f'{prefix}/{scope}/tests/{{q}}.py')
    return expand(f'{prefix}/{scope}/tests/{{q}}.py', q = questions.q)
        
        
        
rule zip_tests:
    input:
        raw_files = get_extra_paths,
        walkthrough_tests = lambda wildcards: get_otter_tests('walkthrough', wildcards),
        lab_tests = lambda wildcards: get_otter_tests('lab', wildcards),
    output:
        student_packed_zip = 'content/{module}/_build/{module}_files.zip'
    run:
        with zipfile.ZipFile(str(output["student_packed_zip"]), mode = 'w') as handle:
            
            print('Packing walkthrough', input['walkthrough_tests'])
            for path in input['walkthrough_tests']:
                name = os.path.basename(path)
                if not name.startswith('.'):
                    handle.write(path, arcname = 'walkthrough-tests/' + name)
            
            print('Packing lab', input['lab_tests'])
            for path in input['lab_tests']:
                name = os.path.basename(path)
                if not name.startswith('.'):
                    handle.write(path, arcname = 'lab-tests/' + name)
            written = set()
            
            print('Packing raw', input['raw_files'])
            for path in input['raw_files']:
                name = os.path.basename(path)
                if not name.startswith('.') and (name not in written):
                    written.add(name)
                    handle.write(path, arcname = name)
                    
rule deploy_notebook:
    input:
        student_notebook = 'content/{module}/_build/{module}_{activity}_otter/student/{module}_{activity}.ipynb',      
        solution_notebook = 'content/{module}/_build/{module}_{activity}_otter/autograder/{module}_{activity}.ipynb',
    output:
        student_notebook = '_bblearn/{module}/{module}_{activity}.ipynb',
        solution_notebook = '_bblearn/{module}/{module}_{activity}_SOLUTION.ipynb',
        
    shell:
        """
        cp {input.student_notebook} {output.student_notebook};
        cp {input.solution_notebook} {output.solution_notebook};
        """
        
rule:
    input:
        'content/{module}/_build/{module}_files.zip'
    output:
        '_bblearn/{module}/{module}_files.zip'
    shell:
        "cp {input} {output}"
        

def get_files_from_book_config(wildcards):
    
    book_yaml_path = f'{wildcards["book"]}_toc.yml'
    book_structure = yaml.full_load(open(book_yaml_path))
    
    root_index_file = book_structure['root'] + '.md' # Assumption
    
    found, missing = search_files_in_yaml(book_structure)
    
    return [root_index_file] + found+missing


rule bookify_walkthrough:
    input:
        "content/{module}/{module}_walkthrough.ipynb"
    output:
        "content/{module}/{module}_walkthrough_book.ipynb"
    shell:
        "jupyter nbconvert {input} --to notebook --stdout --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags remove_cell > {output}"

        
        
rule render_book:
    input:
        toc_file = 'tocs/{book}_toc.yml',
        book_files = get_files_from_book_config,
        config = '_config.yml'
    output:
        directory('_book/{book}/')
        
    
    shell:
        "jupyter-book build --config {input.config} --toc {input.toc_file} --path-output {output} ."
        
        
