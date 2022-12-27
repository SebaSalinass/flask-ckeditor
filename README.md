# Flask-CKEditor-Manager

Flask-CKEditor-Manager _(from now on **FCKM**)_ provides a simple interface to use CKEDitor5 javascript library with Flask. Greatly inspired by Flask-CKEditor

```{warning}
🚧 This package is under heavy development..
```

## Installation

Install the extension with pip:

```bash
pip install flask-ckeditor-manager
```

Install with poetry:

```bash
poetry add flask-ckeditor-manager
```

## Usage

Once installed the **FCKM** is easy to use. Let's walk through setting up a basic application. Also please note that this is a very basic guide: we will be taking shortcuts here that you should never take in a real application.

To begin we'll set up a Flask app:

```python
from flask import Flask

app = Flask(__name__)
```

### Setting up extension

**FCM** works via a CKEditorManager object. To kick things off, we'll set up the `ckeditor_manager` by instantiating it and telling it about our Flask app:

```python
from flask_ckeditor import CKEditorManager

ckeditor_manager = CKEditorManager()
ckeditor_manager.init_app(app)
```

### Load resources

Once the extension is set up, this will make available the `ckeditor` object into the templates context so you could load the javascript package easily, like this.

```html
<head>
  {{ ckeditor.load() }}
</head>
```

### Rendering the editor

Once created you can pass the `Chart` object to render_template and use it likewise.

```html
<!-- ckeditor.load() must be called before this line -->
<textarea id="editor"></textarea>
<div class="my-classes">{{ ckeditor.config('editor') }}</div>
```
