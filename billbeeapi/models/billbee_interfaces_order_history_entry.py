"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from billbeeapi.api_helper import APIHelper


class BillbeeInterfacesOrderHistoryEntry:

    """Implementation of the 'Billbee.Interfaces.Order.HistoryEntry' model.

    TODO: type model description here.

    Attributes:
        created (datetime): TODO: type description here.
        event_type_name (string): TODO: type description here.
        text (string): TODO: type description here.
        employee_name (string): TODO: type description here.
        type_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created": "Created",
        "event_type_name": "EventTypeName",
        "text": "Text",
        "employee_name": "EmployeeName",
        "type_id": "TypeId",
    }

    def __init__(self, created=None, event_type_name=None, text=None, employee_name=None, type_id=None):
        """Constructor for the BillbeeInterfacesOrderHistoryEntry class"""

        # Initialize members of the class
        self.created = APIHelper.RFC3339DateTime(created) if created else None
        self.event_type_name = event_type_name
        self.text = text
        self.employee_name = employee_name
        self.type_id = type_id

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
        created = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("Created")).datetime
            if dictionary.get("Created")
            else None
        )
        event_type_name = dictionary.get("EventTypeName")
        text = dictionary.get("Text")
        employee_name = dictionary.get("EmployeeName")
        type_id = dictionary.get("TypeId")

        # Return an object of this model
        return cls(created, event_type_name, text, employee_name, type_id)
