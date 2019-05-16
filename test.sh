#!/bin/sh

if [ "$1" == "install" ]; then
  jupyter nbextension install --py notebook_owncloud --symlink
  jupyter nbextension enable notebook_owncloud --py
  jupyter serverextension enable --py notebook_owncloud
fi

if [ "$1" == "enable" ]; then 
  jupyter nbextension enable notebook_owncloud --py
fi

if [ "$1" == "uninstall" ]; then 
  jupyter nbextension disable notebook_owncloud
  jupyter nbextension uninstall --py notebook_owncloud
fi

if [ "$1" == "list" ]; then
  jupyter nbextension list
  jupyter serverextension list
fi
