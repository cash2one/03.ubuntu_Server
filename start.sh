#!/bin/sh
#rm *.log *.out
if [ ! -d /data ]; then

	mkdir -p /data/photo	
	mkdir -p /data/database
	mkdir -p /data/download
	chmod -R 755 /data
fi;
cd weixin
python app.py
nginx -s reload
aria2c --enable-rpc --rpc-listen-all
#sqlite_web data/database/database.db
