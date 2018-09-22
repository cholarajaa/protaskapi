Protaskm
========

Protaskm is a simple django application to create/fetch tickets.

How to setUp the project:

    # clone the project
    $ git clone https://github.com/cholaraja/protaskapi.git
    $ cd protaskapi
    
    # create a [virtual environment](https://docs.python.org/3/library/venv.html)
    $ pip install -r requirements/local.txt
    
    # install postgresql if not already installed
    # [ubuntu installation guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
    $ psql -U ./config/createdb.sql

    # run server
    $ python manage.py runserver 0:8000 --settings=config.settings.development
    # server will run at 127.0.0.1:8000
    # ticket api 127.0.0.1:8000/api/tickets/
    # tag api 127.0.0.1:8000/api/tags/

    running tests
    $ pytest

Features
--------

- Add/View/Edit/Delete Tickets
- Add/View/Edit/Delete Tags


License
-------

The project is licensed under the [MIT license.](http://www.opensource.org/licenses/MIT)