#!/bin/bash

precreate-core articles

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 3

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/articles/schema

# Populate collection
bin/post -c articles /data/spacenews.json

# Restart in foreground mode so we can access the interface
solr restart -f