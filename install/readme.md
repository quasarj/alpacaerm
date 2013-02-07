Install instructions.

## Prerequisites
These instructions are written specifically for Ubuntu Server 12.10.
They should work without modification on 12.04, and maybe on older Ubuntu
versions. They will not work on other systems without some modification.


## Install Packages

mysql-server
git
build-essential
apache2
libapache2-mod-wsgi

python-dev
python-mysqldb
python-pip

```
sudo apt-get update
sudo apt-get install mysql-server git build-essential apache2 libapache2-mod-wsgi python-dev python-mysqldb python-pip
```

Set the mysql root password when it asks for it.
Don't forget it, you'll need it later.


## Add User

; set password to whatever you want, don't forget it
adduser alpacaerm

; add the user to the sudo group
usermod -a -G sudo alpacaerm

; confirm with groups

; now reconnect with the new user



check out the repo
------------------
git clone http://github.com/quasarj/alpacaerm


pip install deps
----------------
cd alpacaerm
sudo pip install -r requirements.txt


; test it if desired,
cd erm
./manage runserver



configure some stuff
--------------------

;configure the mysql database
; password as you configured earlier
mysql -u root -p


; create database and users
create database alpacaerm;
create user 'alpacaerm'@'localhost' identified by 'mypassword';
grant all on alpacaerm.* to 'alpacaerm'@'localhost';
exit


export data from the sqlite database
; this must be done in several steps, to help with issues with loading
./manage.py dumpdata contenttypes > types.json
./manage.py dumpdata auth > auth.json
./manage.py dumpdata erm vendor exception > base.json



## switch settings file to new db
; set database settings (per earlier config)
```
cp ../install/settings.py ermproj/
```


### Custom files settings
If you put your files somewhere else, set these.
;set STATIC_ROOT
STATIC_ROOT = '/home/alpacaerm/alpacaerm/staticfiles/'

; set MEDIA_ROOT
MEDIA_ROOT = '/home/alpacaerm/alpacaerm/mediafiles/'

; set the template path
/home/alpacaerm/alpacaerm/erm/templates



; configure logger
; to come later

; run collectstatic! -----------
./manage.py collectstatic


;run syncdb and migrations ------------------
; make sure you say NO to the question about adding a super user
```
./manage.py syncdb
./manage.py migrate
```


import data into the mysql database
; this must be done in several steps
; first, clear the tables auth_permission and django_content_type
```
echo "delete from auth_permission;" | mysql -u alpacaerm -pmypassword alpacaerm
echo "delete from django_content_type;" | mysql -u alpacaerm -pmypassword  alpacaerm
```

; then load the data!
```
./manage.py loaddata types.json
./manage.py loaddata auth.json
./manage.py loaddata base.json
```

## Apache

; bascially, just put this file into place. Switch with user alpacaerm
; this goes in /etc/apache2/sites-available/alpacaerm
; don't forget to make a symlink to sites-enabled (and remove the default)
```
sudo cp ../install/alpacaerm.conf /etc/apache2/sites-available/alpacaerm
sudo ln -s /etc/apache2/sites-available/alpacaerm /etc/apache2/sites-enabled/000-alpacaerm
sudo rm /etc/apache2/sites-enabled/000-default
```

Then, restart the server.
```
service apache2 restart
```
