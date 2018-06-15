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
from Infoplus.api.carton_type_api import CartonTypeApi  # noqa: E501
from Infoplus.rest import ApiException


class TestCartonTypeApi(unittest.TestCase):
    """CartonTypeApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.carton_type_api.CartonTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_carton_type(self):
        """Test case for add_carton_type

        Create a cartonType  # noqa: E501
        """
        pass

    def test_add_carton_type_audit(self):
        """Test case for add_carton_type_audit

        Add new audit for a cartonType  # noqa: E501
        """
        pass

    def test_add_carton_type_tag(self):
        """Test case for add_carton_type_tag

        Add new tags for a cartonType.  # noqa: E501
        """
        pass

    def test_delete_carton_type(self):
        """Test case for delete_carton_type

        Delete a cartonType  # noqa: E501
        """
        pass

    def test_delete_carton_type_tag(self):
        """Test case for delete_carton_type_tag

        Delete a tag for a cartonType.  # noqa: E501
        """
        pass

    def test_get_carton_type_by_filter(self):
        """Test case for get_carton_type_by_filter

        Search cartonTypes by filter  # noqa: E501
        """
        pass

    def test_get_carton_type_by_id(self):
        """Test case for get_carton_type_by_id

        Get a cartonType by id  # noqa: E501
        """
        pass

    def test_get_carton_type_tags(self):
        """Test case for get_carton_type_tags

        Get the tags for a cartonType.  # noqa: E501
        """
        pass

    def test_get_duplicate_carton_type_by_id(self):
        """Test case for get_duplicate_carton_type_by_id

        Get a duplicated a cartonType by id  # noqa: E501
        """
        pass

    def test_update_carton_type(self):
        """Test case for update_carton_type

        Update a cartonType  # noqa: E501
        """
        pass

    def test_update_carton_type_custom_fields(self):
        """Test case for update_carton_type_custom_fields

        Update a cartonType custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
