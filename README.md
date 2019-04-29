# Blogz

#### An application for viewing and posting blogs

## Author

[Jason Muchiri](https://github.com/jasonmuchiri)

## Description

A personal blogging website where you can create and share your opinions and other users can read and comment on them. A user must first register an account, and on registration should receive a welcome email. Once registered and logged in,then he or she can post a blog and comment on other blogs.

## Project's set up instructions

To start using this blogz app, use the following commands:

- `git clone` ~ This will automatically clone the repository to your local machine.

- `sudo apt-get install python3-pip`

- `cd news-highlight`

- `python3.6 -m venv --without-pip virtual` ~ create a virtual environment

- `source virtual/bin/activate` ~ activate the virtual environment

- `sudo curl https://bootstrap.pypa.io/get-pip.py | python` ~ to download pip

- `pip install flask` ~ to install Flask using pip

- `sudo apt-get update`

- `sudo apt-get install postgresql postgresql-contrib libpq-dev` ~ to install Postgres

- `sudo service postgresql start`

- `sudo -u postgres createuser --superuser $USER`

- `sudo -u postgres createdb $USER`

- `touch .psql_history`

- `psql` ~ to connect to the postgres server

- `\q` ~ to exit the server

- `pip install flask-SQLAlchemy` ~ to install Flask-SQLAlchemy

- `pip install psycopg2` ~ to install psycopg2 which is our Postgres driver

- `pip install flask-migrate` ~ to install the flask-migrate extension to create database migrations

- use the following commands to initialize our aplication to use Migrations
  
  - `python3.6 manage.py db init`

  - `python3.6 manage.py db migrate -m "Initial Migration"`

  - `python3.6 manage.py db upgrade`

- `pip install flask-login`

- `pip install flask-uploads`

- `pip install flask-mail`

- `pip install flask-simplemde markdown2`

- `chmod a+x start.sh` ~ to make the file executable

- `./start.sh` ~ to run the application

### Dependancies

- For reference open the requirements.txt file to view all the project's dependancies.

## BDD

|Behaviour|Input Example|Output Example|
|---------|-------------|--------------|
|See blogs|Open a blog|View the blog|
|Create an account|Account details|Account created|
|Log in|Account details|Logged in|
|Comment on a blog|Write a comment|Comment is posted|
|Submit a blog|Create a blog|Blog is submitted|

## Live link to the application's website in heroku



## Contacts

email me here: jasonmkinyua@gmail.com

## License Information

MIT License

Copyright (c) 2019 cooldragon