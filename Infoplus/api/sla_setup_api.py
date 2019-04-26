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


class SlaSetupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_sla_setup_audit(self, sla_setup_id, sla_setup_audit, **kwargs):  # noqa: E501
        """Add new audit for a slaSetup  # noqa: E501

        Adds an audit to an existing slaSetup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_sla_setup_audit(sla_setup_id, sla_setup_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to add an audit to (required)
        :param str sla_setup_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_sla_setup_audit_with_http_info(sla_setup_id, sla_setup_audit, **kwargs)  # noqa: E501
        else:
            (data) = self.add_sla_setup_audit_with_http_info(sla_setup_id, sla_setup_audit, **kwargs)  # noqa: E501
            return data

    def add_sla_setup_audit_with_http_info(self, sla_setup_id, sla_setup_audit, **kwargs):  # noqa: E501
        """Add new audit for a slaSetup  # noqa: E501

        Adds an audit to an existing slaSetup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_sla_setup_audit_with_http_info(sla_setup_id, sla_setup_audit, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to add an audit to (required)
        :param str sla_setup_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sla_setup_id', 'sla_setup_audit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_sla_setup_audit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sla_setup_id' is set
        if ('sla_setup_id' not in params or
                params['sla_setup_id'] is None):
            raise ValueError("Missing the required parameter `sla_setup_id` when calling `add_sla_setup_audit`")  # noqa: E501
        # verify the required parameter 'sla_setup_audit' is set
        if ('sla_setup_audit' not in params or
                params['sla_setup_audit'] is None):
            raise ValueError("Missing the required parameter `sla_setup_audit` when calling `add_sla_setup_audit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sla_setup_id' in params:
            path_params['slaSetupId'] = params['sla_setup_id']  # noqa: E501
        if 'sla_setup_audit' in params:
            path_params['slaSetupAudit'] = params['sla_setup_audit']  # noqa: E501

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
            '/beta/slaSetup/{slaSetupId}/audit/{slaSetupAudit}', 'PUT',
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

    def add_sla_setup_file(self, sla_setup_id, file_name, **kwargs):  # noqa: E501
        """Attach a file to a slaSetup  # noqa: E501

        Adds a file to an existing slaSetup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_sla_setup_file(sla_setup_id, file_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to add a file to (required)
        :param str file_name: Name of file (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_sla_setup_file_with_http_info(sla_setup_id, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.add_sla_setup_file_with_http_info(sla_setup_id, file_name, **kwargs)  # noqa: E501
            return data

    def add_sla_setup_file_with_http_info(self, sla_setup_id, file_name, **kwargs):  # noqa: E501
        """Attach a file to a slaSetup  # noqa: E501

        Adds a file to an existing slaSetup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_sla_setup_file_with_http_info(sla_setup_id, file_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to add a file to (required)
        :param str file_name: Name of file (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sla_setup_id', 'file_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_sla_setup_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sla_setup_id' is set
        if ('sla_setup_id' not in params or
                params['sla_setup_id'] is None):
            raise ValueError("Missing the required parameter `sla_setup_id` when calling `add_sla_setup_file`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `add_sla_setup_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sla_setup_id' in params:
            path_params['slaSetupId'] = params['sla_setup_id']  # noqa: E501
        if 'file_name' in params:
            path_params['fileName'] = params['file_name']  # noqa: E501

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
            '/beta/slaSetup/{slaSetupId}/file/{fileName}', 'POST',
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

    def add_sla_setup_tag(self, sla_setup_id, sla_setup_tag, **kwargs):  # noqa: E501
        """Add new tags for a slaSetup.  # noqa: E501

        Adds a tag to an existing slaSetup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_sla_setup_tag(sla_setup_id, sla_setup_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to add a tag to (required)
        :param str sla_setup_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_sla_setup_tag_with_http_info(sla_setup_id, sla_setup_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.add_sla_setup_tag_with_http_info(sla_setup_id, sla_setup_tag, **kwargs)  # noqa: E501
            return data

    def add_sla_setup_tag_with_http_info(self, sla_setup_id, sla_setup_tag, **kwargs):  # noqa: E501
        """Add new tags for a slaSetup.  # noqa: E501

        Adds a tag to an existing slaSetup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_sla_setup_tag_with_http_info(sla_setup_id, sla_setup_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to add a tag to (required)
        :param str sla_setup_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sla_setup_id', 'sla_setup_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_sla_setup_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sla_setup_id' is set
        if ('sla_setup_id' not in params or
                params['sla_setup_id'] is None):
            raise ValueError("Missing the required parameter `sla_setup_id` when calling `add_sla_setup_tag`")  # noqa: E501
        # verify the required parameter 'sla_setup_tag' is set
        if ('sla_setup_tag' not in params or
                params['sla_setup_tag'] is None):
            raise ValueError("Missing the required parameter `sla_setup_tag` when calling `add_sla_setup_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sla_setup_id' in params:
            path_params['slaSetupId'] = params['sla_setup_id']  # noqa: E501
        if 'sla_setup_tag' in params:
            path_params['slaSetupTag'] = params['sla_setup_tag']  # noqa: E501

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
            '/beta/slaSetup/{slaSetupId}/tag/{slaSetupTag}', 'PUT',
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

    def delete_sla_setup_tag(self, sla_setup_id, sla_setup_tag, **kwargs):  # noqa: E501
        """Delete a tag for a slaSetup.  # noqa: E501

        Deletes an existing slaSetup tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_sla_setup_tag(sla_setup_id, sla_setup_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to remove tag from (required)
        :param str sla_setup_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_sla_setup_tag_with_http_info(sla_setup_id, sla_setup_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_sla_setup_tag_with_http_info(sla_setup_id, sla_setup_tag, **kwargs)  # noqa: E501
            return data

    def delete_sla_setup_tag_with_http_info(self, sla_setup_id, sla_setup_tag, **kwargs):  # noqa: E501
        """Delete a tag for a slaSetup.  # noqa: E501

        Deletes an existing slaSetup tag using the specified data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_sla_setup_tag_with_http_info(sla_setup_id, sla_setup_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to remove tag from (required)
        :param str sla_setup_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sla_setup_id', 'sla_setup_tag']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sla_setup_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sla_setup_id' is set
        if ('sla_setup_id' not in params or
                params['sla_setup_id'] is None):
            raise ValueError("Missing the required parameter `sla_setup_id` when calling `delete_sla_setup_tag`")  # noqa: E501
        # verify the required parameter 'sla_setup_tag' is set
        if ('sla_setup_tag' not in params or
                params['sla_setup_tag'] is None):
            raise ValueError("Missing the required parameter `sla_setup_tag` when calling `delete_sla_setup_tag`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sla_setup_id' in params:
            path_params['slaSetupId'] = params['sla_setup_id']  # noqa: E501
        if 'sla_setup_tag' in params:
            path_params['slaSetupTag'] = params['sla_setup_tag']  # noqa: E501

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
            '/beta/slaSetup/{slaSetupId}/tag/{slaSetupTag}', 'DELETE',
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

    def get_duplicate_sla_setup_by_id(self, sla_setup_id, **kwargs):  # noqa: E501
        """Get a duplicated a slaSetup by id  # noqa: E501

        Returns a duplicated slaSetup identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_sla_setup_by_id(sla_setup_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to be duplicated. (required)
        :return: SlaSetup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_duplicate_sla_setup_by_id_with_http_info(sla_setup_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_duplicate_sla_setup_by_id_with_http_info(sla_setup_id, **kwargs)  # noqa: E501
            return data

    def get_duplicate_sla_setup_by_id_with_http_info(self, sla_setup_id, **kwargs):  # noqa: E501
        """Get a duplicated a slaSetup by id  # noqa: E501

        Returns a duplicated slaSetup identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_duplicate_sla_setup_by_id_with_http_info(sla_setup_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to be duplicated. (required)
        :return: SlaSetup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sla_setup_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_sla_setup_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sla_setup_id' is set
        if ('sla_setup_id' not in params or
                params['sla_setup_id'] is None):
            raise ValueError("Missing the required parameter `sla_setup_id` when calling `get_duplicate_sla_setup_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sla_setup_id' in params:
            path_params['slaSetupId'] = params['sla_setup_id']  # noqa: E501

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
            '/beta/slaSetup/duplicate/{slaSetupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SlaSetup',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sla_setup_by_filter(self, **kwargs):  # noqa: E501
        """Search slaSetups by filter  # noqa: E501

        Returns the list of slaSetups that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sla_setup_by_filter(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[SlaSetup]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_sla_setup_by_filter_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sla_setup_by_filter_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sla_setup_by_filter_with_http_info(self, **kwargs):  # noqa: E501
        """Search slaSetups by filter  # noqa: E501

        Returns the list of slaSetups that match the given filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sla_setup_by_filter_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[SlaSetup]
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
                    " to method get_sla_setup_by_filter" % key
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
            '/beta/slaSetup/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SlaSetup]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sla_setup_by_id(self, sla_setup_id, **kwargs):  # noqa: E501
        """Get a slaSetup by id  # noqa: E501

        Returns the slaSetup identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sla_setup_by_id(sla_setup_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to be returned. (required)
        :return: SlaSetup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_sla_setup_by_id_with_http_info(sla_setup_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sla_setup_by_id_with_http_info(sla_setup_id, **kwargs)  # noqa: E501
            return data

    def get_sla_setup_by_id_with_http_info(self, sla_setup_id, **kwargs):  # noqa: E501
        """Get a slaSetup by id  # noqa: E501

        Returns the slaSetup identified by the specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sla_setup_by_id_with_http_info(sla_setup_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to be returned. (required)
        :return: SlaSetup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sla_setup_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sla_setup_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sla_setup_id' is set
        if ('sla_setup_id' not in params or
                params['sla_setup_id'] is None):
            raise ValueError("Missing the required parameter `sla_setup_id` when calling `get_sla_setup_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sla_setup_id' in params:
            path_params['slaSetupId'] = params['sla_setup_id']  # noqa: E501

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
            '/beta/slaSetup/{slaSetupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SlaSetup',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sla_setup_tags(self, sla_setup_id, **kwargs):  # noqa: E501
        """Get the tags for a slaSetup.  # noqa: E501

        Get all existing slaSetup tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sla_setup_tags(sla_setup_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_sla_setup_tags_with_http_info(sla_setup_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sla_setup_tags_with_http_info(sla_setup_id, **kwargs)  # noqa: E501
            return data

    def get_sla_setup_tags_with_http_info(self, sla_setup_id, **kwargs):  # noqa: E501
        """Get the tags for a slaSetup.  # noqa: E501

        Get all existing slaSetup tags.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sla_setup_tags_with_http_info(sla_setup_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sla_setup_id: Id of the slaSetup to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sla_setup_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sla_setup_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sla_setup_id' is set
        if ('sla_setup_id' not in params or
                params['sla_setup_id'] is None):
            raise ValueError("Missing the required parameter `sla_setup_id` when calling `get_sla_setup_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sla_setup_id' in params:
            path_params['slaSetupId'] = params['sla_setup_id']  # noqa: E501

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
            '/beta/slaSetup/{slaSetupId}/tag', 'GET',
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