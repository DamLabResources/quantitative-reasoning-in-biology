all:
	make uploads
	make books

book:
	snakemake -c 1 _book/book

bblearn:
	snakemake -c 1 _bblearn/website


uploads:
	snakemake -c 1 build_bblearn_uploads

vale:
	vale content/*/*.md

clean:
	rm -r _book
	rm -r _bblearn
	rm -r content/Module*/_build

install:
	mamba env create -f env-minimal.yaml -p ./venv
