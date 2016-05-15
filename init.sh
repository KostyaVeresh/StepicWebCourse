sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
gunicorn -c /etc/gunicorn.d/hello.py hello:wsgiApp
gunicorn -b 0.0.0.0:8000 ask.ask.wsgi
