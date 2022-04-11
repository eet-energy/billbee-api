# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData(object):

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.ApiResult[Billbee.Interfaces.BillbeeAPI.Model.UpdateStockCodeResponseData]' model.

    TODO: type model description here.

    Attributes:
        error_message (string): TODO: type description here.
        error_code (ErrorCodeEnum): TODO: type description here.
        data (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"error_message": "ErrorMessage", "error_code": "ErrorCode", "data": "Data"}

    def __init__(self, error_message=None, error_code=None, data=None):
        """Constructor for the RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData class"""

        # Initialize members of the class
        self.error_message = error_message
        self.error_code = error_code
        self.data = data

    @classmethod
    def from_dictionary(cls, dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        error_message = dictionary.get("ErrorMessage")
        error_code = dictionary.get("ErrorCode")
        data = dictionary.get("Data")

        # Return an object of this model
        return cls(error_message, error_code, data)
