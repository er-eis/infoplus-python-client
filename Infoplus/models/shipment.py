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


class Shipment(object):
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
        'ship_date': 'datetime',
        'delivered_date': 'datetime',
        'tracking_no': 'str',
        'warehouse_id': 'int',
        'lob_id': 'int',
        'order_no': 'float',
        'carton_no': 'int',
        'number_of_cartons': 'int',
        'status': 'str',
        'shipped': 'bool',
        'casebreak': 'bool',
        'carrier_service_id': 'int',
        'dim1_in': 'float',
        'dim2_in': 'float',
        'dim3_in': 'float',
        'estimated_zone': 'str',
        'parcel_account_no': 'str',
        'third_party_parcel_account_no': 'str',
        'shipment_id': 'str',
        'manifest_id': 'int',
        'residential': 'bool',
        'billing_option': 'str',
        'weight_lbs': 'float',
        'dim_weight': 'float',
        'license_plate_number': 'str',
        'charged_freight_amount': 'float',
        'published_freight_amount': 'float',
        'retail_freight_amount': 'float',
        'external_shipping_system_id': 'int',
        'shipment_type': 'str',
        'carrier_company': 'str',
        'carton_id': 'int',
        'carton_type_id': 'int',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'ship_date': 'shipDate',
        'delivered_date': 'deliveredDate',
        'tracking_no': 'trackingNo',
        'warehouse_id': 'warehouseId',
        'lob_id': 'lobId',
        'order_no': 'orderNo',
        'carton_no': 'cartonNo',
        'number_of_cartons': 'numberOfCartons',
        'status': 'status',
        'shipped': 'shipped',
        'casebreak': 'casebreak',
        'carrier_service_id': 'carrierServiceId',
        'dim1_in': 'dim1In',
        'dim2_in': 'dim2In',
        'dim3_in': 'dim3In',
        'estimated_zone': 'estimatedZone',
        'parcel_account_no': 'parcelAccountNo',
        'third_party_parcel_account_no': 'thirdPartyParcelAccountNo',
        'shipment_id': 'shipmentID',
        'manifest_id': 'manifestId',
        'residential': 'residential',
        'billing_option': 'billingOption',
        'weight_lbs': 'weightLbs',
        'dim_weight': 'dimWeight',
        'license_plate_number': 'licensePlateNumber',
        'charged_freight_amount': 'chargedFreightAmount',
        'published_freight_amount': 'publishedFreightAmount',
        'retail_freight_amount': 'retailFreightAmount',
        'external_shipping_system_id': 'externalShippingSystemId',
        'shipment_type': 'shipmentType',
        'carrier_company': 'carrierCompany',
        'carton_id': 'cartonId',
        'carton_type_id': 'cartonTypeId',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, ship_date=None, delivered_date=None, tracking_no=None, warehouse_id=None, lob_id=None, order_no=None, carton_no=None, number_of_cartons=None, status=None, shipped=False, casebreak=False, carrier_service_id=None, dim1_in=None, dim2_in=None, dim3_in=None, estimated_zone=None, parcel_account_no=None, third_party_parcel_account_no=None, shipment_id=None, manifest_id=None, residential=False, billing_option=None, weight_lbs=None, dim_weight=None, license_plate_number=None, charged_freight_amount=None, published_freight_amount=None, retail_freight_amount=None, external_shipping_system_id=None, shipment_type=None, carrier_company=None, carton_id=None, carton_type_id=None, custom_fields=None):  # noqa: E501
        """Shipment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._ship_date = None
        self._delivered_date = None
        self._tracking_no = None
        self._warehouse_id = None
        self._lob_id = None
        self._order_no = None
        self._carton_no = None
        self._number_of_cartons = None
        self._status = None
        self._shipped = None
        self._casebreak = None
        self._carrier_service_id = None
        self._dim1_in = None
        self._dim2_in = None
        self._dim3_in = None
        self._estimated_zone = None
        self._parcel_account_no = None
        self._third_party_parcel_account_no = None
        self._shipment_id = None
        self._manifest_id = None
        self._residential = None
        self._billing_option = None
        self._weight_lbs = None
        self._dim_weight = None
        self._license_plate_number = None
        self._charged_freight_amount = None
        self._published_freight_amount = None
        self._retail_freight_amount = None
        self._external_shipping_system_id = None
        self._shipment_type = None
        self._carrier_company = None
        self._carton_id = None
        self._carton_type_id = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if ship_date is not None:
            self.ship_date = ship_date
        if delivered_date is not None:
            self.delivered_date = delivered_date
        if tracking_no is not None:
            self.tracking_no = tracking_no
        self.warehouse_id = warehouse_id
        if lob_id is not None:
            self.lob_id = lob_id
        if order_no is not None:
            self.order_no = order_no
        if carton_no is not None:
            self.carton_no = carton_no
        if number_of_cartons is not None:
            self.number_of_cartons = number_of_cartons
        if status is not None:
            self.status = status
        if shipped is not None:
            self.shipped = shipped
        if casebreak is not None:
            self.casebreak = casebreak
        if carrier_service_id is not None:
            self.carrier_service_id = carrier_service_id
        if dim1_in is not None:
            self.dim1_in = dim1_in
        if dim2_in is not None:
            self.dim2_in = dim2_in
        if dim3_in is not None:
            self.dim3_in = dim3_in
        if estimated_zone is not None:
            self.estimated_zone = estimated_zone
        if parcel_account_no is not None:
            self.parcel_account_no = parcel_account_no
        if third_party_parcel_account_no is not None:
            self.third_party_parcel_account_no = third_party_parcel_account_no
        if shipment_id is not None:
            self.shipment_id = shipment_id
        if manifest_id is not None:
            self.manifest_id = manifest_id
        if residential is not None:
            self.residential = residential
        if billing_option is not None:
            self.billing_option = billing_option
        if weight_lbs is not None:
            self.weight_lbs = weight_lbs
        if dim_weight is not None:
            self.dim_weight = dim_weight
        if license_plate_number is not None:
            self.license_plate_number = license_plate_number
        if charged_freight_amount is not None:
            self.charged_freight_amount = charged_freight_amount
        if published_freight_amount is not None:
            self.published_freight_amount = published_freight_amount
        if retail_freight_amount is not None:
            self.retail_freight_amount = retail_freight_amount
        if external_shipping_system_id is not None:
            self.external_shipping_system_id = external_shipping_system_id
        if shipment_type is not None:
            self.shipment_type = shipment_type
        self.carrier_company = carrier_company
        if carton_id is not None:
            self.carton_id = carton_id
        if carton_type_id is not None:
            self.carton_type_id = carton_type_id
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Shipment.  # noqa: E501


        :return: The id of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Shipment.


        :param id: The id of this Shipment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this Shipment.  # noqa: E501


        :return: The create_date of this Shipment.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Shipment.


        :param create_date: The create_date of this Shipment.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this Shipment.  # noqa: E501


        :return: The modify_date of this Shipment.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this Shipment.


        :param modify_date: The modify_date of this Shipment.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def ship_date(self):
        """Gets the ship_date of this Shipment.  # noqa: E501


        :return: The ship_date of this Shipment.  # noqa: E501
        :rtype: datetime
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date):
        """Sets the ship_date of this Shipment.


        :param ship_date: The ship_date of this Shipment.  # noqa: E501
        :type: datetime
        """

        self._ship_date = ship_date

    @property
    def delivered_date(self):
        """Gets the delivered_date of this Shipment.  # noqa: E501


        :return: The delivered_date of this Shipment.  # noqa: E501
        :rtype: datetime
        """
        return self._delivered_date

    @delivered_date.setter
    def delivered_date(self, delivered_date):
        """Sets the delivered_date of this Shipment.


        :param delivered_date: The delivered_date of this Shipment.  # noqa: E501
        :type: datetime
        """

        self._delivered_date = delivered_date

    @property
    def tracking_no(self):
        """Gets the tracking_no of this Shipment.  # noqa: E501


        :return: The tracking_no of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, tracking_no):
        """Sets the tracking_no of this Shipment.


        :param tracking_no: The tracking_no of this Shipment.  # noqa: E501
        :type: str
        """

        self._tracking_no = tracking_no

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this Shipment.  # noqa: E501


        :return: The warehouse_id of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this Shipment.


        :param warehouse_id: The warehouse_id of this Shipment.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def lob_id(self):
        """Gets the lob_id of this Shipment.  # noqa: E501


        :return: The lob_id of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this Shipment.


        :param lob_id: The lob_id of this Shipment.  # noqa: E501
        :type: int
        """

        self._lob_id = lob_id

    @property
    def order_no(self):
        """Gets the order_no of this Shipment.  # noqa: E501


        :return: The order_no of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this Shipment.


        :param order_no: The order_no of this Shipment.  # noqa: E501
        :type: float
        """

        self._order_no = order_no

    @property
    def carton_no(self):
        """Gets the carton_no of this Shipment.  # noqa: E501


        :return: The carton_no of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._carton_no

    @carton_no.setter
    def carton_no(self, carton_no):
        """Sets the carton_no of this Shipment.


        :param carton_no: The carton_no of this Shipment.  # noqa: E501
        :type: int
        """

        self._carton_no = carton_no

    @property
    def number_of_cartons(self):
        """Gets the number_of_cartons of this Shipment.  # noqa: E501


        :return: The number_of_cartons of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._number_of_cartons

    @number_of_cartons.setter
    def number_of_cartons(self, number_of_cartons):
        """Sets the number_of_cartons of this Shipment.


        :param number_of_cartons: The number_of_cartons of this Shipment.  # noqa: E501
        :type: int
        """

        self._number_of_cartons = number_of_cartons

    @property
    def status(self):
        """Gets the status of this Shipment.  # noqa: E501


        :return: The status of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Shipment.


        :param status: The status of this Shipment.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def shipped(self):
        """Gets the shipped of this Shipment.  # noqa: E501


        :return: The shipped of this Shipment.  # noqa: E501
        :rtype: bool
        """
        return self._shipped

    @shipped.setter
    def shipped(self, shipped):
        """Sets the shipped of this Shipment.


        :param shipped: The shipped of this Shipment.  # noqa: E501
        :type: bool
        """

        self._shipped = shipped

    @property
    def casebreak(self):
        """Gets the casebreak of this Shipment.  # noqa: E501


        :return: The casebreak of this Shipment.  # noqa: E501
        :rtype: bool
        """
        return self._casebreak

    @casebreak.setter
    def casebreak(self, casebreak):
        """Sets the casebreak of this Shipment.


        :param casebreak: The casebreak of this Shipment.  # noqa: E501
        :type: bool
        """

        self._casebreak = casebreak

    @property
    def carrier_service_id(self):
        """Gets the carrier_service_id of this Shipment.  # noqa: E501


        :return: The carrier_service_id of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._carrier_service_id

    @carrier_service_id.setter
    def carrier_service_id(self, carrier_service_id):
        """Sets the carrier_service_id of this Shipment.


        :param carrier_service_id: The carrier_service_id of this Shipment.  # noqa: E501
        :type: int
        """

        self._carrier_service_id = carrier_service_id

    @property
    def dim1_in(self):
        """Gets the dim1_in of this Shipment.  # noqa: E501


        :return: The dim1_in of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._dim1_in

    @dim1_in.setter
    def dim1_in(self, dim1_in):
        """Sets the dim1_in of this Shipment.


        :param dim1_in: The dim1_in of this Shipment.  # noqa: E501
        :type: float
        """

        self._dim1_in = dim1_in

    @property
    def dim2_in(self):
        """Gets the dim2_in of this Shipment.  # noqa: E501


        :return: The dim2_in of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._dim2_in

    @dim2_in.setter
    def dim2_in(self, dim2_in):
        """Sets the dim2_in of this Shipment.


        :param dim2_in: The dim2_in of this Shipment.  # noqa: E501
        :type: float
        """

        self._dim2_in = dim2_in

    @property
    def dim3_in(self):
        """Gets the dim3_in of this Shipment.  # noqa: E501


        :return: The dim3_in of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._dim3_in

    @dim3_in.setter
    def dim3_in(self, dim3_in):
        """Sets the dim3_in of this Shipment.


        :param dim3_in: The dim3_in of this Shipment.  # noqa: E501
        :type: float
        """

        self._dim3_in = dim3_in

    @property
    def estimated_zone(self):
        """Gets the estimated_zone of this Shipment.  # noqa: E501


        :return: The estimated_zone of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._estimated_zone

    @estimated_zone.setter
    def estimated_zone(self, estimated_zone):
        """Sets the estimated_zone of this Shipment.


        :param estimated_zone: The estimated_zone of this Shipment.  # noqa: E501
        :type: str
        """

        self._estimated_zone = estimated_zone

    @property
    def parcel_account_no(self):
        """Gets the parcel_account_no of this Shipment.  # noqa: E501


        :return: The parcel_account_no of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._parcel_account_no

    @parcel_account_no.setter
    def parcel_account_no(self, parcel_account_no):
        """Sets the parcel_account_no of this Shipment.


        :param parcel_account_no: The parcel_account_no of this Shipment.  # noqa: E501
        :type: str
        """

        self._parcel_account_no = parcel_account_no

    @property
    def third_party_parcel_account_no(self):
        """Gets the third_party_parcel_account_no of this Shipment.  # noqa: E501


        :return: The third_party_parcel_account_no of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._third_party_parcel_account_no

    @third_party_parcel_account_no.setter
    def third_party_parcel_account_no(self, third_party_parcel_account_no):
        """Sets the third_party_parcel_account_no of this Shipment.


        :param third_party_parcel_account_no: The third_party_parcel_account_no of this Shipment.  # noqa: E501
        :type: str
        """

        self._third_party_parcel_account_no = third_party_parcel_account_no

    @property
    def shipment_id(self):
        """Gets the shipment_id of this Shipment.  # noqa: E501


        :return: The shipment_id of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._shipment_id

    @shipment_id.setter
    def shipment_id(self, shipment_id):
        """Sets the shipment_id of this Shipment.


        :param shipment_id: The shipment_id of this Shipment.  # noqa: E501
        :type: str
        """

        self._shipment_id = shipment_id

    @property
    def manifest_id(self):
        """Gets the manifest_id of this Shipment.  # noqa: E501


        :return: The manifest_id of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        """Sets the manifest_id of this Shipment.


        :param manifest_id: The manifest_id of this Shipment.  # noqa: E501
        :type: int
        """

        self._manifest_id = manifest_id

    @property
    def residential(self):
        """Gets the residential of this Shipment.  # noqa: E501


        :return: The residential of this Shipment.  # noqa: E501
        :rtype: bool
        """
        return self._residential

    @residential.setter
    def residential(self, residential):
        """Sets the residential of this Shipment.


        :param residential: The residential of this Shipment.  # noqa: E501
        :type: bool
        """

        self._residential = residential

    @property
    def billing_option(self):
        """Gets the billing_option of this Shipment.  # noqa: E501


        :return: The billing_option of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._billing_option

    @billing_option.setter
    def billing_option(self, billing_option):
        """Sets the billing_option of this Shipment.


        :param billing_option: The billing_option of this Shipment.  # noqa: E501
        :type: str
        """

        self._billing_option = billing_option

    @property
    def weight_lbs(self):
        """Gets the weight_lbs of this Shipment.  # noqa: E501


        :return: The weight_lbs of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._weight_lbs

    @weight_lbs.setter
    def weight_lbs(self, weight_lbs):
        """Sets the weight_lbs of this Shipment.


        :param weight_lbs: The weight_lbs of this Shipment.  # noqa: E501
        :type: float
        """

        self._weight_lbs = weight_lbs

    @property
    def dim_weight(self):
        """Gets the dim_weight of this Shipment.  # noqa: E501


        :return: The dim_weight of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._dim_weight

    @dim_weight.setter
    def dim_weight(self, dim_weight):
        """Sets the dim_weight of this Shipment.


        :param dim_weight: The dim_weight of this Shipment.  # noqa: E501
        :type: float
        """

        self._dim_weight = dim_weight

    @property
    def license_plate_number(self):
        """Gets the license_plate_number of this Shipment.  # noqa: E501


        :return: The license_plate_number of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, license_plate_number):
        """Sets the license_plate_number of this Shipment.


        :param license_plate_number: The license_plate_number of this Shipment.  # noqa: E501
        :type: str
        """

        self._license_plate_number = license_plate_number

    @property
    def charged_freight_amount(self):
        """Gets the charged_freight_amount of this Shipment.  # noqa: E501


        :return: The charged_freight_amount of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._charged_freight_amount

    @charged_freight_amount.setter
    def charged_freight_amount(self, charged_freight_amount):
        """Sets the charged_freight_amount of this Shipment.


        :param charged_freight_amount: The charged_freight_amount of this Shipment.  # noqa: E501
        :type: float
        """

        self._charged_freight_amount = charged_freight_amount

    @property
    def published_freight_amount(self):
        """Gets the published_freight_amount of this Shipment.  # noqa: E501


        :return: The published_freight_amount of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._published_freight_amount

    @published_freight_amount.setter
    def published_freight_amount(self, published_freight_amount):
        """Sets the published_freight_amount of this Shipment.


        :param published_freight_amount: The published_freight_amount of this Shipment.  # noqa: E501
        :type: float
        """

        self._published_freight_amount = published_freight_amount

    @property
    def retail_freight_amount(self):
        """Gets the retail_freight_amount of this Shipment.  # noqa: E501


        :return: The retail_freight_amount of this Shipment.  # noqa: E501
        :rtype: float
        """
        return self._retail_freight_amount

    @retail_freight_amount.setter
    def retail_freight_amount(self, retail_freight_amount):
        """Sets the retail_freight_amount of this Shipment.


        :param retail_freight_amount: The retail_freight_amount of this Shipment.  # noqa: E501
        :type: float
        """

        self._retail_freight_amount = retail_freight_amount

    @property
    def external_shipping_system_id(self):
        """Gets the external_shipping_system_id of this Shipment.  # noqa: E501


        :return: The external_shipping_system_id of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._external_shipping_system_id

    @external_shipping_system_id.setter
    def external_shipping_system_id(self, external_shipping_system_id):
        """Sets the external_shipping_system_id of this Shipment.


        :param external_shipping_system_id: The external_shipping_system_id of this Shipment.  # noqa: E501
        :type: int
        """

        self._external_shipping_system_id = external_shipping_system_id

    @property
    def shipment_type(self):
        """Gets the shipment_type of this Shipment.  # noqa: E501


        :return: The shipment_type of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._shipment_type

    @shipment_type.setter
    def shipment_type(self, shipment_type):
        """Sets the shipment_type of this Shipment.


        :param shipment_type: The shipment_type of this Shipment.  # noqa: E501
        :type: str
        """

        self._shipment_type = shipment_type

    @property
    def carrier_company(self):
        """Gets the carrier_company of this Shipment.  # noqa: E501


        :return: The carrier_company of this Shipment.  # noqa: E501
        :rtype: str
        """
        return self._carrier_company

    @carrier_company.setter
    def carrier_company(self, carrier_company):
        """Sets the carrier_company of this Shipment.


        :param carrier_company: The carrier_company of this Shipment.  # noqa: E501
        :type: str
        """
        if carrier_company is None:
            raise ValueError("Invalid value for `carrier_company`, must not be `None`")  # noqa: E501

        self._carrier_company = carrier_company

    @property
    def carton_id(self):
        """Gets the carton_id of this Shipment.  # noqa: E501


        :return: The carton_id of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._carton_id

    @carton_id.setter
    def carton_id(self, carton_id):
        """Sets the carton_id of this Shipment.


        :param carton_id: The carton_id of this Shipment.  # noqa: E501
        :type: int
        """

        self._carton_id = carton_id

    @property
    def carton_type_id(self):
        """Gets the carton_type_id of this Shipment.  # noqa: E501


        :return: The carton_type_id of this Shipment.  # noqa: E501
        :rtype: int
        """
        return self._carton_type_id

    @carton_type_id.setter
    def carton_type_id(self, carton_type_id):
        """Sets the carton_type_id of this Shipment.


        :param carton_type_id: The carton_type_id of this Shipment.  # noqa: E501
        :type: int
        """

        self._carton_type_id = carton_type_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Shipment.  # noqa: E501


        :return: The custom_fields of this Shipment.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Shipment.


        :param custom_fields: The custom_fields of this Shipment.  # noqa: E501
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
        if not isinstance(other, Shipment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
