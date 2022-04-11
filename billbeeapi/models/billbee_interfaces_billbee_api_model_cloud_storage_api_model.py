"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BillbeeInterfacesBillbeeAPIModelCloudStorageApiModel:

    """Implementation of the 'Billbee.Interfaces.BillbeeAPI.Model.CloudStorageApiModel' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        name (string): TODO: type description here.
        mtype (string): TODO: type description here.
        used_as_printer (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"id": "Id", "name": "Name", "mtype": "Type", "used_as_printer": "UsedAsPrinter"}

    def __init__(self, id=None, name=None, mtype=None, used_as_printer=None):
        """Constructor for the BillbeeInterfacesBillbeeAPIModelCloudStorageApiModel class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.mtype = mtype
        self.used_as_printer = used_as_printer

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
        mtype = dictionary.get("Type")
        used_as_printer = dictionary.get("UsedAsPrinter")

        # Return an object of this model
        return cls(id, name, mtype, used_as_printer)
