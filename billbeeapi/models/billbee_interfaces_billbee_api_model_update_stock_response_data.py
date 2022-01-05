# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BillbeeInterfacesBillbeeAPIModelUpdateStockResponseData(object):

    """Implementation of the 'Billbee.Interfaces.BillbeeAPI.Model.UpdateStockResponseData' model.

    TODO: type model description here.

    Attributes:
        sku (string): The SKU of the article to update the current stock
        current_stock (float): The new value for current stock after the
            update
        unfulfilled_amount (float): The value of the unfulfilled amount
            (reserved) of the article
        message (string): A human readable message that explains the result of
            the operation

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sku": 'SKU',
        "current_stock": 'CurrentStock',
        "unfulfilled_amount": 'UnfulfilledAmount',
        "message": 'Message'
    }

    def __init__(self,
                 sku=None,
                 current_stock=None,
                 unfulfilled_amount=None,
                 message=None):
        """Constructor for the BillbeeInterfacesBillbeeAPIModelUpdateStockResponseData class"""

        # Initialize members of the class
        self.sku = sku
        self.current_stock = current_stock
        self.unfulfilled_amount = unfulfilled_amount
        self.message = message

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
        sku = dictionary.get('SKU')
        current_stock = dictionary.get('CurrentStock')
        unfulfilled_amount = dictionary.get('UnfulfilledAmount')
        message = dictionary.get('Message')

        # Return an object of this model
        return cls(sku,
                   current_stock,
                   unfulfilled_amount,
                   message)
