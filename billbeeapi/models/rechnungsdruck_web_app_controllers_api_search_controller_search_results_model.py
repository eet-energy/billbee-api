"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from billbeeapi.models.rechnungsdruck_web_app_controllers_api_search_controller_customer_result import (
    RechnungsdruckWebAppControllersApiSearchControllerCustomerResult,
)
from billbeeapi.models.rechnungsdruck_web_app_controllers_api_search_controller_order_result import (
    RechnungsdruckWebAppControllersApiSearchControllerOrderResult,
)
from billbeeapi.models.rechnungsdruck_web_app_controllers_api_search_controller_product_result import (
    RechnungsdruckWebAppControllersApiSearchControllerProductResult,
)


class RechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel:

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.SearchController.SearchResultsModel' model.

    TODO: type model description here.

    Attributes:
        products (list of
            RechnungsdruckWebAppControllersApiSearchControllerProductResult):
            TODO: type description here.
        orders (list of
            RechnungsdruckWebAppControllersApiSearchControllerOrderResult):
            TODO: type description here.
        customers (list of
            RechnungsdruckWebAppControllersApiSearchControllerCustomerResult):
            TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"products": "Products", "orders": "Orders", "customers": "Customers"}

    def __init__(self, products=None, orders=None, customers=None):
        """Constructor for the RechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel class"""

        # Initialize members of the class
        self.products = products
        self.orders = orders
        self.customers = customers

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
        products = None
        if dictionary.get("Products") is not None:
            products = [
                RechnungsdruckWebAppControllersApiSearchControllerProductResult.from_dictionary(x)
                for x in dictionary.get("Products")
            ]
        orders = None
        if dictionary.get("Orders") is not None:
            orders = [
                RechnungsdruckWebAppControllersApiSearchControllerOrderResult.from_dictionary(x)
                for x in dictionary.get("Orders")
            ]
        customers = None
        if dictionary.get("Customers") is not None:
            customers = [
                RechnungsdruckWebAppControllersApiSearchControllerCustomerResult.from_dictionary(x)
                for x in dictionary.get("Customers")
            ]

        # Return an object of this model
        return cls(products, orders, customers)
