git config --global user.email "rebusiztysyachidetaley@bk.ru"
git config --global user.name "caxapakaared" 
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
source web/myvenv/bin/activate
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ hello:app &     
gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application & 