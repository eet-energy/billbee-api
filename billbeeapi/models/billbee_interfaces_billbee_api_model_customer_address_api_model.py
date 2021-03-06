"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel:

    """Implementation of the 'Billbee.Interfaces.BillbeeAPI.Model.CustomerAddressApiModel' model.

    Container for passing address data

    Attributes:
        id (long|int): The internal Billbee ID of the address record. Can be
            null if a new address is created
        address_type (AddressTypeEnum): The type of the address
        customer_id (long|int): The internal Billbee id of the customer the
            address belongs to
        company (string): The name of the company
        first_name (string): TODO: type description here.
        last_name (string): TODO: type description here.
        name_2 (string): Optionally an additional name field
        street (string): TODO: type description here.
        housenumber (string): TODO: type description here.
        zip (string): TODO: type description here.
        city (string): TODO: type description here.
        state (string): TODO: type description here.
        country_code (string): The ISO2 code of the country
        email (string): TODO: type description here.
        tel_1 (string): TODO: type description here.
        tel_2 (string): TODO: type description here.
        fax (string): TODO: type description here.
        address_addition (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "address_type": "AddressType",
        "customer_id": "CustomerId",
        "company": "Company",
        "first_name": "FirstName",
        "last_name": "LastName",
        "name_2": "Name2",
        "street": "Street",
        "housenumber": "Housenumber",
        "zip": "Zip",
        "city": "City",
        "state": "State",
        "country_code": "CountryCode",
        "email": "Email",
        "tel_1": "Tel1",
        "tel_2": "Tel2",
        "fax": "Fax",
        "address_addition": "AddressAddition",
    }

    def __init__(
        self,
        id=None,
        address_type=None,
        customer_id=None,
        company=None,
        first_name=None,
        last_name=None,
        name_2=None,
        street=None,
        housenumber=None,
        zip=None,
        city=None,
        state=None,
        country_code=None,
        email=None,
        tel_1=None,
        tel_2=None,
        fax=None,
        address_addition=None,
    ):
        """Constructor for the BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel class"""

        # Initialize members of the class
        self.id = id
        self.address_type = address_type
        self.customer_id = customer_id
        self.company = company
        self.first_name = first_name
        self.last_name = last_name
        self.name_2 = name_2
        self.street = street
        self.housenumber = housenumber
        self.zip = zip
        self.city = city
        self.state = state
        self.country_code = country_code
        self.email = email
        self.tel_1 = tel_1
        self.tel_2 = tel_2
        self.fax = fax
        self.address_addition = address_addition

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
        address_type = dictionary.get("AddressType")
        customer_id = dictionary.get("CustomerId")
        company = dictionary.get("Company")
        first_name = dictionary.get("FirstName")
        last_name = dictionary.get("LastName")
        name_2 = dictionary.get("Name2")
        street = dictionary.get("Street")
        housenumber = dictionary.get("Housenumber")
        zip = dictionary.get("Zip")
        city = dictionary.get("City")
        state = dictionary.get("State")
        country_code = dictionary.get("CountryCode")
        email = dictionary.get("Email")
        tel_1 = dictionary.get("Tel1")
        tel_2 = dictionary.get("Tel2")
        fax = dictionary.get("Fax")
        address_addition = dictionary.get("AddressAddition")

        # Return an object of this model
        return cls(
            id,
            address_type,
            customer_id,
            company,
            first_name,
            last_name,
            name_2,
            street,
            housenumber,
            zip,
            city,
            state,
            country_code,
            email,
            tel_1,
            tel_2,
            fax,
            address_addition,
        )
