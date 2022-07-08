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
from Infoplus.api.location_billing_type_api import LocationBillingTypeApi  # noqa: E501
from Infoplus.rest import ApiException


class TestLocationBillingTypeApi(unittest.TestCase):
    """LocationBillingTypeApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.location_billing_type_api.LocationBillingTypeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_location_billing_type(self):
        """Test case for add_location_billing_type

        Create a locationBillingType  # noqa: E501
        """
        pass

    def test_add_location_billing_type_audit(self):
        """Test case for add_location_billing_type_audit

        Add new audit for a locationBillingType  # noqa: E501
        """
        pass

    def test_add_location_billing_type_file(self):
        """Test case for add_location_billing_type_file

        Attach a file to a locationBillingType  # noqa: E501
        """
        pass

    def test_add_location_billing_type_file_by_url(self):
        """Test case for add_location_billing_type_file_by_url

        Attach a file to a locationBillingType by URL.  # noqa: E501
        """
        pass

    def test_add_location_billing_type_tag(self):
        """Test case for add_location_billing_type_tag

        Add new tags for a locationBillingType.  # noqa: E501
        """
        pass

    def test_delete_location_billing_type(self):
        """Test case for delete_location_billing_type

        Delete a locationBillingType  # noqa: E501
        """
        pass

    def test_delete_location_billing_type_file(self):
        """Test case for delete_location_billing_type_file

        Delete a file for a locationBillingType.  # noqa: E501
        """
        pass

    def test_delete_location_billing_type_tag(self):
        """Test case for delete_location_billing_type_tag

        Delete a tag for a locationBillingType.  # noqa: E501
        """
        pass

    def test_get_duplicate_location_billing_type_by_id(self):
        """Test case for get_duplicate_location_billing_type_by_id

        Get a duplicated a locationBillingType by id  # noqa: E501
        """
        pass

    def test_get_location_billing_type_by_filter(self):
        """Test case for get_location_billing_type_by_filter

        Search locationBillingTypes by filter  # noqa: E501
        """
        pass

    def test_get_location_billing_type_by_id(self):
        """Test case for get_location_billing_type_by_id

        Get a locationBillingType by id  # noqa: E501
        """
        pass

    def test_get_location_billing_type_files(self):
        """Test case for get_location_billing_type_files

        Get the files for a locationBillingType.  # noqa: E501
        """
        pass

    def test_get_location_billing_type_tags(self):
        """Test case for get_location_billing_type_tags

        Get the tags for a locationBillingType.  # noqa: E501
        """
        pass

    def test_update_location_billing_type(self):
        """Test case for update_location_billing_type

        Update a locationBillingType  # noqa: E501
        """
        pass

    def test_update_location_billing_type_custom_fields(self):
        """Test case for update_location_billing_type_custom_fields

        Update a locationBillingType custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
