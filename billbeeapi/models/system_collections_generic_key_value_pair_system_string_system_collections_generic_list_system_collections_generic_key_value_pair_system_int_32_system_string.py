# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from billbeeapi.models.system_collections_generic_key_value_pair_system_int_32_system_string import SystemCollectionsGenericKeyValuePairSystemInt32SystemString


class SystemCollectionsGenericKeyValuePairSystemStringSystemCollectionsGenericListSystemCollectionsGenericKeyValuePairSystemInt32SystemString(object):

    """Implementation of the 'System.Collections.Generic.KeyValuePair[System.String,System.Collections.Generic.List[System.Collections.Generic.KeyValuePair[System.Int32,System.String]]]' model.

    TODO: type model description here.

    Attributes:
        key (string): TODO: type description here.
        value (list of
            SystemCollectionsGenericKeyValuePairSystemInt32SystemString):
            TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'key',
        "value": 'value'
    }

    def __init__(self,
                 key=None,
                 value=None):
        """Constructor for the SystemCollectionsGenericKeyValuePairSystemStringSystemCollectionsGenericListSystemCollectionsGenericKeyValuePairSystemInt32SystemString class"""

        # Initialize members of the class
        self.key = key
        self.value = value

    @classmethod
    def from_dictionary(cls,
                        dictionary):
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
        key = dictionary.get('key')
        value = None
        if dictionary.get('value') is not None:
            value = [SystemCollectionsGenericKeyValuePairSystemInt32SystemString.from_dictionary(x) for x in dictionary.get('value')]

        # Return an object of this model
        return cls(key,
                   value)
