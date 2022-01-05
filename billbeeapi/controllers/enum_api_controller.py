# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from billbeeapi.api_helper import APIHelper
from billbeeapi.configuration import Server
from billbeeapi.controllers.base_controller import BaseController
from billbeeapi.http.auth.basic_auth import BasicAuth


class EnumApiController(BaseController):

    """A Controller to access Endpoints in the billbeeapi API."""

    def __init__(self, config, call_back=None):
        super(EnumApiController, self).__init__(config, call_back)

    def enum_api_get_payment_types(self):
        """Does a GET request to /api/v1/enums/paymenttypes.

        Returns a list with all defined paymenttypes

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/v1/enums/paymenttypes'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = _response.text

        return decoded

    def enum_api_get_shipping_carriers(self):
        """Does a GET request to /api/v1/enums/shippingcarriers.

        Returns a list with all defined shippingcarriers

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/v1/enums/shippingcarriers'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = _response.text

        return decoded

    def enum_api_get_order_states(self):
        """Does a GET request to /api/v1/enums/orderstates.

        Returns a list with all defined orderstates

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/v1/enums/orderstates'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = _response.text

        return decoded
