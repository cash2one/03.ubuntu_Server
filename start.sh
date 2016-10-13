#!/bin/sh
#rm *.log *.out
cd weixin
python app.py
nginx -s reload
aria2c --enable-rpc --rpc-listen-all
#sqlite_web data/database/database.db
