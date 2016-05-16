sudo /etc/init.d/mysql restart
mysql -uroot -e "create database qadb; create user 'box'@'%'; grant all qadb.* to 'box'@'%';"