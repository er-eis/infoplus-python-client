# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from Infoplus.api_client import ApiClient


class WorkBatchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_work_batch_audit(self, work_batch_id, work_batch_audit, **kwargs):  # noqa: E501
        """Add new audit for a workBatch  # noqa: E501

        Adds an audit to an existing workBatch.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_work_batch_audit(work_batch_id, work_batch_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to add an audit to (required)
        :param str work_batch_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_work_batch_audit_with_http_info(work_batch_id, work_batch_audit, **kwargs)  # noqa: E501
        else:
            (data) = self.add_work_batch_audit_with_http_info(work_batch_id, work_batch_audit, **kwargs)  # noqa: E501
            return data

    def add_work_batch_audit_with_http_info(self, work_batch_id, work_batch_audit, **kwargs):  # noqa: E501
        """Add new audit for a workBatch  # noqa: E501

        Adds an audit to an existing workBatch.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_work_batch_audit_with_http_info(work_batch_id, work_batch_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to add an audit to (required)
        :param str work_batch_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['work_batch_id', 'work_batch_audit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_work_batch_audit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'work_batch_id' is set
        if ('work_batch_id' not in params or
                params['work_batch_id'] is None):
            raise ValueError("Missing the required parameter `work_batch_id` when calling `add_work_batch_audit`")  # noqa: E501
        # verify the required parameter 'work_batch_audit' is set
        if ('work_batch_audit' not in params or
                params['work_batch_audit'] is None):
            raise ValueError("Missing the required parameter `work_batch_audit` when calling `add_work_batch_audit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'work_batch_id' in params:
            path_params['workBatchId'] = params['work_batch_id']  # noqa: E501
        if 'work_batch_audit' in params:
            path_params['workBatchAudit'] = params['work_batch_audit']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/workBatch/{workBatchId}/audit/{workBatchAudit}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_work_batch_tag(self, work_batch_id, work_batch_tag, **kwargs):  # noqa: E501
        """Add new tags for a workBatch.  # noqa: E501

        Adds a tag to an existing workBatch.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_work_batch_tag(work_batch_id, work_batch_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to add a tag to (required)
        :param str work_batch_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_work_batch_tag_with_http_info(work_batch_id, work_batch_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.add_work_batch_tag_with_http_info(work_batch_id, work_batch_tag, **kwargs)  # noqa: E501
            return data

    def add_work_batch_tag_with_http_info(self, work_batch_id, work_batch_tag, **kwargs):  # noqa: E501
        """Add new tags for a workBatch.  # noqa: E501

        Adds a tag to an existing workBatch.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_work_batch_tag_with_http_info(work_batch_id, work_batch_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to add a tag to (required)
        :param str work_batch_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['work_batch_id', 'work_batch_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_work_batch_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'work_batch_id' is set
        if ('work_batch_id' not in params or
                params['work_batch_id'] is None):
            raise ValueError("Missing the required parameter `work_batch_id` when calling `add_work_batch_tag`")  # noqa: E501
        # verify the required parameter 'work_batch_tag' is set
        if ('work_batch_tag' not in params or
                params['work_batch_tag'] is None):
            raise ValueError("Missing the required parameter `work_batch_tag` when calling `add_work_batch_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'work_batch_id' in params:
            path_params['workBatchId'] = params['work_batch_id']  # noqa: E501
        if 'work_batch_tag' in params:
            path_params['workBatchTag'] = params['work_batch_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/workBatch/{workBatchId}/tag/{workBatchTag}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_work_batch_tag(self, work_batch_id, work_batch_tag, **kwargs):  # noqa: E501
        """Delete a tag for a workBatch.  # noqa: E501

        Deletes an existing workBatch tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_work_batch_tag(work_batch_id, work_batch_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to remove tag from (required)
        :param str work_batch_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_work_batch_tag_with_http_info(work_batch_id, work_batch_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_work_batch_tag_with_http_info(work_batch_id, work_batch_tag, **kwargs)  # noqa: E501
            return data

    def delete_work_batch_tag_with_http_info(self, work_batch_id, work_batch_tag, **kwargs):  # noqa: E501
        """Delete a tag for a workBatch.  # noqa: E501

        Deletes an existing workBatch tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_work_batch_tag_with_http_info(work_batch_id, work_batch_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to remove tag from (required)
        :param str work_batch_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['work_batch_id', 'work_batch_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_work_batch_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'work_batch_id' is set
        if ('work_batch_id' not in params or
                params['work_batch_id'] is None):
            raise ValueError("Missing the required parameter `work_batch_id` when calling `delete_work_batch_tag`")  # noqa: E501
        # verify the required parameter 'work_batch_tag' is set
        if ('work_batch_tag' not in params or
                params['work_batch_tag'] is None):
            raise ValueError("Missing the required parameter `work_batch_tag` when calling `delete_work_batch_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'work_batch_id' in params:
            path_params['workBatchId'] = params['work_batch_id']  # noqa: E501
        if 'work_batch_tag' in params:
            path_params['workBatchTag'] = params['work_batch_tag']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/workBatch/{workBatchId}/tag/{workBatchTag}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_duplicate_work_batch_by_id(self, work_batch_id, **kwargs):  # noqa: E501
        """Get a duplicated a workBatch by id  # noqa: E501

        Returns a duplicated workBatch identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_work_batch_by_id(work_batch_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to be duplicated. (required)
        :return: WorkBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_duplicate_work_batch_by_id_with_http_info(work_batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_duplicate_work_batch_by_id_with_http_info(work_batch_id, **kwargs)  # noqa: E501
            return data

    def get_duplicate_work_batch_by_id_with_http_info(self, work_batch_id, **kwargs):  # noqa: E501
        """Get a duplicated a workBatch by id  # noqa: E501

        Returns a duplicated workBatch identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_work_batch_by_id_with_http_info(work_batch_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to be duplicated. (required)
        :return: WorkBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['work_batch_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_work_batch_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'work_batch_id' is set
        if ('work_batch_id' not in params or
                params['work_batch_id'] is None):
            raise ValueError("Missing the required parameter `work_batch_id` when calling `get_duplicate_work_batch_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'work_batch_id' in params:
            path_params['workBatchId'] = params['work_batch_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/workBatch/duplicate/{workBatchId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkBatch',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_work_batch_by_filter(self, **kwargs):  # noqa: E501
        """Search workBatchs by filter  # noqa: E501

        Returns the list of workBatchs that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_work_batch_by_filter(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[WorkBatch]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_work_batch_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_work_batch_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_work_batch_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Search workBatchs by filter  # noqa: E501

        Returns the list of workBatchs that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_work_batch_by_filter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[WorkBatch]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'page', 'limit', 'sort']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_work_batch_by_filter" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/workBatch/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[WorkBatch]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_work_batch_by_id(self, work_batch_id, **kwargs):  # noqa: E501
        """Get a workBatch by id  # noqa: E501

        Returns the workBatch identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_work_batch_by_id(work_batch_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to be returned. (required)
        :return: WorkBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_work_batch_by_id_with_http_info(work_batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_work_batch_by_id_with_http_info(work_batch_id, **kwargs)  # noqa: E501
            return data

    def get_work_batch_by_id_with_http_info(self, work_batch_id, **kwargs):  # noqa: E501
        """Get a workBatch by id  # noqa: E501

        Returns the workBatch identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_work_batch_by_id_with_http_info(work_batch_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to be returned. (required)
        :return: WorkBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['work_batch_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_work_batch_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'work_batch_id' is set
        if ('work_batch_id' not in params or
                params['work_batch_id'] is None):
            raise ValueError("Missing the required parameter `work_batch_id` when calling `get_work_batch_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'work_batch_id' in params:
            path_params['workBatchId'] = params['work_batch_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/workBatch/{workBatchId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkBatch',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_work_batch_tags(self, work_batch_id, **kwargs):  # noqa: E501
        """Get the tags for a workBatch.  # noqa: E501

        Get all existing workBatch tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_work_batch_tags(work_batch_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_work_batch_tags_with_http_info(work_batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_work_batch_tags_with_http_info(work_batch_id, **kwargs)  # noqa: E501
            return data

    def get_work_batch_tags_with_http_info(self, work_batch_id, **kwargs):  # noqa: E501
        """Get the tags for a workBatch.  # noqa: E501

        Get all existing workBatch tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_work_batch_tags_with_http_info(work_batch_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int work_batch_id: Id of the workBatch to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['work_batch_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_work_batch_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'work_batch_id' is set
        if ('work_batch_id' not in params or
                params['work_batch_id'] is None):
            raise ValueError("Missing the required parameter `work_batch_id` when calling `get_work_batch_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'work_batch_id' in params:
            path_params['workBatchId'] = params['work_batch_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/workBatch/{workBatchId}/tag', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_work_batch_custom_fields(self, body, **kwargs):  # noqa: E501
        """Update a workBatch custom fields  # noqa: E501

        Updates an existing workBatch custom fields using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_work_batch_custom_fields(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param WorkBatch body: WorkBatch to be updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_work_batch_custom_fields_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_work_batch_custom_fields_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_work_batch_custom_fields_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update a workBatch custom fields  # noqa: E501

        Updates an existing workBatch custom fields using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_work_batch_custom_fields_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param WorkBatch body: WorkBatch to be updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_work_batch_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_work_batch_custom_fields`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/beta/workBatch/customFields', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
