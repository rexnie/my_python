my_python
=========
ch1 hello world,use template
    1. pip install Django==1.7
    2. django-admin.py startproject project1
    3. django-admin.py startapp blog
    4. add "blog" to INSTATLLED_APPS in setting.py  
    5. modfy urls.py and views.py

ch2 use db:mySQL
    1. sudo apt-get install mysql-server mysql-client libmysqlclient-dev
    2. sudo apt-get install python-dev
    3. sudo apt-get install  python-setuptools
    4. sudo apt-get install libmysqlclient-dev libmysqld-dev
    5. sudo easy_install mysql-python
    6. create database:
            mysql -uroot -p
            create database my_db default charset = utf8;
    7. vim blog/models.py
        object-relationship model
    8. python manage.py syncdb
    9. show database status
            use my_db;
            show tables;
            desc table_name;
            select * from table_name;

ch3 admin interface, use sqlite3
    1. sudo apt-get install sqlite3
    2. vim setting.py
        database, add app
    3. startproject, startapp
    4. vim models.py
    5. python manage.py syncdb
    6. vim urls.py
