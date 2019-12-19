#!/bin/bash


db_user=root
db_password=Lhzl596A1005
db_host=121.40.92.131
db_date=`date +%F`
db_list=`sudo mysql -u$db_user -p$db_password -h $db_host -e "show databases;" |grep -v "|"|sed '1d'`


sudo mkdir /data/db_backup/$db_date -p
for i in $db_list
	do
		sudo mysqldump -u$db_user -p$db_password -h $db_host -B $i >/data/db_backup/$db_date/${i}_$db_date.sql
	done


