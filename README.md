# PDF Merger

This application merges several PDFs together.

## Ideas

### Merging PDF files

The merging is done with a package called `pypdf` and is explained [here](https://pypdf.readthedocs.io/en/stable/user/merging-pdfs.html).

### Building a GUI

Our GUI is based on `PySimpleGUI`. It is a Python package that enables Python programmers of all levels to create GUIs. The main structure of our GUI is taken from an outstanding [tutorial](https://www.youtube.com/watch?v=LzCfNanQ_9c&ab_channel=CodingIsFun) on YouTube.

### Convert Python File to Executable

For this step we use `pyinstaller` and the conversion is done as follows

```{shell}
pyinstaller --noconfirm --onefile --windowed --name "PDF Merger" --icon=merger_icon.icns main.py
```

Related to the conversion is [this](https://www.youtube.com/watch?v=jnUpSK3D3is&t=93s&ab_channel=ThePyCoach) video and [this](https://github.com/pyinstaller/pyinstaller/issues/3968) forum post.