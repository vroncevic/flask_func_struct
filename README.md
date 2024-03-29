<img align="right" src="https://raw.githubusercontent.com/vroncevic/flask_func_struct/dev/docs/flask_func_struct_logo.png" width="25%">

# Flask Functional-Structured Framework

☯️ **flask_func_struct** is framework for managing Flask App.

Developed in 🐍 **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![flask_func_struct python checker](https://img.shields.io/github/workflow/status/vroncevic/flask_func_struct/flask_func_struct_python_checker?style=flat&label=flask_func_struct%20python%20checker)](https://github.com/vroncevic/flask_func_struct/actions/workflows/flask_func_struct_python_checker.yml) [![flask_func_struct package checker](https://img.shields.io/github/workflow/status/vroncevic/flask_func_struct/flask_func_struct_package_checker?style=flat&label=flask_func_struct%20package%20checker)](https://github.com/vroncevic/flask_func_struct/actions/workflows/flask_func_struct_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/flask_func_struct.svg)](https://github.com/vroncevic/flask_func_struct/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/flask_func_struct.svg)](https://github.com/vroncevic/flask_func_struct/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Package structure](#package-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/flask_func_struct/dev/docs/debtux.png)

Navigate to **[release page](https://github.com/vroncevic/flask_func_struct/releases)** download and extract release archive 📦.

To install **flask_func_struct** 📦 type the following

```bash
tar xvzf flask_func_struct-x.y.z.tar.gz
cd flask_func_struct-x.y.z/
pip install -r requirements.txt
cp manage.py /FlaskApp/
cp -R /manage_commands/ /FlaskApp/
cp -R /app_server/ /Flask/
```

Or You can use Dockerfile to create image/container 🚢.

[![flask_func_struct docker checker](https://img.shields.io/github/workflow/status/vroncevic/flask_func_struct/flask_func_struct_docker_checker?style=flat&label=flask_func_struct%20docker%20checker)](https://github.com/vroncevic/flask_func_struct/actions/workflows/flask_func_struct_docker_checker.yml)

### Usage

Create databse

```bash
$ python manage.py create_db
Create database/tables
Done
```

Init databse and prepare alembic table

```bash
$ python manage.py db init
  Creating directory /data/dev/python/flask_func_struct/github/flask_func_struct/migrations ...  done
  Creating directory /data/dev/python/flask_func_struct/github/flask_func_struct/migrations/versions ...  done
  Generating /data/dev/python/flask_func_struct/github/flask_func_struct/migrations/env.pyc ...  done
  Generating /data/dev/python/flask_func_struct/github/flask_func_struct/migrations/env.py ...  done
  Generating /data/dev/python/flask_func_struct/github/flask_func_struct/migrations/alembic.ini ...  done
  Generating /data/dev/python/flask_func_struct/github/flask_func_struct/migrations/README ...  done
  Generating /data/dev/python/flask_func_struct/github/flask_func_struct/migrations/script.py.mako ...  done
  Please edit configuration/connection/logging settings in
  '/data/dev/python/flask_func_struct/github/flask_func_struct/migrations/alembic.ini' before proceeding.
```

Generate a migration script that makes the database match the models

```bash
$ python manage.py db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.env] No changes in schema detected.
```

Create super user

```bash
$ python manage.py createsuperuser
Creating superuser account
Insert username of superuser: adroot
Insert email of superuser: adroot@test.com
Insert password of superuser: 
Done
```

Run application

```bash
$ python manage.py runserver
 * Serving Flask app "app_server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 226-526-932
```

### Dependencies

**flask_func_struct** requires other modules and libraries (Python 2.x)

```bash
alembic                           1.6.5
Flask                             1.1.4
Flask-Bcrypt                      1.0.1
Flask-Bootstrap                   3.3.7.1
Flask-Cors                        3.0.10
Flask-DebugToolbar                0.13.1
Flask-Login                       0.5.0
Flask-Mail                        0.9.1
Flask-Migrate                     2.6.0
Flask-Script                      2.0.6
Flask-SQLAlchemy                  2.5.1
Flask-Testing                     0.8.1
Flask-WTF                         0.14.3
SQLAlchemy                        1.4.27
Werkzeug                          1.0.1
WTForms                           2.3.3
```

### Package structure

🧰 Expected framework structure

```bash
app_server/
├── configuration/
│   ├── database/
│   │   ├── development_config.py
│   │   ├── __init__.py
│   │   ├── production_config.py
│   │   └── test_config.py
│   ├── development_config.py
│   ├── __init__.py
│   ├── mail/
│   │   ├── development_config.py
│   │   ├── __init__.py
│   │   ├── production_config.py
│   │   └── test_config.py
│   ├── production_config.py
│   └── test_config.py
├── forms/
│   ├── base/
│   │   ├── contact.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── user/
│       ├── edit.py
│       ├── __init__.py
│       ├── login.py
│       └── register.py
├── __init__.py
├── models/
│   ├── __init__.py
│   └── model_user.py
├── static/
│   ├── base.css
│   └── favicon.ico
├── templates/
│   ├── base/
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── home.html
│   ├── _base.html
│   ├── errors/
│   │   ├── 401.html
│   │   ├── 403.html
│   │   ├── 404.html
│   │   └── 500.html
│   ├── footer.html
│   ├── header.html
│   └── user/
│       ├── administration.html
│       ├── edit.html
│       ├── login.html
│       ├── members.html
│       └── register.html
└── views/
    ├── base/
    │   ├── about.py
    │   ├── contact.py
    │   ├── home.py
    │   └── __init__.py
    ├── __init__.py
    └── user/
        ├── administration.py
        ├── edit.py
        ├── __init__.py
        ├── login.py
        ├── logout.py
        ├── members.py
        └── register.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/flask-func-struct/badge/?version=latest)](https://flask-func-struct.readthedocs.io/en/latest/?badge=latest)

📗 More documentation and info at

* [flask_func_struct.readthedocs.io](https://flask_func_struct.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

🌎 🌍 🌏 [Contributing to config_flask](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 by [vroncevic.github.io/flask_func_struct](https://vroncevic.github.io/flask_func_struct/)

**flask_func_struct** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x or,
at your option, any later version of Python 2 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/flask_func_struct/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
