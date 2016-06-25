#!/usr/bin/env bash
NOW=$(date +%F)
git pull

echo "updatetable.py is running"
python updatetable.py

echo "Committing new changes"
git add -u
git commit -am "Update ndk versions ${NOW}"

echo "Pushing it"
git push
