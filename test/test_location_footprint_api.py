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
from Infoplus.api.location_footprint_api import LocationFootprintApi  # noqa: E501
from Infoplus.rest import ApiException


class TestLocationFootprintApi(unittest.TestCase):
    """LocationFootprintApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.location_footprint_api.LocationFootprintApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_location_footprint(self):
        """Test case for add_location_footprint

        Create a locationFootprint  # noqa: E501
        """
        pass

    def test_add_location_footprint_audit(self):
        """Test case for add_location_footprint_audit

        Add new audit for a locationFootprint  # noqa: E501
        """
        pass

    def test_add_location_footprint_tag(self):
        """Test case for add_location_footprint_tag

        Add new tags for a locationFootprint.  # noqa: E501
        """
        pass

    def test_delete_location_footprint(self):
        """Test case for delete_location_footprint

        Delete a locationFootprint  # noqa: E501
        """
        pass

    def test_delete_location_footprint_tag(self):
        """Test case for delete_location_footprint_tag

        Delete a tag for a locationFootprint.  # noqa: E501
        """
        pass

    def test_get_duplicate_location_footprint_by_id(self):
        """Test case for get_duplicate_location_footprint_by_id

        Get a duplicated a locationFootprint by id  # noqa: E501
        """
        pass

    def test_get_location_footprint_by_filter(self):
        """Test case for get_location_footprint_by_filter

        Search locationFootprints by filter  # noqa: E501
        """
        pass

    def test_get_location_footprint_by_id(self):
        """Test case for get_location_footprint_by_id

        Get a locationFootprint by id  # noqa: E501
        """
        pass

    def test_get_location_footprint_tags(self):
        """Test case for get_location_footprint_tags

        Get the tags for a locationFootprint.  # noqa: E501
        """
        pass

    def test_update_location_footprint(self):
        """Test case for update_location_footprint

        Update a locationFootprint  # noqa: E501
        """
        pass

    def test_update_location_footprint_custom_fields(self):
        """Test case for update_location_footprint_custom_fields

        Update a locationFootprint custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
