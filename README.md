# Deviceinfo-parser

## About
Tool for extracting useful information from .deviceinfo-files exported from iphone configuration utility.

It parses the .deviceinfo-files in the current folder, and adds them to your specified .csv-file.

The .csv-file can then be imported in openoffice/libreoffice calc or Excel :)

## Dependencies
Please install [python-unicodecsv](https://pypi.python.org/pypi/unicodecsv/) to the python-path, i.e.:

	pip install unicodecsv

or

	easy_install unicodecsv
		

## Usage
	python parser.py output.csv

**Note: when importing, use utf-8 as charset, and separation by comma.**
