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

# doc = db['02_19_2017']
# doc = db['local_ecommerce_traffic_webinar_notes']
# doc = db['how_to_write_an_epic_blog_post_notes']
doc = db['seo_notes']
if not os.path.exists('data/' + doc['folder']):
        os.makedirs('data/' + doc['folder'])

note_file = open('data/' + doc['folder'] + '/' + doc['_id'] + '.md','w')
note_file.write('# ' + doc['title'] + "\n\n")

for block in doc['body']['blocks']:

    # Determine if there is a link in the text, and if so create a Markdown link for it.
    block_text = block['text']
    if (len(block['entityRanges']) > 0):
        before_text = block['text'][0:block['entityRanges'][0]['offset']]
        link_text = block['text'][block['entityRanges'][0]['offset']:block['entityRanges'][0]['offset'] + block['entityRanges'][0]['length']]
        after_text = block['text'][block['entityRanges'][0]['offset'] + block['entityRanges'][0]['length']:]
        link = doc['body']['entityMap'][str(block['entityRanges'][0]['key'])]['data']['url']

        block_text = before_text + '[' + link_text + '](' + link + ')' + after_text

    if (block['type'] == 'unstyled'):
        # print(block_text)
        note_file.write(block_text + "\n")
    elif (block['type'] == 'ordered-list-item'):
        # print('1. ' + block_text)
        note_file.write('1. ' + block_text + "\n")
    elif (block['type'] == 'unordered-list-item'):
        # print('* ' + block_text)
        note_file.write('* ' + block_text + "\n")

note_file.write("\n---\n")
note_file.write('<span style="font-size: 10px; color; silver;">Created in Note Pila! on: {} Last updated at: {}.</span>'.format(str(doc['createdAt']), str(doc['updatedAt'])))
note_file.close()
