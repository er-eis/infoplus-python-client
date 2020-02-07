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
from Infoplus.api.work_batch_api import WorkBatchApi  # noqa: E501
from Infoplus.rest import ApiException


class TestWorkBatchApi(unittest.TestCase):
    """WorkBatchApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.work_batch_api.WorkBatchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_work_batch_audit(self):
        """Test case for add_work_batch_audit

        Add new audit for a workBatch  # noqa: E501
        """
        pass

    def test_add_work_batch_file(self):
        """Test case for add_work_batch_file

        Attach a file to a workBatch  # noqa: E501
        """
        pass

    def test_add_work_batch_file_by_url(self):
        """Test case for add_work_batch_file_by_url

        Attach a file to a workBatch by URL.  # noqa: E501
        """
        pass

    def test_add_work_batch_tag(self):
        """Test case for add_work_batch_tag

        Add new tags for a workBatch.  # noqa: E501
        """
        pass

    def test_delete_work_batch_file(self):
        """Test case for delete_work_batch_file

        Delete a file for a workBatch.  # noqa: E501
        """
        pass

    def test_delete_work_batch_tag(self):
        """Test case for delete_work_batch_tag

        Delete a tag for a workBatch.  # noqa: E501
        """
        pass

    def test_get_duplicate_work_batch_by_id(self):
        """Test case for get_duplicate_work_batch_by_id

        Get a duplicated a workBatch by id  # noqa: E501
        """
        pass

    def test_get_work_batch_by_filter(self):
        """Test case for get_work_batch_by_filter

        Search workBatchs by filter  # noqa: E501
        """
        pass

    def test_get_work_batch_by_id(self):
        """Test case for get_work_batch_by_id

        Get a workBatch by id  # noqa: E501
        """
        pass

    def test_get_work_batch_files(self):
        """Test case for get_work_batch_files

        Get the files for a workBatch.  # noqa: E501
        """
        pass

    def test_get_work_batch_tags(self):
        """Test case for get_work_batch_tags

        Get the tags for a workBatch.  # noqa: E501
        """
        pass

    def test_update_work_batch(self):
        """Test case for update_work_batch

        Update a workBatch  # noqa: E501
        """
        pass

    def test_update_work_batch_custom_fields(self):
        """Test case for update_work_batch_custom_fields

        Update a workBatch custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
