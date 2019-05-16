import io
import os
from notebook.utils import to_api_path

_script_exporter = None

def script_post_save(model, os_path, contents_manager, **kwargs):
    """convert notebooks to Python script after save with nbconvert

    replaces `jupyter notebook --script`
    """
    print(model)
    print(os_path)

    if model['type'] != 'notebook':
      return


								
c.FileContentsManager.post_save_hook = script_post_save

