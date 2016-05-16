sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE qadb;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON qadb.* TO 'box'@'localhost' WITH GRANT OPTION;"