FROM solr:8.10

COPY spacenews_compact.json /data/spacenews.json

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
