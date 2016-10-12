#!/bin/sh
rm *.log *.out
cd weixin
python app.py
nginx -s reload
sqlite_web data/database/database.db
