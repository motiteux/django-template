.. {% comment %}

===============
Django Template
===============

``django-template`` provides a template for Django templates,
based on several sources. To use this template run the following command::

     django-admin.py startproject --template=https://github.com/motiteux/django-template/zipball/master --extension=py,rst,gitignore,md project_name

.. note:: The text following this comment block will become the README.rst of the new project.

-----

.. {% endcomment %}

# {{ project_name | title }} #
## Prerequisites ##

- python >= 2.7
- Django >= 1.4.*

## Installation ##
Get the code at <GIT_REPO>, using

```bash
git clone <GIT_REPO> {{ project_name }}
```

### Install requirements ###
If pip is your thing:

```bash
cd {{ project_name }}
pip install -r requirements.txt
```

### Configure project ###
```bash
cd {{ project_name }}
cp {{ project_name }}/settings/personal.py.dist {{ project_name }}/settings/personal.py
vi {{ project_name }}/personal.py
```

### Sync & migrate database ###
```bash
python manage.py syncdb
python manage.py migrate
```

## Running ##
```bash
python manage.py runserver
```

Open browser to http://127.0.0.1:8000