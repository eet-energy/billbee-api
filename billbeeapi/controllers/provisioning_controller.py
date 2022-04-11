"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from billbeeapi.api_helper import APIHelper
from billbeeapi.controllers.base_controller import BaseController
from billbeeapi.http.auth.basic_auth import BasicAuth


class ProvisioningController(BaseController):

    """A Controller to access Endpoints in the billbeeapi API."""

    def __init__(self, config, call_back=None):
        super().__init__(config, call_back)

    def automatic_provisioning_create_account(self, model):
        """Does a POST request to /api/v1/automaticprovision/createaccount.

        Creates a new Billbee user account with the data passed

        Args:
            model
                (RechnungsdruckWebAppControllersApiAutomaticProvisioningControl
                lerCreateAccountContainer): TODO: type description here.

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = "/api/v1/automaticprovision/createaccount"
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {"content-type": "application/json; charset=utf-8"}

        # Prepare and execute request
        _request = self.config.http_client.post(
            _query_url, headers=_headers, parameters=APIHelper.json_serialize(model)
        )
        BasicAuth.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = _response.text

        return decoded

    def automatic_provisioning_terms_info(self):
        """Does a GET request to /api/v1/automaticprovision/termsinfo.

        Returns infos about Billbee terms and conditions

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = "/api/v1/automaticprovision/termsinfo"
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
