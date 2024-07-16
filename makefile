all:
	make uploads
	make books

books:
	snakemake -c 1 build_all_books

uploads:
	snakemake -c 1 build_bblearn_uploads

vale:
	vale content/*/*.md

clean:
	rm -r _book
	rm -r _bblearn
	rm -r content/Module*/_build
