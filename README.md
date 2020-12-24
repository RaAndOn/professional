# PRODUCTION

## Heroku:

### Hide Secrets:

You can avoid having your secrets in the github repository by adding them directly to Heroku as constants using the following:

  `$ heroku config:set SECRET_KEY=`

Any constant created this way can be captured by using

  ```
    os.environ.get('SECRET_KEY')
  ```

For development, I recommend creating a 'secret_settings.py' file and adding it to your .gitignore. Then if settings_secrets.py exists
import it to the settings, otherwise use the 'os.environ.get('')'

### Push code:

  `$ git push heroku master`

### Migrate changes:

  `$ heroku run python manage.py migrate`

### Add domains:

  `$ heroku domains:add www.joshua-raanan.com -a joshua-raanan-professional`
  `$ heroku domains:add joshua-raanan.com -a joshua-raanan-professional`

Go to Hover and under the DNS tab add 2 new settings:

  Hover -> DNS
  TYPE: CNAME
  HOST: www
  VALUE: www.joshua-raanan.com.herokudns.com

  Hover -> DNS
  TYPE: CNAME
  HOST: @
  VALUE: joshua-raanan.com.herokudns.com

### Add SSL:

Heroku is capable of handling SSL for you, simply use the command:

  `$ heroku certs:auto:enable`

Add 'django-secure' to the requirements.txt, and add 'djangosecure' to INSTALLED_APPS in the settings.py.
Also make sure that the MIDDLEWARE includes 'django.middleware.security.SecurityMiddleware'. Finally add the
setting 'SECURE_SSL_REDIRECT = True'

SSH into server:

  `$ heroku ps:exec --dyno=web.1`

### Database:
This site uses Postgresql. The database settings on the server, which are needed in the settings.py file, are accessible
via the Heroku constant 'DATABASE_URL' and can be seen with the command:

  ` $heroku config:get DATABASE_URL -a joshua-raanan-professional`

This returns a uri broken down into:

postgres://username:password@host:port/name

However, in django this can be parsed with the dj-database-url package. Add this to the requirements.txt and add the following
to the settings.py. Which consists of Database default (used for development), and then overriding that for production.
  ```
    import dj_database_url
    DATABASES = {}
    DATABASES['default'] =  dj_database_url.config()
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
  ```

### Python Version
Specify the version of python to use when deploying in the `runtime.txt` file.

## Media

In production the uploaded images are stored in AWS.
https://devcenter.heroku.com/articles/s3#pass-through-uploads
https://devcenter.heroku.com/articles/s3-upload-python
https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html

Locally the uploaded images are stored in the `media/` folder

# DEVELOPMENT

## Setup

### Provide Required Values

Create a file called `development_settings.py` with the following contents:

```
#!/usr/bin/env python

SECRET_KEY = "ThisIsntTheActualSecretKey"
```
The actual secret key is stored on Heroku, but the existence of this file will cause django to run
the site using development settings.

### Database

SETUP POSGRES DATABASE AND SERVER
```
  ethel$ sudo apt-get install libpq-dev
  ethel$ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
  ethel$ sudo su - postgres
  postgres$ psql
  postgres# CREATE DATABASE professional;
  postgres# CREATE USER [USER] WITH PASSWORD '[PASSWORD]';
  postgres# ALTER ROLE [USER] SET client_encoding TO 'utf8';
  postgres# ALTER ROLE [USER] SET default_transaction_isolation TO 'read committed';
  postgres# ALTER ROLE [USER] SET timezone TO 'UTC';
  postgres# GRANT ALL PRIVILEGES ON DATABASE [DATABASE] TO [USER];
  \q
  exit
```

### Testing
```
python3 -Wa manage.py test
```

### Running the Website
```
python3 manage.py runserver
```

# DESIGN

Logo made with: https://www.canva.com/design/DACfQNJIaWw/vOxOIXQ8hySkXXDUx9Z-ZQ/edit?layouts=&utm_source=onboarding

### Fonts

Header - Bebas neue

Body - Arial

Added setting secrets to Heroku constants
