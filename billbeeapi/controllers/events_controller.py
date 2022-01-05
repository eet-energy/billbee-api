# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from billbeeapi.api_helper import APIHelper
from billbeeapi.configuration import Server
from billbeeapi.controllers.base_controller import BaseController
from billbeeapi.http.auth.basic_auth import BasicAuth


class EventsController(BaseController):

    """A Controller to access Endpoints in the billbeeapi API."""

    def __init__(self, config, call_back=None):
        super(EventsController, self).__init__(config, call_back)

    def event_api_get_list(self,
                           min_date=None,
                           max_date=None,
                           page=None,
                           page_size=None,
                           type_id=None,
                           order_id=None):
        """Does a GET request to /api/v1/events.

        Get a list of all events optionally filtered by date. This request is
        extra throttled to 2 calls per page per hour.

        Args:
            min_date (datetime, optional): Specifies the oldest date to
                include in the response
            max_date (datetime, optional): Specifies the newest date to
                include in the response
            page (int, optional): Specifies the page to request
            page_size (int, optional): Specifies the pagesize. Defaults to 50,
                max value is 250
            type_id (list of int, optional): Filter for specific event types
            order_id (int, optional): Filter for specific order id

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/api/v1/events'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'minDate': APIHelper.when_defined(APIHelper.RFC3339DateTime, min_date),
            'maxDate': APIHelper.when_defined(APIHelper.RFC3339DateTime, max_date),
            'page': page,
            'pageSize': page_size,
            'typeId': type_id,
            'orderId': order_id
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url)
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = _response.text

        return decoded
