# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel(object):

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.ApiAddShipmentToOrderModel' model.

    Data of the shipment to be created

    Attributes:
        shipping_id (string): The id of the shipment
            (Sendungsnummer/trackingid)
        order_id (string): Optional a differing order number of the shipment
            if available
        comment (string): Optional a text stored with the shipment
        shipping_provider_id (long|int): Optional the id of a shipping
            provider existing in the billbee account that should be assigned
            to the shipment
        shipping_provider_product_id (long|int): Optional the id of a shipping
            provider product that should be assigend to the shipment
        carrier_id (int): Optional the id of a shipping carrier that should be
            assigend to the shipment  Will override the carrier from the
            shipment product.  Please use the integer value from this
            Enumeration:  {Billbee.Interfaces.Shipping.Enums.ShippingCarrier}

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "shipping_id": "ShippingId",
        "order_id": "OrderId",
        "comment": "Comment",
        "shipping_provider_id": "ShippingProviderId",
        "shipping_provider_product_id": "ShippingProviderProductId",
        "carrier_id": "CarrierId",
    }

    def __init__(
        self,
        shipping_id=None,
        order_id=None,
        comment=None,
        shipping_provider_id=None,
        shipping_provider_product_id=None,
        carrier_id=None,
    ):
        """Constructor for the RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel class"""

        # Initialize members of the class
        self.shipping_id = shipping_id
        self.order_id = order_id
        self.comment = comment
        self.shipping_provider_id = shipping_provider_id
        self.shipping_provider_product_id = shipping_provider_product_id
        self.carrier_id = carrier_id

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
        shipping_id = dictionary.get("ShippingId")
        order_id = dictionary.get("OrderId")
        comment = dictionary.get("Comment")
        shipping_provider_id = dictionary.get("ShippingProviderId")
        shipping_provider_product_id = dictionary.get("ShippingProviderProductId")
        carrier_id = dictionary.get("CarrierId")

        # Return an object of this model
        return cls(shipping_id, order_id, comment, shipping_provider_id, shipping_provider_product_id, carrier_id)
