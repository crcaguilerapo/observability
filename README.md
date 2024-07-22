# Zipkin!


## Get indexes

Lists all the indices currently available in the Elasticsearch cluster.

```
curl --location 'localhost:9200/_cat/indices'
```

## Delete Index

Deletes the index named `zipkin-span-2024-07-21` from the Elasticsearch cluster.

```
curl --location --request DELETE 'localhost:9200/zipkin-span-2024-07-21'
```

## Create Repository

Creates a snapshot repository named `my_fs_backup` using the filesystem type and specifies the location where the snapshots will be stored.

```
curl --location --request PUT 'http://localhost:9200/_snapshot/my_fs_backup' \
--header 'Content-Type: application/json' \
--data-raw '{
  "type": "fs",
  "settings": {
    "location": "/usr/share/elasticsearch/snapshots"
  }
}'

```

## Get Repository

Retrieves information about the snapshot repositories configured in Elasticsearch.

```
curl --location 'http://localhost:9200/_snapshot/'
```


## Create Snapshot

Creates a snapshot named `snapshot_1` in the `my_fs_backup` repository, including all indices and excluding global state.
```
curl --location --request PUT 'http://localhost:9200/_snapshot/my_fs_backup/snapshot_1' \
--header 'Content-Type: application/json' \
--data-raw '{
  "indices": "*",
  "ignore_unavailable": true,
  "include_global_state": false
}'

```


## Get Snapshot

Retrieves information about a specific snapshot (`snapshot_1`) from the `my_fs_backup` repository.

```
curl --location 'http://localhost:9200/_snapshot/my_fs_backup/snapshot_1'
```


## Restore Snapshot

Restores the snapshot named `snapshot_1` from the `my_fs_backup` repository, including the index `zipkin-span-2024-07-21`. It does not include the global state.

```
curl --location --request POST 'http://localhost:9200/_snapshot/my_fs_backup/snapshot_1/_restore' \
--header 'Content-Type: application/json' \
--data-raw '{
  "indices": "zipkin-span-2024-07-21",
  "ignore_unavailable": true,
  "include_global_state": false
}'

```


