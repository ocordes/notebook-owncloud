from notebook.utils import url_path_join as ujoin
from notebook.base.handlers import IPythonHandler
import os, json, urllib, requests
from subprocess import check_output
import subprocess


class OwnCloudHandler(IPythonHandler):

    def put(self):
        # close connection
        self.write({'status': 200, 'statusText': 'Success!'})


    def get(self):
        self.write({'status': 200, 'statusText': 'Success!'})


def setup_handlers(nbapp):
    route_pattern = ujoin(nbapp.settings['base_url'], '/owncloud/api')
    nbapp.add_handlers('.*', [(route_pattern, OwnCloudHandler)])
