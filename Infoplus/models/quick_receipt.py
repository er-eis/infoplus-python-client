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


class QuickReceipt(object):
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
        'created_by': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'warehouse_id': 'int',
        'lob_id': 'int',
        'location_id': 'int',
        'quantity': 'int',
        'vendor_id': 'int',
        'carrier': 'str',
        'status': 'str',
        'unit_code': 'str',
        'wrap_code': 'str',
        'weight_per_wrap': 'float',
        'units_per_wrap': 'int',
        'units_per_case': 'int',
        'cases_per_pallet': 'int',
        'case_weight': 'float',
        'production_lot': 'str',
        'revision_date': 'str',
        'origin': 'str',
        'carton_length': 'float',
        'carton_width': 'float',
        'carton_height': 'float',
        'cost': 'float',
        'sell_price': 'float',
        'pricing_per': 'str',
        'generated_item_receipt_id': 'int',
        'generated_asn_id': 'int',
        'dock_date': 'datetime',
        'product_id_tag': 'str',
        'custom_fields': 'dict(str, object)',
        'sku': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'warehouse_id': 'warehouseId',
        'lob_id': 'lobId',
        'location_id': 'locationId',
        'quantity': 'quantity',
        'vendor_id': 'vendorId',
        'carrier': 'carrier',
        'status': 'status',
        'unit_code': 'unitCode',
        'wrap_code': 'wrapCode',
        'weight_per_wrap': 'weightPerWrap',
        'units_per_wrap': 'unitsPerWrap',
        'units_per_case': 'unitsPerCase',
        'cases_per_pallet': 'casesPerPallet',
        'case_weight': 'caseWeight',
        'production_lot': 'productionLot',
        'revision_date': 'revisionDate',
        'origin': 'origin',
        'carton_length': 'cartonLength',
        'carton_width': 'cartonWidth',
        'carton_height': 'cartonHeight',
        'cost': 'cost',
        'sell_price': 'sellPrice',
        'pricing_per': 'pricingPer',
        'generated_item_receipt_id': 'generatedItemReceiptId',
        'generated_asn_id': 'generatedASNId',
        'dock_date': 'dockDate',
        'product_id_tag': 'productIdTag',
        'custom_fields': 'customFields',
        'sku': 'sku'
    }

    def __init__(self, id=None, created_by=None, create_date=None, modify_date=None, warehouse_id=None, lob_id=None, location_id=None, quantity=None, vendor_id=None, carrier=None, status=None, unit_code=None, wrap_code=None, weight_per_wrap=None, units_per_wrap=None, units_per_case=None, cases_per_pallet=None, case_weight=None, production_lot=None, revision_date=None, origin=None, carton_length=None, carton_width=None, carton_height=None, cost=None, sell_price=None, pricing_per=None, generated_item_receipt_id=None, generated_asn_id=None, dock_date=None, product_id_tag=None, custom_fields=None, sku=None):  # noqa: E501
        """QuickReceipt - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_by = None
        self._create_date = None
        self._modify_date = None
        self._warehouse_id = None
        self._lob_id = None
        self._location_id = None
        self._quantity = None
        self._vendor_id = None
        self._carrier = None
        self._status = None
        self._unit_code = None
        self._wrap_code = None
        self._weight_per_wrap = None
        self._units_per_wrap = None
        self._units_per_case = None
        self._cases_per_pallet = None
        self._case_weight = None
        self._production_lot = None
        self._revision_date = None
        self._origin = None
        self._carton_length = None
        self._carton_width = None
        self._carton_height = None
        self._cost = None
        self._sell_price = None
        self._pricing_per = None
        self._generated_item_receipt_id = None
        self._generated_asn_id = None
        self._dock_date = None
        self._product_id_tag = None
        self._custom_fields = None
        self._sku = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_by is not None:
            self.created_by = created_by
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        self.warehouse_id = warehouse_id
        self.lob_id = lob_id
        self.location_id = location_id
        self.quantity = quantity
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if carrier is not None:
            self.carrier = carrier
        if status is not None:
            self.status = status
        self.unit_code = unit_code
        self.wrap_code = wrap_code
        self.weight_per_wrap = weight_per_wrap
        self.units_per_wrap = units_per_wrap
        if units_per_case is not None:
            self.units_per_case = units_per_case
        if cases_per_pallet is not None:
            self.cases_per_pallet = cases_per_pallet
        if case_weight is not None:
            self.case_weight = case_weight
        if production_lot is not None:
            self.production_lot = production_lot
        if revision_date is not None:
            self.revision_date = revision_date
        if origin is not None:
            self.origin = origin
        if carton_length is not None:
            self.carton_length = carton_length
        if carton_width is not None:
            self.carton_width = carton_width
        if carton_height is not None:
            self.carton_height = carton_height
        if cost is not None:
            self.cost = cost
        if sell_price is not None:
            self.sell_price = sell_price
        if pricing_per is not None:
            self.pricing_per = pricing_per
        if generated_item_receipt_id is not None:
            self.generated_item_receipt_id = generated_item_receipt_id
        if generated_asn_id is not None:
            self.generated_asn_id = generated_asn_id
        if dock_date is not None:
            self.dock_date = dock_date
        if product_id_tag is not None:
            self.product_id_tag = product_id_tag
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if sku is not None:
            self.sku = sku

    @property
    def id(self):
        """Gets the id of this QuickReceipt.  # noqa: E501


        :return: The id of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuickReceipt.


        :param id: The id of this QuickReceipt.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this QuickReceipt.  # noqa: E501


        :return: The created_by of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this QuickReceipt.


        :param created_by: The created_by of this QuickReceipt.  # noqa: E501
        :type: int
        """

        self._created_by = created_by

    @property
    def create_date(self):
        """Gets the create_date of this QuickReceipt.  # noqa: E501


        :return: The create_date of this QuickReceipt.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this QuickReceipt.


        :param create_date: The create_date of this QuickReceipt.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this QuickReceipt.  # noqa: E501


        :return: The modify_date of this QuickReceipt.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this QuickReceipt.


        :param modify_date: The modify_date of this QuickReceipt.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this QuickReceipt.  # noqa: E501


        :return: The warehouse_id of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this QuickReceipt.


        :param warehouse_id: The warehouse_id of this QuickReceipt.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def lob_id(self):
        """Gets the lob_id of this QuickReceipt.  # noqa: E501


        :return: The lob_id of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this QuickReceipt.


        :param lob_id: The lob_id of this QuickReceipt.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def location_id(self):
        """Gets the location_id of this QuickReceipt.  # noqa: E501


        :return: The location_id of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this QuickReceipt.


        :param location_id: The location_id of this QuickReceipt.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def quantity(self):
        """Gets the quantity of this QuickReceipt.  # noqa: E501


        :return: The quantity of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this QuickReceipt.


        :param quantity: The quantity of this QuickReceipt.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def vendor_id(self):
        """Gets the vendor_id of this QuickReceipt.  # noqa: E501


        :return: The vendor_id of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this QuickReceipt.


        :param vendor_id: The vendor_id of this QuickReceipt.  # noqa: E501
        :type: int
        """

        self._vendor_id = vendor_id

    @property
    def carrier(self):
        """Gets the carrier of this QuickReceipt.  # noqa: E501


        :return: The carrier of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this QuickReceipt.


        :param carrier: The carrier of this QuickReceipt.  # noqa: E501
        :type: str
        """

        self._carrier = carrier

    @property
    def status(self):
        """Gets the status of this QuickReceipt.  # noqa: E501


        :return: The status of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QuickReceipt.


        :param status: The status of this QuickReceipt.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def unit_code(self):
        """Gets the unit_code of this QuickReceipt.  # noqa: E501


        :return: The unit_code of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._unit_code

    @unit_code.setter
    def unit_code(self, unit_code):
        """Sets the unit_code of this QuickReceipt.


        :param unit_code: The unit_code of this QuickReceipt.  # noqa: E501
        :type: str
        """
        if unit_code is None:
            raise ValueError("Invalid value for `unit_code`, must not be `None`")  # noqa: E501

        self._unit_code = unit_code

    @property
    def wrap_code(self):
        """Gets the wrap_code of this QuickReceipt.  # noqa: E501


        :return: The wrap_code of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._wrap_code

    @wrap_code.setter
    def wrap_code(self, wrap_code):
        """Sets the wrap_code of this QuickReceipt.


        :param wrap_code: The wrap_code of this QuickReceipt.  # noqa: E501
        :type: str
        """
        if wrap_code is None:
            raise ValueError("Invalid value for `wrap_code`, must not be `None`")  # noqa: E501

        self._wrap_code = wrap_code

    @property
    def weight_per_wrap(self):
        """Gets the weight_per_wrap of this QuickReceipt.  # noqa: E501


        :return: The weight_per_wrap of this QuickReceipt.  # noqa: E501
        :rtype: float
        """
        return self._weight_per_wrap

    @weight_per_wrap.setter
    def weight_per_wrap(self, weight_per_wrap):
        """Sets the weight_per_wrap of this QuickReceipt.


        :param weight_per_wrap: The weight_per_wrap of this QuickReceipt.  # noqa: E501
        :type: float
        """
        if weight_per_wrap is None:
            raise ValueError("Invalid value for `weight_per_wrap`, must not be `None`")  # noqa: E501

        self._weight_per_wrap = weight_per_wrap

    @property
    def units_per_wrap(self):
        """Gets the units_per_wrap of this QuickReceipt.  # noqa: E501


        :return: The units_per_wrap of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._units_per_wrap

    @units_per_wrap.setter
    def units_per_wrap(self, units_per_wrap):
        """Sets the units_per_wrap of this QuickReceipt.


        :param units_per_wrap: The units_per_wrap of this QuickReceipt.  # noqa: E501
        :type: int
        """
        if units_per_wrap is None:
            raise ValueError("Invalid value for `units_per_wrap`, must not be `None`")  # noqa: E501

        self._units_per_wrap = units_per_wrap

    @property
    def units_per_case(self):
        """Gets the units_per_case of this QuickReceipt.  # noqa: E501


        :return: The units_per_case of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._units_per_case

    @units_per_case.setter
    def units_per_case(self, units_per_case):
        """Sets the units_per_case of this QuickReceipt.


        :param units_per_case: The units_per_case of this QuickReceipt.  # noqa: E501
        :type: int
        """

        self._units_per_case = units_per_case

    @property
    def cases_per_pallet(self):
        """Gets the cases_per_pallet of this QuickReceipt.  # noqa: E501


        :return: The cases_per_pallet of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._cases_per_pallet

    @cases_per_pallet.setter
    def cases_per_pallet(self, cases_per_pallet):
        """Sets the cases_per_pallet of this QuickReceipt.


        :param cases_per_pallet: The cases_per_pallet of this QuickReceipt.  # noqa: E501
        :type: int
        """

        self._cases_per_pallet = cases_per_pallet

    @property
    def case_weight(self):
        """Gets the case_weight of this QuickReceipt.  # noqa: E501


        :return: The case_weight of this QuickReceipt.  # noqa: E501
        :rtype: float
        """
        return self._case_weight

    @case_weight.setter
    def case_weight(self, case_weight):
        """Sets the case_weight of this QuickReceipt.


        :param case_weight: The case_weight of this QuickReceipt.  # noqa: E501
        :type: float
        """

        self._case_weight = case_weight

    @property
    def production_lot(self):
        """Gets the production_lot of this QuickReceipt.  # noqa: E501


        :return: The production_lot of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._production_lot

    @production_lot.setter
    def production_lot(self, production_lot):
        """Sets the production_lot of this QuickReceipt.


        :param production_lot: The production_lot of this QuickReceipt.  # noqa: E501
        :type: str
        """

        self._production_lot = production_lot

    @property
    def revision_date(self):
        """Gets the revision_date of this QuickReceipt.  # noqa: E501


        :return: The revision_date of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._revision_date

    @revision_date.setter
    def revision_date(self, revision_date):
        """Sets the revision_date of this QuickReceipt.


        :param revision_date: The revision_date of this QuickReceipt.  # noqa: E501
        :type: str
        """

        self._revision_date = revision_date

    @property
    def origin(self):
        """Gets the origin of this QuickReceipt.  # noqa: E501


        :return: The origin of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this QuickReceipt.


        :param origin: The origin of this QuickReceipt.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def carton_length(self):
        """Gets the carton_length of this QuickReceipt.  # noqa: E501


        :return: The carton_length of this QuickReceipt.  # noqa: E501
        :rtype: float
        """
        return self._carton_length

    @carton_length.setter
    def carton_length(self, carton_length):
        """Sets the carton_length of this QuickReceipt.


        :param carton_length: The carton_length of this QuickReceipt.  # noqa: E501
        :type: float
        """

        self._carton_length = carton_length

    @property
    def carton_width(self):
        """Gets the carton_width of this QuickReceipt.  # noqa: E501


        :return: The carton_width of this QuickReceipt.  # noqa: E501
        :rtype: float
        """
        return self._carton_width

    @carton_width.setter
    def carton_width(self, carton_width):
        """Sets the carton_width of this QuickReceipt.


        :param carton_width: The carton_width of this QuickReceipt.  # noqa: E501
        :type: float
        """

        self._carton_width = carton_width

    @property
    def carton_height(self):
        """Gets the carton_height of this QuickReceipt.  # noqa: E501


        :return: The carton_height of this QuickReceipt.  # noqa: E501
        :rtype: float
        """
        return self._carton_height

    @carton_height.setter
    def carton_height(self, carton_height):
        """Sets the carton_height of this QuickReceipt.


        :param carton_height: The carton_height of this QuickReceipt.  # noqa: E501
        :type: float
        """

        self._carton_height = carton_height

    @property
    def cost(self):
        """Gets the cost of this QuickReceipt.  # noqa: E501


        :return: The cost of this QuickReceipt.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this QuickReceipt.


        :param cost: The cost of this QuickReceipt.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def sell_price(self):
        """Gets the sell_price of this QuickReceipt.  # noqa: E501


        :return: The sell_price of this QuickReceipt.  # noqa: E501
        :rtype: float
        """
        return self._sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        """Sets the sell_price of this QuickReceipt.


        :param sell_price: The sell_price of this QuickReceipt.  # noqa: E501
        :type: float
        """

        self._sell_price = sell_price

    @property
    def pricing_per(self):
        """Gets the pricing_per of this QuickReceipt.  # noqa: E501


        :return: The pricing_per of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._pricing_per

    @pricing_per.setter
    def pricing_per(self, pricing_per):
        """Sets the pricing_per of this QuickReceipt.


        :param pricing_per: The pricing_per of this QuickReceipt.  # noqa: E501
        :type: str
        """

        self._pricing_per = pricing_per

    @property
    def generated_item_receipt_id(self):
        """Gets the generated_item_receipt_id of this QuickReceipt.  # noqa: E501


        :return: The generated_item_receipt_id of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._generated_item_receipt_id

    @generated_item_receipt_id.setter
    def generated_item_receipt_id(self, generated_item_receipt_id):
        """Sets the generated_item_receipt_id of this QuickReceipt.


        :param generated_item_receipt_id: The generated_item_receipt_id of this QuickReceipt.  # noqa: E501
        :type: int
        """

        self._generated_item_receipt_id = generated_item_receipt_id

    @property
    def generated_asn_id(self):
        """Gets the generated_asn_id of this QuickReceipt.  # noqa: E501


        :return: The generated_asn_id of this QuickReceipt.  # noqa: E501
        :rtype: int
        """
        return self._generated_asn_id

    @generated_asn_id.setter
    def generated_asn_id(self, generated_asn_id):
        """Sets the generated_asn_id of this QuickReceipt.


        :param generated_asn_id: The generated_asn_id of this QuickReceipt.  # noqa: E501
        :type: int
        """

        self._generated_asn_id = generated_asn_id

    @property
    def dock_date(self):
        """Gets the dock_date of this QuickReceipt.  # noqa: E501


        :return: The dock_date of this QuickReceipt.  # noqa: E501
        :rtype: datetime
        """
        return self._dock_date

    @dock_date.setter
    def dock_date(self, dock_date):
        """Sets the dock_date of this QuickReceipt.


        :param dock_date: The dock_date of this QuickReceipt.  # noqa: E501
        :type: datetime
        """

        self._dock_date = dock_date

    @property
    def product_id_tag(self):
        """Gets the product_id_tag of this QuickReceipt.  # noqa: E501


        :return: The product_id_tag of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._product_id_tag

    @product_id_tag.setter
    def product_id_tag(self, product_id_tag):
        """Sets the product_id_tag of this QuickReceipt.


        :param product_id_tag: The product_id_tag of this QuickReceipt.  # noqa: E501
        :type: str
        """

        self._product_id_tag = product_id_tag

    @property
    def custom_fields(self):
        """Gets the custom_fields of this QuickReceipt.  # noqa: E501


        :return: The custom_fields of this QuickReceipt.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this QuickReceipt.


        :param custom_fields: The custom_fields of this QuickReceipt.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def sku(self):
        """Gets the sku of this QuickReceipt.  # noqa: E501


        :return: The sku of this QuickReceipt.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this QuickReceipt.


        :param sku: The sku of this QuickReceipt.  # noqa: E501
        :type: str
        """

        self._sku = sku

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
        if not isinstance(other, QuickReceipt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
