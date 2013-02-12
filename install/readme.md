Install instructions.

## Prerequisites
These instructions are written specifically for Ubuntu Server 12.10.
They have also been tested on Ubuntu Server 12.04, and may work on earlier
versions of Ubuntu Server. They will not work on other systems without 
some modification.


These are the basic prerequisites to install the system on any server:

* Python 2.7
* Development headers for Python, for compiling some python modules (like PIL)
* PIP, the Python package manager
* Apache 2
* mod_wsgi (must be compiled against python 2.7)
* MySQL (or another database server supported by django)
* git


## Install Packages

These packages are required:

* mysql-server
* git
* build-essential
* apache2
* libapache2-mod-wsgi
* python-dev
* python-mysqldb
* python-pip

Install them with:
```
sudo apt-get update
sudo apt-get install mysql-server git build-essential apache2 libapache2-mod-wsgi python-dev python-mysqldb python-pip
```

Set the mysql root password when it asks for it.
Don't forget it, you'll need it later.

## Add User

Set password to whatever you want, just don't forget it.
```
adduser alpacaerm
```

Add the user to the sudo group.
```
usermod -a -G sudo alpacaerm
```

Confirm with groups.
```
groups alpacaerm
```
Make sure it lists the sudo group.


Now reconnect with the new user. All of the files will be
installed into this new user's home directory.


## Check out the repo
```
git clone http://github.com/quasarj/alpacaerm
```

## pip install dependancies
```
cd alpacaerm
sudo pip install -r requirements.txt
```

## Test, if desired
```
cd erm
./manage.py runserver 0.0.0.0:8000
```

Navigate to the server's hostname:8000 to test if it's working.
Press control+c to terminate the test server.

## Configure everything

### Configure the mysql database
Connect to mysql as root. When prompted, enter the password you set ealier
for mysql root.
```
mysql -u root -p
```

Create database and user. If you want, you can use a password of your choice
in place of "mypassword" below. If you do, it will be needed later.
```
create database alpacaerm;
create user 'alpacaerm'@'localhost' identified by 'mypassword';
grant all on alpacaerm.* to 'alpacaerm'@'localhost';
exit
```

### Export data from the sqlite database
If you wish to migrate the data from the test database into this
deployment, you must complete this setp.

```
./manage.py dumpdata contenttypes > types.json
./manage.py dumpdata auth > auth.json
./manage.py dumpdata erm vendor exception > base.json
```


### Switch settings file to new db
In the install directory there is an example settings.py file.
This file contains all the settings needed if you follow these 
instructions exactly. 

Copy it into place, even if you used different settings.
```
cp ../install/settings.py ermproj/
```

#### Custom files settings
If you used different usernames or passwords
or paths, you will need to edit the settings.py file and 
update it with those settings at this time.

If you used different usernames or passwords, set those at the top of the file.

If you put your files somewhere else, modify STATIC_ROOT and MEDIA_ROOT.
Note: These are already in the file, find them and change them.
```
STATIC_ROOT = '/home/alpacaerm/alpacaerm/staticfiles/'
MEDIA_ROOT = '/home/alpacaerm/alpacaerm/mediafiles/'
```

Also set the template path correctly.
```
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/home/alpacaerm/alpacaerm/erm/templates",
)
```

### Configure logger
This section is not written yet.

### Collect static files
```
./manage.py collectstatic
```

### Sync and migrate database
Make sure you say NO to the question about adding a super user.

```
./manage.py syncdb
./manage.py migrate
```


### Import data into the mysql database
If you are migrating the data from the test database, you now need to
import it into the new mysql database.

First, clear the tables auth_permission and django_content_type.
```
echo "delete from auth_permission;" | mysql -u alpacaerm -pmypassword alpacaerm
echo "delete from django_content_type;" | mysql -u alpacaerm -pmypassword  alpacaerm
```

Then load the data.
```
./manage.py loaddata types.json
./manage.py loaddata auth.json
./manage.py loaddata base.json
```

## Apache

There is an example apache config in the install directory, alpacaerm.conf.
This file is setup specifically for Debian-based apache2 installations
that use the sites-available/sites-enabled structure. Also note that this
file will only work if this is the *only* site configured on this apache
install. If you used all of the paths in this guide, you can simply
copy this file into place.

```
sudo cp ../install/alpacaerm.conf /etc/apache2/sites-available/alpacaerm
sudo ln -s /etc/apache2/sites-available/alpacaerm /etc/apache2/sites-enabled/000-alpacaerm
sudo rm /etc/apache2/sites-enabled/000-default
```

Then, restart the server.
```
service apache2 restart
```
