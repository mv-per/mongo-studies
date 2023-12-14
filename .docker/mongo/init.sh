#!/bin/bash

# https://gist.github.com/zhangyoufu/d1d43ac0fa268cda4dd2dfe55a8c834e
{
while ! nc -z localhost $MONGO_DB_PORT; do
  sleep 0.1 # wait for 1/10 of the second before check again
done &&
mongo --port $MONGO_DB_PORT -- "$MONGO_INITDB_DATABASE" 2>&1 > /data/logs/mongo-init.log <<-EOJS
  var rootUser = '$MONGO_INITDB_ROOT_USERNAME';
  var rootPassword = '$MONGO_INITDB_ROOT_PASSWORD';
  var admin = db.getSiblingDB('admin');
  admin.auth(rootUser, rootPassword);
EOJS && sleep 3 &&
mongo --port $MONGO_DB_PORT -- "$MONGO_INITDB_DATABASE" 2>&1 > /data/logs/mongo-rs-init.log <<-EOJS
    var rootUser = '$MONGO_INITDB_ROOT_USERNAME';
    var rootPassword = '$MONGO_INITDB_ROOT_PASSWORD';
    var admin = db.getSiblingDB('admin');
    admin.auth(rootUser, rootPassword);
    rs.initiate({_id: 'rs0', members: [{_id: 0, host: "localhost:$MONGO_DB_PORT"}]})
EOJS
} &