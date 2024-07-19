# Notebook basics

This section covers background concepts about Jupyter notebooks that should know.


## Jupyter Notebooks

A Jupyter Notebook file is a specially written text file that encodes text, formatting, code, and images.
While you can open it with programs like Notepad or WordPad, it will be difficult to understand or edit.
Jupyter compatible systems (like Google Colab) can render these files and allow you to interact with them.
For our purposes, we will only be talking about _Python_ notebooks, but there are similar formats for other languages like R and Julia.
Each notebook is a series of independent _cells_.

## Cells

Content within a notebook is contained within cells.
You can create, run, edit, delete, and re-ordered them at will.

There are two basic cell types we will use in this course.

* **Markdown** - These cells contain plain text with optional formatting tags.
These can be rendered to create formatted text, tables, images, and links.
* **Code** - These cells contain python code ready to be sent to the interpreter.

Both can be _executed_ by using the `Play` button on the browser or the shortcut \<shift>-Enter.
When executed, markdown files Render themselves, code cells send their content to the interpreter.


## Session

When running code on Google Colab or similar system you are using _the cloud_.
When you load a notebook, the program itself, runs on a computer in Google's services.
This frees you from installing software yourself and potentially gives you access to a more powerful computer.
However, it comes with some limitations.

1) You need to upload and download files across the computer.
When you first start, or just testing, this is okay.
However, when you are working with large datasets, you'll want to install this on your own computer.
2) On the free version, it only runs for two hours without any interaction.
For the purposes of this class, this is not an issue.
All code will take less than a second to run.
However, if you plan more extensive analysis, this will become a problem.
3) Security. When you run things on Google's systems, you are sharing everything with them.
Never upload HIPAA protected data or sensitive or secrety information from your company to Colab.

When you connect to Google Colab, a new virtual computer gets created in the cloud and connected to our browser.
A Python _interpreter_ then starts and awaits for our commands, we call this the _session_.

When you first start, the session is empty.
As we execute cells, that sends commands to the session which responds accordingly based on this and past commands.
An important thing to remember, we cannot _undo_ a command once it is sent.

We can either issue new commands that overwrite the incorrect actions like so:

```python
# Original cell
x = 12
```

```python
# Fixed cell
x = 21
```

Running these two cells have the effect of only the most recent one being relevant.

This is not always possible, or maybe there are too many mistakes to fix.
In this case, we want to **restart** the session.
This can be done using the Menu -> Runtime -> Restart Session; or the shortcut \<ctrl>-M.
 * Oftentimes, you have many cells you want to execute before this one; use Menu -> Runtime -> Run Before.
 * Sometimes, you want to run everything fresh (like before submission); use Menu -> Runtime -> Restart & Run all.
 * Ocassionally, you will need to completely restart the system as if you just freshly logged in; use Menu -> Runtime -> Disconnect and delete runtime.

`````{admonition} Don't be afraid to Restart & Run all
:class: tip
Use **Restart & Run all** often! It is useful to ensure that your written code is complete.
`````