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
from Infoplus.api.parcel_invoice_api import ParcelInvoiceApi  # noqa: E501
from Infoplus.rest import ApiException


class TestParcelInvoiceApi(unittest.TestCase):
    """ParcelInvoiceApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.parcel_invoice_api.ParcelInvoiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_parcel_invoice_audit(self):
        """Test case for add_parcel_invoice_audit

        Add new audit for a parcelInvoice  # noqa: E501
        """
        pass

    def test_add_parcel_invoice_tag(self):
        """Test case for add_parcel_invoice_tag

        Add new tags for a parcelInvoice.  # noqa: E501
        """
        pass

    def test_delete_parcel_invoice(self):
        """Test case for delete_parcel_invoice

        Delete a parcelInvoice  # noqa: E501
        """
        pass

    def test_delete_parcel_invoice_tag(self):
        """Test case for delete_parcel_invoice_tag

        Delete a tag for a parcelInvoice.  # noqa: E501
        """
        pass

    def test_get_duplicate_parcel_invoice_by_id(self):
        """Test case for get_duplicate_parcel_invoice_by_id

        Get a duplicated a parcelInvoice by id  # noqa: E501
        """
        pass

    def test_get_parcel_invoice_by_filter(self):
        """Test case for get_parcel_invoice_by_filter

        Search parcelInvoices by filter  # noqa: E501
        """
        pass

    def test_get_parcel_invoice_by_id(self):
        """Test case for get_parcel_invoice_by_id

        Get a parcelInvoice by id  # noqa: E501
        """
        pass

    def test_get_parcel_invoice_tags(self):
        """Test case for get_parcel_invoice_tags

        Get the tags for a parcelInvoice.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()