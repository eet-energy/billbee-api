"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from billbeeapi.api_helper import APIHelper
from billbeeapi.models.billbee_interfaces_shipping_shipment_data_dimensions import (
    BillbeeInterfacesShippingShipmentDataDimensions,
)


class RechnungsdruckWebAppControllersApiShipmentWithLabel:

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.ShipmentWithLabel' model.

    TODO: type model description here.

    Attributes:
        order_id (long|int): The Billbee internal id of the order to ship
        provider_id (long|int): The id of the provider. You can query all
            providers with the shippingproviders endpoint
        product_id (long|int): the id of the shipping provider product to be
            used
        change_state_to_send (bool): Optional parameter to automatically
            change the orderstate to sent after creating the shipment
        printer_name (string): Optional the name of a connected cloudprinter
            to send the label to
        weight_in_gram (int): Optional the shipments weight in gram to
            override the calculated weight
        ship_date (datetime): Optional specify the shipdate to be transmitted
            to the carrier
        client_reference (string): Optional specify a reference text to be
            included on the label. Works not with all carriers
        dimension (BillbeeInterfacesShippingShipmentDataDimensions): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "order_id": "OrderId",
        "provider_id": "ProviderId",
        "product_id": "ProductId",
        "change_state_to_send": "ChangeStateToSend",
        "printer_name": "PrinterName",
        "weight_in_gram": "WeightInGram",
        "ship_date": "ShipDate",
        "client_reference": "ClientReference",
        "dimension": "Dimension",
    }

    def __init__(
        self,
        order_id=None,
        provider_id=None,
        product_id=None,
        change_state_to_send=None,
        printer_name=None,
        weight_in_gram=None,
        ship_date=None,
        client_reference=None,
        dimension=None,
    ):
        """Constructor for the RechnungsdruckWebAppControllersApiShipmentWithLabel class"""

        # Initialize members of the class
        self.order_id = order_id
        self.provider_id = provider_id
        self.product_id = product_id
        self.change_state_to_send = change_state_to_send
        self.printer_name = printer_name
        self.weight_in_gram = weight_in_gram
        self.ship_date = APIHelper.RFC3339DateTime(ship_date) if ship_date else None
        self.client_reference = client_reference
        self.dimension = dimension

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
        order_id = dictionary.get("OrderId")
        provider_id = dictionary.get("ProviderId")
        product_id = dictionary.get("ProductId")
        change_state_to_send = dictionary.get("ChangeStateToSend")
        printer_name = dictionary.get("PrinterName")
        weight_in_gram = dictionary.get("WeightInGram")
        ship_date = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("ShipDate")).datetime
            if dictionary.get("ShipDate")
            else None
        )
        client_reference = dictionary.get("ClientReference")
        dimension = (
            BillbeeInterfacesShippingShipmentDataDimensions.from_dictionary(dictionary.get("Dimension"))
            if dictionary.get("Dimension")
            else None
        )

        # Return an object of this model
        return cls(
            order_id,
            provider_id,
            product_id,
            change_state_to_send,
            printer_name,
            weight_in_gram,
            ship_date,
            client_reference,
            dimension,
        )
