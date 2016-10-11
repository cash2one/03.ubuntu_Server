#!/bin/sh

python weixin/app.py
nginx -s reload
sqlite_web data/database/database.db