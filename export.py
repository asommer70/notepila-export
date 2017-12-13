#!/usr/bin/env python
#
# Export notes from Note Pila! into Markdown files.
#
import couchdb
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

url = "http://{}:{}@notes:5984".format(os.environ.get("USER"), os.environ.get("PASS"))
couch = couchdb.Server(url)
db = couch['notepila']

print('02_19_2017:', db['02_19_2017'])
