sudo /etc/init.d/mysql start
mysql -uroot -e "create database qadb"
mysql -uroot -e "create user 'box'@'%'"
mysql -uroot -e "grant all qadb.* to 'box'@'%'"