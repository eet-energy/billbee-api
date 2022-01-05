# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel(object):

    """Implementation of the 'Billbee.Interfaces.BillbeeAPI.Model.OrderAddressApiModel' model.

    TODO: type model description here.

    Attributes:
        billbee_id (long|int): TODO: type description here.
        first_name (string): TODO: type description here.
        last_name (string): TODO: type description here.
        company (string): TODO: type description here.
        name_addition (string): TODO: type description here.
        street (string): TODO: type description here.
        house_number (string): TODO: type description here.
        zip (string): TODO: type description here.
        city (string): TODO: type description here.
        country_iso_2 (string): TODO: type description here.
        country (string): TODO: type description here.
        line_2 (string): TODO: type description here.
        email (string): TODO: type description here.
        state (string): TODO: type description here.
        phone (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "billbee_id": 'BillbeeId',
        "first_name": 'FirstName',
        "last_name": 'LastName',
        "company": 'Company',
        "name_addition": 'NameAddition',
        "street": 'Street',
        "house_number": 'HouseNumber',
        "zip": 'Zip',
        "city": 'City',
        "country_iso_2": 'CountryISO2',
        "country": 'Country',
        "line_2": 'Line2',
        "email": 'Email',
        "state": 'State',
        "phone": 'Phone'
    }

    def __init__(self,
                 billbee_id=None,
                 first_name=None,
                 last_name=None,
                 company=None,
                 name_addition=None,
                 street=None,
                 house_number=None,
                 zip=None,
                 city=None,
                 country_iso_2=None,
                 country=None,
                 line_2=None,
                 email=None,
                 state=None,
                 phone=None):
        """Constructor for the BillbeeInterfacesBillbeeAPIModelOrderAddressApiModel class"""

        # Initialize members of the class
        self.billbee_id = billbee_id
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.name_addition = name_addition
        self.street = street
        self.house_number = house_number
        self.zip = zip
        self.city = city
        self.country_iso_2 = country_iso_2
        self.country = country
        self.line_2 = line_2
        self.email = email
        self.state = state
        self.phone = phone

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
        billbee_id = dictionary.get('BillbeeId')
        first_name = dictionary.get('FirstName')
        last_name = dictionary.get('LastName')
        company = dictionary.get('Company')
        name_addition = dictionary.get('NameAddition')
        street = dictionary.get('Street')
        house_number = dictionary.get('HouseNumber')
        zip = dictionary.get('Zip')
        city = dictionary.get('City')
        country_iso_2 = dictionary.get('CountryISO2')
        country = dictionary.get('Country')
        line_2 = dictionary.get('Line2')
        email = dictionary.get('Email')
        state = dictionary.get('State')
        phone = dictionary.get('Phone')

        # Return an object of this model
        return cls(billbee_id,
                   first_name,
                   last_name,
                   company,
                   name_addition,
                   street,
                   house_number,
                   zip,
                   city,
                   country_iso_2,
                   country,
                   line_2,
                   email,
                   state,
                   phone)