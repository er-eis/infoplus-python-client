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
from Infoplus.api.invoice_worksheet_line_detail_api import InvoiceWorksheetLineDetailApi  # noqa: E501
from Infoplus.rest import ApiException


class TestInvoiceWorksheetLineDetailApi(unittest.TestCase):
    """InvoiceWorksheetLineDetailApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.invoice_worksheet_line_detail_api.InvoiceWorksheetLineDetailApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_invoice_worksheet_line_detail_audit(self):
        """Test case for add_invoice_worksheet_line_detail_audit

        Add new audit for an invoiceWorksheetLineDetail  # noqa: E501
        """
        pass

    def test_add_invoice_worksheet_line_detail_file(self):
        """Test case for add_invoice_worksheet_line_detail_file

        Attach a file to an invoiceWorksheetLineDetail  # noqa: E501
        """
        pass

    def test_add_invoice_worksheet_line_detail_file_by_url(self):
        """Test case for add_invoice_worksheet_line_detail_file_by_url

        Attach a file to an invoiceWorksheetLineDetail by URL.  # noqa: E501
        """
        pass

    def test_add_invoice_worksheet_line_detail_tag(self):
        """Test case for add_invoice_worksheet_line_detail_tag

        Add new tags for an invoiceWorksheetLineDetail.  # noqa: E501
        """
        pass

    def test_delete_invoice_worksheet_line_detail_file(self):
        """Test case for delete_invoice_worksheet_line_detail_file

        Delete a file for an invoiceWorksheetLineDetail.  # noqa: E501
        """
        pass

    def test_delete_invoice_worksheet_line_detail_tag(self):
        """Test case for delete_invoice_worksheet_line_detail_tag

        Delete a tag for an invoiceWorksheetLineDetail.  # noqa: E501
        """
        pass

    def test_get_duplicate_invoice_worksheet_line_detail_by_id(self):
        """Test case for get_duplicate_invoice_worksheet_line_detail_by_id

        Get a duplicated an invoiceWorksheetLineDetail by id  # noqa: E501
        """
        pass

    def test_get_invoice_worksheet_line_detail_by_filter(self):
        """Test case for get_invoice_worksheet_line_detail_by_filter

        Search invoiceWorksheetLineDetails by filter  # noqa: E501
        """
        pass

    def test_get_invoice_worksheet_line_detail_by_id(self):
        """Test case for get_invoice_worksheet_line_detail_by_id

        Get an invoiceWorksheetLineDetail by id  # noqa: E501
        """
        pass

    def test_get_invoice_worksheet_line_detail_files(self):
        """Test case for get_invoice_worksheet_line_detail_files

        Get the files for an invoiceWorksheetLineDetail.  # noqa: E501
        """
        pass

    def test_get_invoice_worksheet_line_detail_tags(self):
        """Test case for get_invoice_worksheet_line_detail_tags

        Get the tags for an invoiceWorksheetLineDetail.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
