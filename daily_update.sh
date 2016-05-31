#!/usr/bin/env bash
NOW=$(date +%F)
git pull

echo "updateTable.py is running"
python updateTable.py

echo "Committing new changes"
git add -u
git commit -am "Update ndk versions ${NOW}"

echo "Pushing it"
git push
