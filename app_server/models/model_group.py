# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

import datetime

from app_server import db
from app_server.models.model_base import Base


class Group(Base):
	"""
	Define class Group with attribute(s) and method(s).
	Model Group for user operations.
	It defines:
		attribute:
			name - Group name
		method:
			__init__ - Initial constructor
			get_id - Getting id
			__repr__ - Printable representation of the group
	"""

	__tablename__ = "groups"

	name = db.Column(db.String(255), unique=True, nullable=False)

	def __init__(self, name):
		"""
		:param name: Group name
		:type: str
		"""
		self.name = name
		self.modified = self.created = datetime.datetime.now()

	def get_id(self):
		"""
		:return: Getting id
		:type: int
		"""
		return self.id

	def __repr__(self):
		"""
		:return: Printable representation of the group
		:type: str
		"""
		return "<{0} {1}>".format(self.__class__.__name__, self.name)
