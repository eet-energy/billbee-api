"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from billbeeapi.models.billbee_interfaces_billbee_api_model_customer_api_model import (
    BillbeeInterfacesBillbeeAPIModelCustomerApiModel,
)
from billbeeapi.models.rechnungsdruck_web_app_controllers_api_api_paged_result_paging_information_system_collections_generic_list_billbee_interfaces_billbee_api_model_customer_api_model import (
    RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel,
)


class RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel:

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.ApiPagedResult[System.Collections.Generic.List[Billbee.Interfaces.BillbeeAPI.Model.CustomerApiModel]]' model.

    TODO: type model description here.

    Attributes:
        paging
            (RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationS
            ystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomer
            ApiModel): TODO: type description here.
        error_message (string): TODO: type description here.
        error_code (ErrorCodeEnum): TODO: type description here.
        data (list of BillbeeInterfacesBillbeeAPIModelCustomerApiModel): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"paging": "Paging", "error_message": "ErrorMessage", "error_code": "ErrorCode", "data": "Data"}

    def __init__(self, paging=None, error_message=None, error_code=None, data=None):
        """Constructor for the RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel class"""

        # Initialize members of the class
        self.paging = paging
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
        paging = (
            RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel.from_dictionary(
                dictionary.get("Paging")
            )
            if dictionary.get("Paging")
            else None
        )
        error_message = dictionary.get("ErrorMessage")
        error_code = dictionary.get("ErrorCode")
        data = None
        if dictionary.get("Data") is not None:
            data = [BillbeeInterfacesBillbeeAPIModelCustomerApiModel.from_dictionary(x) for x in dictionary.get("Data")]

        # Return an object of this model
        return cls(paging, error_message, error_code, data)
