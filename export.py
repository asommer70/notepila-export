#
# Export notes from Note Pila! into Markdown files.
#
import couchdb

couch = couchdb.Server('http://notes:5984/')

for db in couch:
    print(db)
