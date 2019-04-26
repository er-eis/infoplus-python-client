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


class Location(object):
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
        'warehouse_id': 'int',
        'building_id': 'int',
        'zone_id': 'int',
        'aisle_id': 'int',
        'billing_type_id': 'int',
        'behavior_type': 'str',
        'footprint_id': 'int',
        'address_scheme_id': 'int',
        'origin': 'int',
        'address': 'str',
        'level': 'int',
        'bay': 'int',
        'number': 'int',
        'online': 'bool',
        'priority_code': 'int',
        'cost': 'int',
        'allow_item_mixing': 'bool',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'warehouse_id': 'warehouseId',
        'building_id': 'buildingId',
        'zone_id': 'zoneId',
        'aisle_id': 'aisleId',
        'billing_type_id': 'billingTypeId',
        'behavior_type': 'behaviorType',
        'footprint_id': 'footprintId',
        'address_scheme_id': 'addressSchemeId',
        'origin': 'origin',
        'address': 'address',
        'level': 'level',
        'bay': 'bay',
        'number': 'number',
        'online': 'online',
        'priority_code': 'priorityCode',
        'cost': 'cost',
        'allow_item_mixing': 'allowItemMixing',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, warehouse_id=None, building_id=None, zone_id=None, aisle_id=None, billing_type_id=None, behavior_type=None, footprint_id=None, address_scheme_id=None, origin=None, address=None, level=None, bay=None, number=None, online=False, priority_code=None, cost=None, allow_item_mixing=False, create_date=None, modify_date=None, custom_fields=None):  # noqa: E501
        """Location - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._warehouse_id = None
        self._building_id = None
        self._zone_id = None
        self._aisle_id = None
        self._billing_type_id = None
        self._behavior_type = None
        self._footprint_id = None
        self._address_scheme_id = None
        self._origin = None
        self._address = None
        self._level = None
        self._bay = None
        self._number = None
        self._online = None
        self._priority_code = None
        self._cost = None
        self._allow_item_mixing = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.warehouse_id = warehouse_id
        if building_id is not None:
            self.building_id = building_id
        if zone_id is not None:
            self.zone_id = zone_id
        if aisle_id is not None:
            self.aisle_id = aisle_id
        self.billing_type_id = billing_type_id
        self.behavior_type = behavior_type
        self.footprint_id = footprint_id
        if address_scheme_id is not None:
            self.address_scheme_id = address_scheme_id
        if origin is not None:
            self.origin = origin
        if address is not None:
            self.address = address
        if level is not None:
            self.level = level
        if bay is not None:
            self.bay = bay
        if number is not None:
            self.number = number
        self.online = online
        if priority_code is not None:
            self.priority_code = priority_code
        if cost is not None:
            self.cost = cost
        self.allow_item_mixing = allow_item_mixing
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Location.  # noqa: E501


        :return: The id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Location.


        :param id: The id of this Location.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this Location.  # noqa: E501


        :return: The warehouse_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this Location.


        :param warehouse_id: The warehouse_id of this Location.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def building_id(self):
        """Gets the building_id of this Location.  # noqa: E501


        :return: The building_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this Location.


        :param building_id: The building_id of this Location.  # noqa: E501
        :type: int
        """

        self._building_id = building_id

    @property
    def zone_id(self):
        """Gets the zone_id of this Location.  # noqa: E501


        :return: The zone_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this Location.


        :param zone_id: The zone_id of this Location.  # noqa: E501
        :type: int
        """

        self._zone_id = zone_id

    @property
    def aisle_id(self):
        """Gets the aisle_id of this Location.  # noqa: E501


        :return: The aisle_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._aisle_id

    @aisle_id.setter
    def aisle_id(self, aisle_id):
        """Sets the aisle_id of this Location.


        :param aisle_id: The aisle_id of this Location.  # noqa: E501
        :type: int
        """

        self._aisle_id = aisle_id

    @property
    def billing_type_id(self):
        """Gets the billing_type_id of this Location.  # noqa: E501


        :return: The billing_type_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._billing_type_id

    @billing_type_id.setter
    def billing_type_id(self, billing_type_id):
        """Sets the billing_type_id of this Location.


        :param billing_type_id: The billing_type_id of this Location.  # noqa: E501
        :type: int
        """
        if billing_type_id is None:
            raise ValueError("Invalid value for `billing_type_id`, must not be `None`")  # noqa: E501

        self._billing_type_id = billing_type_id

    @property
    def behavior_type(self):
        """Gets the behavior_type of this Location.  # noqa: E501


        :return: The behavior_type of this Location.  # noqa: E501
        :rtype: str
        """
        return self._behavior_type

    @behavior_type.setter
    def behavior_type(self, behavior_type):
        """Sets the behavior_type of this Location.


        :param behavior_type: The behavior_type of this Location.  # noqa: E501
        :type: str
        """
        if behavior_type is None:
            raise ValueError("Invalid value for `behavior_type`, must not be `None`")  # noqa: E501

        self._behavior_type = behavior_type

    @property
    def footprint_id(self):
        """Gets the footprint_id of this Location.  # noqa: E501


        :return: The footprint_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._footprint_id

    @footprint_id.setter
    def footprint_id(self, footprint_id):
        """Sets the footprint_id of this Location.


        :param footprint_id: The footprint_id of this Location.  # noqa: E501
        :type: int
        """
        if footprint_id is None:
            raise ValueError("Invalid value for `footprint_id`, must not be `None`")  # noqa: E501

        self._footprint_id = footprint_id

    @property
    def address_scheme_id(self):
        """Gets the address_scheme_id of this Location.  # noqa: E501


        :return: The address_scheme_id of this Location.  # noqa: E501
        :rtype: int
        """
        return self._address_scheme_id

    @address_scheme_id.setter
    def address_scheme_id(self, address_scheme_id):
        """Sets the address_scheme_id of this Location.


        :param address_scheme_id: The address_scheme_id of this Location.  # noqa: E501
        :type: int
        """

        self._address_scheme_id = address_scheme_id

    @property
    def origin(self):
        """Gets the origin of this Location.  # noqa: E501


        :return: The origin of this Location.  # noqa: E501
        :rtype: int
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this Location.


        :param origin: The origin of this Location.  # noqa: E501
        :type: int
        """

        self._origin = origin

    @property
    def address(self):
        """Gets the address of this Location.  # noqa: E501


        :return: The address of this Location.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Location.


        :param address: The address of this Location.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def level(self):
        """Gets the level of this Location.  # noqa: E501


        :return: The level of this Location.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Location.


        :param level: The level of this Location.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def bay(self):
        """Gets the bay of this Location.  # noqa: E501


        :return: The bay of this Location.  # noqa: E501
        :rtype: int
        """
        return self._bay

    @bay.setter
    def bay(self, bay):
        """Sets the bay of this Location.


        :param bay: The bay of this Location.  # noqa: E501
        :type: int
        """

        self._bay = bay

    @property
    def number(self):
        """Gets the number of this Location.  # noqa: E501


        :return: The number of this Location.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Location.


        :param number: The number of this Location.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def online(self):
        """Gets the online of this Location.  # noqa: E501


        :return: The online of this Location.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this Location.


        :param online: The online of this Location.  # noqa: E501
        :type: bool
        """
        if online is None:
            raise ValueError("Invalid value for `online`, must not be `None`")  # noqa: E501

        self._online = online

    @property
    def priority_code(self):
        """Gets the priority_code of this Location.  # noqa: E501


        :return: The priority_code of this Location.  # noqa: E501
        :rtype: int
        """
        return self._priority_code

    @priority_code.setter
    def priority_code(self, priority_code):
        """Sets the priority_code of this Location.


        :param priority_code: The priority_code of this Location.  # noqa: E501
        :type: int
        """

        self._priority_code = priority_code

    @property
    def cost(self):
        """Gets the cost of this Location.  # noqa: E501


        :return: The cost of this Location.  # noqa: E501
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this Location.


        :param cost: The cost of this Location.  # noqa: E501
        :type: int
        """

        self._cost = cost

    @property
    def allow_item_mixing(self):
        """Gets the allow_item_mixing of this Location.  # noqa: E501


        :return: The allow_item_mixing of this Location.  # noqa: E501
        :rtype: bool
        """
        return self._allow_item_mixing

    @allow_item_mixing.setter
    def allow_item_mixing(self, allow_item_mixing):
        """Sets the allow_item_mixing of this Location.


        :param allow_item_mixing: The allow_item_mixing of this Location.  # noqa: E501
        :type: bool
        """
        if allow_item_mixing is None:
            raise ValueError("Invalid value for `allow_item_mixing`, must not be `None`")  # noqa: E501

        self._allow_item_mixing = allow_item_mixing

    @property
    def create_date(self):
        """Gets the create_date of this Location.  # noqa: E501


        :return: The create_date of this Location.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Location.


        :param create_date: The create_date of this Location.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this Location.  # noqa: E501


        :return: The modify_date of this Location.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this Location.


        :param modify_date: The modify_date of this Location.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Location.  # noqa: E501


        :return: The custom_fields of this Location.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Location.


        :param custom_fields: The custom_fields of this Location.  # noqa: E501
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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other