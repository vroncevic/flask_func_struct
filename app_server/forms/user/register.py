# -*- coding: utf-8 -*-

'''
 Module
     register.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     flask_func_struct is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as
     published by the Free Software Foundation, either version 3 of
     the License, or (at your option) any later version.
     flask_func_struct is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License
     along with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class UserRegisterForm with attribute(s) and method(s).
     Form for register user data.
'''

import sys

try:
    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField
    from wtforms.validators import DataRequired, Email, Length, EqualTo
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class UserRegisterForm(FlaskForm):
    '''
        Define class UserRegisterForm with attribute(s) and method(s).
        Define user registration form (creating new user - public operation).
        It defines:

            :attributes:
                | fullname - User fullname
                | username - User system name
                | email - User email contact
                | password - User password
                | confirm - User password confirm
            :methods:
                | None
    '''

    fullname = StringField('Fullname', validators=[Length(min=4, max=72)])
    username = StringField('Username', validators=[Length(min=4, max=32)])
    email = StringField(
        'Email Address',
        validators=[DataRequired(), Email(), Length(min=6, max=80)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=32)]
    )
    confirm = PasswordField(
        'Confirm password', validators=[DataRequired(), EqualTo('password')]
    )
