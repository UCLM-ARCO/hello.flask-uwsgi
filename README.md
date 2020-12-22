::
    $ ian build -ci
    $ sudo ln -s /etc/nginx/sites-available/hello /etc/nginx/sites-enabled/
    $ sudo ln -s /etc/uwsgi/apps-available/hello.ini /etc/uwsgi/apps-enabled/
    $ sudo service nginx restart
