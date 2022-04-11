# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BillbeeInterfacesOrderMultiLanguageString(object):

    """Implementation of the 'Billbee.Interfaces.Order.MultiLanguageString' model.

    TODO: type model description here.

    Attributes:
        text (string): TODO: type description here.
        language_code (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"text": "Text", "language_code": "LanguageCode"}

    def __init__(self, text=None, language_code=None):
        """Constructor for the BillbeeInterfacesOrderMultiLanguageString class"""

        # Initialize members of the class
        self.text = text
        self.language_code = language_code

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
        text = dictionary.get("Text")
        language_code = dictionary.get("LanguageCode")

        # Return an object of this model
        return cls(text, language_code)
