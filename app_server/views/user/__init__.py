# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from flask import Blueprint

from app_server.views.user.login import Login
from app_server.views.user.logout import Logout
from app_server.views.user.register import Register
from app_server.views.user.members import Members
from app_server.views.user.administration import Administration
from app_server.views.user.edit import Edit

user_blueprint = Blueprint("user", __name__)

user_blueprint.add_url_rule("/login/", view_func=Login.as_view("login"))
user_blueprint.add_url_rule(
	"/register/", view_func=Register.as_view("register")
)
user_blueprint.add_url_rule("/logout/", view_func=Logout.as_view("logout"))
user_blueprint.add_url_rule("/members/", view_func=Members.as_view("members"))
user_blueprint.add_url_rule(
	"/administration/", view_func=Administration.as_view("administration")
)
user_blueprint.add_url_rule("/edit/<username>", view_func=Edit.as_view("edit"))
