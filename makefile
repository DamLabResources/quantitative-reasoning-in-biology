
update_book:
	cp -r ../applied_biostats/_book/book/_build/html/* .
	cp -r ../applied_biostats/_book/book/_build/jupyter_execute .
	mkdir -p tests/
	cp ../applied_biostats/_bblearn/*/*_files.zip tests/

#deploy_book:

