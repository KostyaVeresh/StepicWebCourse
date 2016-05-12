mkdir web
cd web
mkdir public uploads etc
cd public
mkdir img css js
cd
cp /home/box/StepicWebCourse/nginx.conf /home/box/web/etc/nginx.conf
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart