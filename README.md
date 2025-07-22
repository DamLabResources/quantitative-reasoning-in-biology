# Applied Biostatistics

This repository contains the content and build system for the Applied Biostatistics book and Drexel course.

In general, this can be described a Frankenstien melding of a [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) and [Otter Grader](https://otter-grader.readthedocs.io/en/latest/).
The Otter system is used to create a set of template notebooks for instructional walkthroughs and evaluating labs.
Using an extended langauge, these notebooks are marked with auto-graded questions after building.
The Jupyter Book project is used to create a richly rendered HTML _book_ from these notebooks and supplemental markdown files.
A [Snakemake](https://snakemake.readthedocs.io/en/stable/) is pipeline is then used to tie all of the different toolsets together.


## Organization:

 - `content/` - This directory contains the markdown and notebook files that represent the content of the course.
 - `tocs/` - This directory contains the Table of Contents for each of the Juptyer Books.
    This maps the files in the `content/` directory into each individual Juptyer Book.
 - `styles/` - A set of `vale` styles to enforce a writing style.
 - `workflow` - A `snakemake` pipeline that manages all of the commands that run Otter and Jupyter Book.
 - `_book/` - Build directories for each of the jupyter books. 
 - `_bblearn/` - A directory of files to upload to BBLearn for student use. Files in here should not be edited.
 
## Usage

### Adding or modifying content

ONLY edit the files in the `content/` directory.

### Style checking

This project uses [`vale`](https://vale.sh/) as a generic style checker.

```bash
vale path/to/file.md
```

Vale cannot natively handle `.ipynb` files.
However, if you add the following alias to your local `~./.bashrc` file you can sidestep the issue.

```bash
alias smrt_vale='function _smrt_vale(){ 
    local file="$1"; 
    shift 
    if [[ "${file##*.}" == "md" ]]; then 
        vale "$file" "$@"; 
    elif [[ "${file##*.}" == "ipynb" ]]; then 
        jupyter nbconvert --to markdown "$file" --stdout | vale --ext=.md /dev/stdin "$@"; 
    else 
        echo "Unsupported file extension. Please provide a .md or .ipynb file."; 
    fi 
}; _smrt_vale'


smrt_vale path/to/file.ipynb
```


### Building 

The entire set can be built with:

```bash
make all
```

Indvidual parts can be made with:

```bash
make books
make uploads
```

<img src="https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/DamLabResources/quantitative-reasoning-in-biology/commits?path=notebooks/Module02_lab.ipynb&query=$[0].commit.author.date&label=Last%20Updated&style=flat-square&color=brightgreen" alt="File Last Updated">