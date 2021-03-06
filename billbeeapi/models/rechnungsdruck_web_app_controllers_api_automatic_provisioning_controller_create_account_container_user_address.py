"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainerUserAddress:

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.AutomaticProvisioningController.CreateAccountContainer.UserAddress' model.

    Represents the invoice address of a Billbee user

    Attributes:
        company (string): TODO: type description here.
        name (string): TODO: type description here.
        address_1 (string): TODO: type description here.
        address_2 (string): TODO: type description here.
        zip (string): TODO: type description here.
        city (string): TODO: type description here.
        country (string): The ISO2 country code of the users country
        vat_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "company": "Company",
        "name": "Name",
        "address_1": "Address1",
        "address_2": "Address2",
        "zip": "Zip",
        "city": "City",
        "country": "Country",
        "vat_id": "VatId",
    }

    def __init__(
        self, company=None, name=None, address_1=None, address_2=None, zip=None, city=None, country=None, vat_id=None
    ):
        """Constructor for the RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainerUserAddress class"""

        # Initialize members of the class
        self.company = company
        self.name = name
        self.address_1 = address_1
        self.address_2 = address_2
        self.zip = zip
        self.city = city
        self.country = country
        self.vat_id = vat_id

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
        company = dictionary.get("Company")
        name = dictionary.get("Name")
        address_1 = dictionary.get("Address1")
        address_2 = dictionary.get("Address2")
        zip = dictionary.get("Zip")
        city = dictionary.get("City")
        country = dictionary.get("Country")
        vat_id = dictionary.get("VatId")

        # Return an object of this model
        return cls(company, name, address_1, address_2, zip, city, country, vat_id)
