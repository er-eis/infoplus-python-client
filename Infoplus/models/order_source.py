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


class OrderSource(object):
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
        'lob_id': 'int',
        'name': 'str',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'packing_notes': 'str',
        'require_cartonized_asn': 'bool',
        'uses_reservations': 'bool',
        'require_gs1128_label': 'bool',
        'shipping_notes': 'str',
        'packing_slip_id': 'int',
        'order_invoice_id': 'int',
        'order_confirmation_email_id': 'int',
        'shipment_confirmation_email_id': 'int',
        'out_for_delivery_confirmation_email_id': 'int',
        'delivered_confirmation_email_id': 'int',
        'default_service_type_id': 'int',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'lob_id': 'lobId',
        'name': 'name',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'packing_notes': 'packingNotes',
        'require_cartonized_asn': 'requireCartonizedASN',
        'uses_reservations': 'usesReservations',
        'require_gs1128_label': 'requireGS1128Label',
        'shipping_notes': 'shippingNotes',
        'packing_slip_id': 'packingSlipId',
        'order_invoice_id': 'orderInvoiceId',
        'order_confirmation_email_id': 'orderConfirmationEmailId',
        'shipment_confirmation_email_id': 'shipmentConfirmationEmailId',
        'out_for_delivery_confirmation_email_id': 'outForDeliveryConfirmationEmailId',
        'delivered_confirmation_email_id': 'deliveredConfirmationEmailId',
        'default_service_type_id': 'defaultServiceTypeId',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, lob_id=None, name=None, create_date=None, modify_date=None, packing_notes=None, require_cartonized_asn=False, uses_reservations=False, require_gs1128_label=False, shipping_notes=None, packing_slip_id=None, order_invoice_id=None, order_confirmation_email_id=None, shipment_confirmation_email_id=None, out_for_delivery_confirmation_email_id=None, delivered_confirmation_email_id=None, default_service_type_id=None, custom_fields=None):  # noqa: E501
        """OrderSource - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._lob_id = None
        self._name = None
        self._create_date = None
        self._modify_date = None
        self._packing_notes = None
        self._require_cartonized_asn = None
        self._uses_reservations = None
        self._require_gs1128_label = None
        self._shipping_notes = None
        self._packing_slip_id = None
        self._order_invoice_id = None
        self._order_confirmation_email_id = None
        self._shipment_confirmation_email_id = None
        self._out_for_delivery_confirmation_email_id = None
        self._delivered_confirmation_email_id = None
        self._default_service_type_id = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.lob_id = lob_id
        self.name = name
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if packing_notes is not None:
            self.packing_notes = packing_notes
        if require_cartonized_asn is not None:
            self.require_cartonized_asn = require_cartonized_asn
        if uses_reservations is not None:
            self.uses_reservations = uses_reservations
        if require_gs1128_label is not None:
            self.require_gs1128_label = require_gs1128_label
        if shipping_notes is not None:
            self.shipping_notes = shipping_notes
        if packing_slip_id is not None:
            self.packing_slip_id = packing_slip_id
        if order_invoice_id is not None:
            self.order_invoice_id = order_invoice_id
        if order_confirmation_email_id is not None:
            self.order_confirmation_email_id = order_confirmation_email_id
        if shipment_confirmation_email_id is not None:
            self.shipment_confirmation_email_id = shipment_confirmation_email_id
        if out_for_delivery_confirmation_email_id is not None:
            self.out_for_delivery_confirmation_email_id = out_for_delivery_confirmation_email_id
        if delivered_confirmation_email_id is not None:
            self.delivered_confirmation_email_id = delivered_confirmation_email_id
        if default_service_type_id is not None:
            self.default_service_type_id = default_service_type_id
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this OrderSource.  # noqa: E501


        :return: The id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderSource.


        :param id: The id of this OrderSource.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lob_id(self):
        """Gets the lob_id of this OrderSource.  # noqa: E501


        :return: The lob_id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this OrderSource.


        :param lob_id: The lob_id of this OrderSource.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def name(self):
        """Gets the name of this OrderSource.  # noqa: E501


        :return: The name of this OrderSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrderSource.


        :param name: The name of this OrderSource.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def create_date(self):
        """Gets the create_date of this OrderSource.  # noqa: E501


        :return: The create_date of this OrderSource.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this OrderSource.


        :param create_date: The create_date of this OrderSource.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this OrderSource.  # noqa: E501


        :return: The modify_date of this OrderSource.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this OrderSource.


        :param modify_date: The modify_date of this OrderSource.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def packing_notes(self):
        """Gets the packing_notes of this OrderSource.  # noqa: E501


        :return: The packing_notes of this OrderSource.  # noqa: E501
        :rtype: str
        """
        return self._packing_notes

    @packing_notes.setter
    def packing_notes(self, packing_notes):
        """Sets the packing_notes of this OrderSource.


        :param packing_notes: The packing_notes of this OrderSource.  # noqa: E501
        :type: str
        """

        self._packing_notes = packing_notes

    @property
    def require_cartonized_asn(self):
        """Gets the require_cartonized_asn of this OrderSource.  # noqa: E501


        :return: The require_cartonized_asn of this OrderSource.  # noqa: E501
        :rtype: bool
        """
        return self._require_cartonized_asn

    @require_cartonized_asn.setter
    def require_cartonized_asn(self, require_cartonized_asn):
        """Sets the require_cartonized_asn of this OrderSource.


        :param require_cartonized_asn: The require_cartonized_asn of this OrderSource.  # noqa: E501
        :type: bool
        """

        self._require_cartonized_asn = require_cartonized_asn

    @property
    def uses_reservations(self):
        """Gets the uses_reservations of this OrderSource.  # noqa: E501


        :return: The uses_reservations of this OrderSource.  # noqa: E501
        :rtype: bool
        """
        return self._uses_reservations

    @uses_reservations.setter
    def uses_reservations(self, uses_reservations):
        """Sets the uses_reservations of this OrderSource.


        :param uses_reservations: The uses_reservations of this OrderSource.  # noqa: E501
        :type: bool
        """

        self._uses_reservations = uses_reservations

    @property
    def require_gs1128_label(self):
        """Gets the require_gs1128_label of this OrderSource.  # noqa: E501


        :return: The require_gs1128_label of this OrderSource.  # noqa: E501
        :rtype: bool
        """
        return self._require_gs1128_label

    @require_gs1128_label.setter
    def require_gs1128_label(self, require_gs1128_label):
        """Sets the require_gs1128_label of this OrderSource.


        :param require_gs1128_label: The require_gs1128_label of this OrderSource.  # noqa: E501
        :type: bool
        """

        self._require_gs1128_label = require_gs1128_label

    @property
    def shipping_notes(self):
        """Gets the shipping_notes of this OrderSource.  # noqa: E501


        :return: The shipping_notes of this OrderSource.  # noqa: E501
        :rtype: str
        """
        return self._shipping_notes

    @shipping_notes.setter
    def shipping_notes(self, shipping_notes):
        """Sets the shipping_notes of this OrderSource.


        :param shipping_notes: The shipping_notes of this OrderSource.  # noqa: E501
        :type: str
        """

        self._shipping_notes = shipping_notes

    @property
    def packing_slip_id(self):
        """Gets the packing_slip_id of this OrderSource.  # noqa: E501


        :return: The packing_slip_id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._packing_slip_id

    @packing_slip_id.setter
    def packing_slip_id(self, packing_slip_id):
        """Sets the packing_slip_id of this OrderSource.


        :param packing_slip_id: The packing_slip_id of this OrderSource.  # noqa: E501
        :type: int
        """

        self._packing_slip_id = packing_slip_id

    @property
    def order_invoice_id(self):
        """Gets the order_invoice_id of this OrderSource.  # noqa: E501


        :return: The order_invoice_id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._order_invoice_id

    @order_invoice_id.setter
    def order_invoice_id(self, order_invoice_id):
        """Sets the order_invoice_id of this OrderSource.


        :param order_invoice_id: The order_invoice_id of this OrderSource.  # noqa: E501
        :type: int
        """

        self._order_invoice_id = order_invoice_id

    @property
    def order_confirmation_email_id(self):
        """Gets the order_confirmation_email_id of this OrderSource.  # noqa: E501


        :return: The order_confirmation_email_id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._order_confirmation_email_id

    @order_confirmation_email_id.setter
    def order_confirmation_email_id(self, order_confirmation_email_id):
        """Sets the order_confirmation_email_id of this OrderSource.


        :param order_confirmation_email_id: The order_confirmation_email_id of this OrderSource.  # noqa: E501
        :type: int
        """

        self._order_confirmation_email_id = order_confirmation_email_id

    @property
    def shipment_confirmation_email_id(self):
        """Gets the shipment_confirmation_email_id of this OrderSource.  # noqa: E501


        :return: The shipment_confirmation_email_id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._shipment_confirmation_email_id

    @shipment_confirmation_email_id.setter
    def shipment_confirmation_email_id(self, shipment_confirmation_email_id):
        """Sets the shipment_confirmation_email_id of this OrderSource.


        :param shipment_confirmation_email_id: The shipment_confirmation_email_id of this OrderSource.  # noqa: E501
        :type: int
        """

        self._shipment_confirmation_email_id = shipment_confirmation_email_id

    @property
    def out_for_delivery_confirmation_email_id(self):
        """Gets the out_for_delivery_confirmation_email_id of this OrderSource.  # noqa: E501


        :return: The out_for_delivery_confirmation_email_id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._out_for_delivery_confirmation_email_id

    @out_for_delivery_confirmation_email_id.setter
    def out_for_delivery_confirmation_email_id(self, out_for_delivery_confirmation_email_id):
        """Sets the out_for_delivery_confirmation_email_id of this OrderSource.


        :param out_for_delivery_confirmation_email_id: The out_for_delivery_confirmation_email_id of this OrderSource.  # noqa: E501
        :type: int
        """

        self._out_for_delivery_confirmation_email_id = out_for_delivery_confirmation_email_id

    @property
    def delivered_confirmation_email_id(self):
        """Gets the delivered_confirmation_email_id of this OrderSource.  # noqa: E501


        :return: The delivered_confirmation_email_id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._delivered_confirmation_email_id

    @delivered_confirmation_email_id.setter
    def delivered_confirmation_email_id(self, delivered_confirmation_email_id):
        """Sets the delivered_confirmation_email_id of this OrderSource.


        :param delivered_confirmation_email_id: The delivered_confirmation_email_id of this OrderSource.  # noqa: E501
        :type: int
        """

        self._delivered_confirmation_email_id = delivered_confirmation_email_id

    @property
    def default_service_type_id(self):
        """Gets the default_service_type_id of this OrderSource.  # noqa: E501


        :return: The default_service_type_id of this OrderSource.  # noqa: E501
        :rtype: int
        """
        return self._default_service_type_id

    @default_service_type_id.setter
    def default_service_type_id(self, default_service_type_id):
        """Sets the default_service_type_id of this OrderSource.


        :param default_service_type_id: The default_service_type_id of this OrderSource.  # noqa: E501
        :type: int
        """

        self._default_service_type_id = default_service_type_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderSource.  # noqa: E501


        :return: The custom_fields of this OrderSource.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderSource.


        :param custom_fields: The custom_fields of this OrderSource.  # noqa: E501
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
        if not isinstance(other, OrderSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
