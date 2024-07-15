import yaml
import os
import glob as pyglob


def get_all_modules():
    
    content_dirs = glob_wildcards('content/{module}/{mod}_course.md')
    return [d for d in content_dirs.module]


def infer_extension(value):
    
    if 'walkthrough' in value:
        return value + '.ipynb'
    
    elif 'book' in value:
        return value + '.md'
    
    return value


def search_files_in_yaml(yaml_content):
    """
    Recursively search for 'file' keys in the given YAML content and
    return all files with .md, .txt, or .ipynb extensions at the indicated paths.
    Also, return paths where no file with the specified extensions was found.
    
    Args:
    yaml_content (dict): The parsed YAML content.
    
    Returns:
    tuple: Two lists - 
           1. Paths to files with the specified extensions.
           2. Paths where no file with the specified extensions was found.
    """
    def recurse_structure(data):
        found_files = []
        not_found_files = []
        valid_extensions = ['.md', '.txt', '.ipynb']
        
        if isinstance(data, dict):
            for key, value in data.items():
                if key == 'file':
                    matched_files = []
                    for ext in valid_extensions:
                        matched_files.extend(pyglob.glob(value + ext))
                    if matched_files:
                        found_files.extend(matched_files)
                    else:
                        not_found_files.append(infer_extension(value))
                else:
                    sub_found, sub_not_found = recurse_structure(value)
                    found_files.extend(sub_found)
                    not_found_files.extend(sub_not_found)
        elif isinstance(data, list):
            for item in data:
                sub_found, sub_not_found = recurse_structure(item)
                found_files.extend(sub_found)
                not_found_files.extend(sub_not_found)
        return found_files, not_found_files

    return recurse_structure(yaml_content)


