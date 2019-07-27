# Django CMS Contact Form

This is a django cms based application for working contact form with validation which sends EMAIL to specified receipent and also gives freedom to user to CC themselves

## Features
- Working contact form which sends mail to specified receipent with subject, message and mail of sender.
- User Friendly Interface.
- User can opt to receive the same mail.

## Requirenments
See the [Python/Django requirements for the current release version](http://docs.django-cms.org/en/latest/#software-version-requirements-and-release-notes) in our documentation.

See the [installation how-to guide for an overview of some other requirements and dependencies of the current release](http://docs.django-cms.org/en/latest/how_to/install.html)

## Installation
Follow the following steps to setup this application on your local system:
```
# Setup Development environment
$ virtualenv env  
$ source env/bin/activate

# Clone Repository
$ git clone https://github.com/shreyaagrawal0809/djangocms_contact_form.git
$ cd djangocms_contact_form

# Install all dependencies
$ cd contact_form
$ pip install -r requirements.txt

# Update Mail Credentials
$ cd contact_form
$ vim settings.py

edit following lines at the last of settings:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'emailwhichwillsendmails'
EMAIL_HOST_PASSWORD = 'password'

change 'emailwhichwillsendmails' with mail which will send emails to receipent and 'password' to its password

# Update receipent mail address
$ vim views.py

edit following lines in views.py
  recipients = ['shreyaagrawal0809@gmail.com']
  
edit shreyaagrawal0809@gmail.com to email address you want to receive contact mails

# Run the server
$ python manage.py runserver
```
## Create admin user
```
python manage.py createsuperuser
```
