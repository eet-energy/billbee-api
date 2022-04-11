"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RechnungsdruckWebAppControllersApiOrderStateUpdate:

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.OrderStateUpdate' model.

    Specifies the parameters used to set the new state of an order

    Attributes:
        new_state_id (NewStateIdEnum): The new state to set

    """

    # Create a mapping from Model property names to API property names
    _names = {"new_state_id": "NewStateId"}

    def __init__(self, new_state_id=None):
        """Constructor for the RechnungsdruckWebAppControllersApiOrderStateUpdate class"""

        # Initialize members of the class
        self.new_state_id = new_state_id

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
        new_state_id = dictionary.get("NewStateId")

        # Return an object of this model
        return cls(new_state_id)
