# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse201(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, username: str=None):  # noqa: E501
        """InlineResponse201 - a model defined in Swagger

        :param id: The id of this InlineResponse201.  # noqa: E501
        :type id: int
        :param username: The username of this InlineResponse201.  # noqa: E501
        :type username: str
        """
        self.swagger_types = {
            'id': int,
            'username': str
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username'
        }
        self._id = id
        self._username = username

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse201':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201 of this InlineResponse201.  # noqa: E501
        :rtype: InlineResponse201
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this InlineResponse201.


        :return: The id of this InlineResponse201.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this InlineResponse201.


        :param id: The id of this InlineResponse201.
        :type id: int
        """

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this InlineResponse201.


        :return: The username of this InlineResponse201.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this InlineResponse201.


        :param username: The username of this InlineResponse201.
        :type username: str
        """

        self._username = username
