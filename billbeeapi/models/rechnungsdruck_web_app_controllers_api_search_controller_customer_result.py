"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RechnungsdruckWebAppControllersApiSearchControllerCustomerResult:

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.SearchController.CustomerResult' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        name (string): TODO: type description here.
        addresses (string): TODO: type description here.
        number (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"id": "Id", "name": "Name", "addresses": "Addresses", "number": "Number"}

    def __init__(self, id=None, name=None, addresses=None, number=None):
        """Constructor for the RechnungsdruckWebAppControllersApiSearchControllerCustomerResult class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.addresses = addresses
        self.number = number

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
        id = dictionary.get("Id")
        name = dictionary.get("Name")
        addresses = dictionary.get("Addresses")
        number = dictionary.get("Number")

        # Return an object of this model
        return cls(id, name, addresses, number)
