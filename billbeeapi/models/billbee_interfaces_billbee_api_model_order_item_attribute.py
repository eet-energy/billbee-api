"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BillbeeInterfacesBillbeeAPIModelOrderItemAttribute:

    """Implementation of the 'Billbee.Interfaces.BillbeeAPI.Model.OrderItemAttribute' model.

    TODO: type model description here.

    Attributes:
        id (string): The internal id of this attribute
        name (string): The attribute name. E.g. color
        value (string): The attribute value. E.g. red
        price (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"id": "Id", "name": "Name", "value": "Value", "price": "Price"}

    def __init__(self, id=None, name=None, value=None, price=None):
        """Constructor for the BillbeeInterfacesBillbeeAPIModelOrderItemAttribute class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.value = value
        self.price = price

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
        value = dictionary.get("Value")
        price = dictionary.get("Price")

        # Return an object of this model
        return cls(id, name, value, price)
