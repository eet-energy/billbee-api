# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from billbeeapi.models.billbee_interfaces_billbee_api_model_customer_address_api_model import BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel


class BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel(object):

    """Implementation of the 'Billbee.Interfaces.BillbeeAPI.Model.CreateCustomerApiModel' model.

    TODO: type model description here.

    Attributes:
        address (BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel):
            Container for passing address data
        id (long|int): The Billbee Id of the customer
        name (string): TODO: type description here.
        email (string): TODO: type description here.
        tel_1 (string): TODO: type description here.
        tel_2 (string): TODO: type description here.
        number (int): TODO: type description here.
        price_group_id (long|int): TODO: type description here.
        language_id (int): TODO: type description here.
        vat_id (string): TODO: type description here.
        mtype (int): Customer Type

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'Address',
        "id": 'Id',
        "name": 'Name',
        "email": 'Email',
        "tel_1": 'Tel1',
        "tel_2": 'Tel2',
        "number": 'Number',
        "price_group_id": 'PriceGroupId',
        "language_id": 'LanguageId',
        "vat_id": 'VatId',
        "mtype": 'Type'
    }

    def __init__(self,
                 address=None,
                 id=None,
                 name=None,
                 email=None,
                 tel_1=None,
                 tel_2=None,
                 number=None,
                 price_group_id=None,
                 language_id=None,
                 vat_id=None,
                 mtype=None):
        """Constructor for the BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel class"""

        # Initialize members of the class
        self.address = address
        self.id = id
        self.name = name
        self.email = email
        self.tel_1 = tel_1
        self.tel_2 = tel_2
        self.number = number
        self.price_group_id = price_group_id
        self.language_id = language_id
        self.vat_id = vat_id
        self.mtype = mtype

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
        address = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.from_dictionary(dictionary.get('Address')) if dictionary.get('Address') else None
        id = dictionary.get('Id')
        name = dictionary.get('Name')
        email = dictionary.get('Email')
        tel_1 = dictionary.get('Tel1')
        tel_2 = dictionary.get('Tel2')
        number = dictionary.get('Number')
        price_group_id = dictionary.get('PriceGroupId')
        language_id = dictionary.get('LanguageId')
        vat_id = dictionary.get('VatId')
        mtype = dictionary.get('Type')

        # Return an object of this model
        return cls(address,
                   id,
                   name,
                   email,
                   tel_1,
                   tel_2,
                   number,
                   price_group_id,
                   language_id,
                   vat_id,
                   mtype)