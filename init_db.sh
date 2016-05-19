sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE qadb"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '12345'"
mysql -uroot -e "GRANT ALL ON qadb.* TO 'box'@'localhost'"