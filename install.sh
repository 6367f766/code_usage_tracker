#!/bin/bash


pyinstaller -n search-code -F src/main.py;
mv dist/search-code ..
rm -rf dist build *.spec

