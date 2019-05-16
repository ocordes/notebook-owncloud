from notebook_owncloud.handlers import setup_handlers



# Jupyter Extension points


def _jupyter_server_extension_paths():
    return [{
        'module': 'notebook_owncloud',
    }]


def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "notebook_owncloud",
        "src": "static",
        "require": "notebook_owncloud/main"
    }]


def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
