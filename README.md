
    $ ian build -cfi
    $ sudo ln -s /etc/nginx/sites-available/hello /etc/nginx/sites-enabled/
    $ sudo service nginx restart
    $ sudo ln -s /etc/uwsgi/apps-available/hello.ini /etc/uwsgi/apps-enabled/
    $ sudo service uwsgi restart
    $ xdg-open http://localhost:8181
