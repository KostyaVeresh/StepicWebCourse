sudo /etc/init.d/mysql restart
mysql -u root -e "CREATE DATABASE IF NOT EXISTS qadb; CREATE USER 'box'@'localhost'; GRANT ALL ON qadb.* TO 'box'@'localhost';"
python /home/box/web/ask/manage.py syncdb