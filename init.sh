mkdir web
cd web
mkdir public uploads etc
cd public
mkdir img css js
cd
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart