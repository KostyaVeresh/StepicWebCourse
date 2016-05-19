#sudo /etc/init.d/mysql restart
mysql -uroot -e "DROP DATABASE qadb"
mysql -uroot -e "CREATE DATABASE qadb"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '12345'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON qadb.* TO 'box'@'localhost'"

python /home/box/web/ask/manage.py syncdb