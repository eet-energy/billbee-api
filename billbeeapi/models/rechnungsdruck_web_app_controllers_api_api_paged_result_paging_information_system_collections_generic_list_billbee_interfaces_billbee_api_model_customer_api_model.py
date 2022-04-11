# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel(
    object
):

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.ApiPagedResult.PagingInformation[System.Collections.Generic.List[Billbee.Interfaces.BillbeeAPI.Model.CustomerApiModel]]' model.

    TODO: type model description here.

    Attributes:
        page (int): TODO: type description here.
        total_pages (int): TODO: type description here.
        total_rows (int): TODO: type description here.
        page_size (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"page": "Page", "total_pages": "TotalPages", "total_rows": "TotalRows", "page_size": "PageSize"}

    def __init__(self, page=None, total_pages=None, total_rows=None, page_size=None):
        """Constructor for the RechnungsdruckWebAppControllersApiApiPagedResultPagingInformationSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel class"""

        # Initialize members of the class
        self.page = page
        self.total_pages = total_pages
        self.total_rows = total_rows
        self.page_size = page_size

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
        page = dictionary.get("Page")
        total_pages = dictionary.get("TotalPages")
        total_rows = dictionary.get("TotalRows")
        page_size = dictionary.get("PageSize")

        # Return an object of this model
        return cls(page, total_pages, total_rows, page_size)
