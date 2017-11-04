# Vue + flask demo
Demo application to demonstrate **Vue + Flask** stack bundle


  

## Installation

pip3 install -r requirements.txt

## db init
* Create db `ticket_booking` in mysql  
**for postgres/sqlite** 
change link to connection/file in `SQLALCHEMY_DATABASE_URI` in `config.py`
* change credentials param `SQLALCHEMY_DATABASE_URI` in `config.py`


##### Migrations way
* Run `python3 manage.py db init`  
* then `python3 manage.py db migrate`  
* then `python3 manage.py db upgrade`

##### Sql dump way
* import `sql_dump.sql` to your db

## Startup
* For backend application run `python3 app.py`
* For frontend dev see `frontend/README.md`


## Demo ##

![Main screen](/doc/app_screen.png?raw=true "Main screen")
![Movie screen](/doc/item_screen.png?raw=true "movie screen")
