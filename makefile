

update: update_book update_tests update_notebooks


update_book:
	cp -r ../applied_biostats/_book/book/_build/html/* .
	cp -r ../applied_biostats/_book/book/_build/jupyter_execute .
	
update_tests:
	mkdir -p tests/
	cp -r ../applied_biostats/_bblearn/*/*_files.zip tests/

update_notebooks:
	mkdir -p notebooks/
	cp -r ../applied_biostats/_bblearn/*/*_walkthrough.ipynb notebooks/
	cp -r ../applied_biostats/_bblearn/*/*_walkthrough_SOLUTION.ipynb notebooks/
	cp -r ../applied_biostats/_bblearn/*/*_lab.ipynb notebooks/


