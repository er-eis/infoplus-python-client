# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ScheduledPlanLog(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'scheduled_plan_id': 'int',
        'plan': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'status': 'str',
        'message': 'str',
        'link_url': 'str',
        'link_text': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'scheduled_plan_id': 'scheduledPlanId',
        'plan': 'plan',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'status': 'status',
        'message': 'message',
        'link_url': 'linkURL',
        'link_text': 'linkText',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, scheduled_plan_id=None, plan=None, start_time=None, end_time=None, status=None, message=None, link_url=None, link_text=None, custom_fields=None):  # noqa: E501
        """ScheduledPlanLog - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._scheduled_plan_id = None
        self._plan = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._message = None
        self._link_url = None
        self._link_text = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if scheduled_plan_id is not None:
            self.scheduled_plan_id = scheduled_plan_id
        if plan is not None:
            self.plan = plan
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.status = status
        if message is not None:
            self.message = message
        if link_url is not None:
            self.link_url = link_url
        if link_text is not None:
            self.link_text = link_text
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ScheduledPlanLog.  # noqa: E501


        :return: The id of this ScheduledPlanLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScheduledPlanLog.


        :param id: The id of this ScheduledPlanLog.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this ScheduledPlanLog.  # noqa: E501


        :return: The create_date of this ScheduledPlanLog.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ScheduledPlanLog.


        :param create_date: The create_date of this ScheduledPlanLog.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ScheduledPlanLog.  # noqa: E501


        :return: The modify_date of this ScheduledPlanLog.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ScheduledPlanLog.


        :param modify_date: The modify_date of this ScheduledPlanLog.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def scheduled_plan_id(self):
        """Gets the scheduled_plan_id of this ScheduledPlanLog.  # noqa: E501


        :return: The scheduled_plan_id of this ScheduledPlanLog.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_plan_id

    @scheduled_plan_id.setter
    def scheduled_plan_id(self, scheduled_plan_id):
        """Sets the scheduled_plan_id of this ScheduledPlanLog.


        :param scheduled_plan_id: The scheduled_plan_id of this ScheduledPlanLog.  # noqa: E501
        :type: int
        """

        self._scheduled_plan_id = scheduled_plan_id

    @property
    def plan(self):
        """Gets the plan of this ScheduledPlanLog.  # noqa: E501


        :return: The plan of this ScheduledPlanLog.  # noqa: E501
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this ScheduledPlanLog.


        :param plan: The plan of this ScheduledPlanLog.  # noqa: E501
        :type: str
        """

        self._plan = plan

    @property
    def start_time(self):
        """Gets the start_time of this ScheduledPlanLog.  # noqa: E501


        :return: The start_time of this ScheduledPlanLog.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScheduledPlanLog.


        :param start_time: The start_time of this ScheduledPlanLog.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScheduledPlanLog.  # noqa: E501


        :return: The end_time of this ScheduledPlanLog.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScheduledPlanLog.


        :param end_time: The end_time of this ScheduledPlanLog.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ScheduledPlanLog.  # noqa: E501


        :return: The status of this ScheduledPlanLog.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScheduledPlanLog.


        :param status: The status of this ScheduledPlanLog.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this ScheduledPlanLog.  # noqa: E501


        :return: The message of this ScheduledPlanLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ScheduledPlanLog.


        :param message: The message of this ScheduledPlanLog.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def link_url(self):
        """Gets the link_url of this ScheduledPlanLog.  # noqa: E501


        :return: The link_url of this ScheduledPlanLog.  # noqa: E501
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url):
        """Sets the link_url of this ScheduledPlanLog.


        :param link_url: The link_url of this ScheduledPlanLog.  # noqa: E501
        :type: str
        """

        self._link_url = link_url

    @property
    def link_text(self):
        """Gets the link_text of this ScheduledPlanLog.  # noqa: E501


        :return: The link_text of this ScheduledPlanLog.  # noqa: E501
        :rtype: str
        """
        return self._link_text

    @link_text.setter
    def link_text(self, link_text):
        """Sets the link_text of this ScheduledPlanLog.


        :param link_text: The link_text of this ScheduledPlanLog.  # noqa: E501
        :type: str
        """

        self._link_text = link_text

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ScheduledPlanLog.  # noqa: E501


        :return: The custom_fields of this ScheduledPlanLog.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ScheduledPlanLog.


        :param custom_fields: The custom_fields of this ScheduledPlanLog.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduledPlanLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other