# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import Infoplus
from Infoplus.api.order_api import OrderApi  # noqa: E501
from Infoplus.rest import ApiException


class TestOrderApi(unittest.TestCase):
    """OrderApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.order_api.OrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_order(self):
        """Test case for add_order

        Create an order  # noqa: E501
        """
        pass

    def test_add_order_audit(self):
        """Test case for add_order_audit

        Add new audit for an order  # noqa: E501
        """
        pass

    def test_add_order_tag(self):
        """Test case for add_order_tag

        Add new tags for an order.  # noqa: E501
        """
        pass

    def test_apply_order_warehouse_fulfillment_plan(self):
        """Test case for apply_order_warehouse_fulfillment_plan

        Run the Apply Order Warehouse Fulfillment Plan method.  # noqa: E501
        """
        pass

    def test_delete_order(self):
        """Test case for delete_order

        Delete an order  # noqa: E501
        """
        pass

    def test_delete_order_tag(self):
        """Test case for delete_order_tag

        Delete a tag for an order.  # noqa: E501
        """
        pass

    def test_get_duplicate_order_by_id(self):
        """Test case for get_duplicate_order_by_id

        Get a duplicated an order by id  # noqa: E501
        """
        pass

    def test_get_order_by_filter(self):
        """Test case for get_order_by_filter

        Search orders by filter  # noqa: E501
        """
        pass

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        Get an order by id  # noqa: E501
        """
        pass

    def test_get_order_tags(self):
        """Test case for get_order_tags

        Get the tags for an order.  # noqa: E501
        """
        pass

    def test_get_order_warehouse_fulfillment_data(self):
        """Test case for get_order_warehouse_fulfillment_data

        Run the Get Order Warehouse Fulfillment Plan method.  # noqa: E501
        """
        pass

    def test_update_order(self):
        """Test case for update_order

        Update an order  # noqa: E501
        """
        pass

    def test_update_order_custom_fields(self):
        """Test case for update_order_custom_fields

        Update an order custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
