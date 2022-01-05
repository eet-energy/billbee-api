# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from billbeeapi.models.system_collections_generic_key_value_pair_system_string_system_collections_generic_list_system_collections_generic_key_value_pair_system_int_32_system_string import SystemCollectionsGenericKeyValuePairSystemStringSystemCollectionsGenericListSystemCollectionsGenericKeyValuePairSystemInt32SystemString


class BillbeeInterfacesShippingProductService(object):

    """Implementation of the 'Billbee.Interfaces.Shipping.ProductService' model.

    TODO: type model description here.

    Attributes:
        display_name (string): TODO: type description here.
        display_value (string): TODO: type description here.
        requires_user_input (bool): TODO: type description here.
        service_name (string): TODO: type description here.
        type_name (string): TODO: type description here.
        possible_value_lists (list of
            SystemCollectionsGenericKeyValuePairSystemStringSystemCollectionsGe
            nericListSystemCollectionsGenericKeyValuePairSystemInt32SystemStrin
            g): TODO: type description here.
        can_be_configured (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "display_name": 'DisplayName',
        "display_value": 'DisplayValue',
        "requires_user_input": 'RequiresUserInput',
        "service_name": 'ServiceName',
        "type_name": 'typeName',
        "possible_value_lists": 'PossibleValueLists',
        "can_be_configured": 'CanBeConfigured'
    }

    def __init__(self,
                 display_name=None,
                 display_value=None,
                 requires_user_input=None,
                 service_name=None,
                 type_name=None,
                 possible_value_lists=None,
                 can_be_configured=None):
        """Constructor for the BillbeeInterfacesShippingProductService class"""

        # Initialize members of the class
        self.display_name = display_name
        self.display_value = display_value
        self.requires_user_input = requires_user_input
        self.service_name = service_name
        self.type_name = type_name
        self.possible_value_lists = possible_value_lists
        self.can_be_configured = can_be_configured

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
        display_name = dictionary.get('DisplayName')
        display_value = dictionary.get('DisplayValue')
        requires_user_input = dictionary.get('RequiresUserInput')
        service_name = dictionary.get('ServiceName')
        type_name = dictionary.get('typeName')
        possible_value_lists = None
        if dictionary.get('PossibleValueLists') is not None:
            possible_value_lists = [SystemCollectionsGenericKeyValuePairSystemStringSystemCollectionsGenericListSystemCollectionsGenericKeyValuePairSystemInt32SystemString.from_dictionary(x) for x in dictionary.get('PossibleValueLists')]
        can_be_configured = dictionary.get('CanBeConfigured')

        # Return an object of this model
        return cls(display_name,
                   display_value,
                   requires_user_input,
                   service_name,
                   type_name,
                   possible_value_lists,
                   can_be_configured)
