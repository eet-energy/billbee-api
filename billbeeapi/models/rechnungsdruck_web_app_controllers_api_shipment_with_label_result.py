"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""
from billbeeapi.api_helper import APIHelper


class RechnungsdruckWebAppControllersApiShipmentWithLabelResult:

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.ShipmentWithLabelResult' model.

    TODO: type model description here.

    Attributes:
        order_id (long|int): TODO: type description here.
        order_reference (string): TODO: type description here.
        shipping_id (string): TODO: type description here.
        tracking_url (string): TODO: type description here.
        label_data_pdf (string): TODO: type description here.
        export_docs_pdf (string): TODO: type description here.
        carrier (string): TODO: type description here.
        shipping_date (datetime): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "order_id": "OrderId",
        "order_reference": "OrderReference",
        "shipping_id": "ShippingId",
        "tracking_url": "TrackingUrl",
        "label_data_pdf": "LabelDataPdf",
        "export_docs_pdf": "ExportDocsPdf",
        "carrier": "Carrier",
        "shipping_date": "ShippingDate",
    }

    def __init__(
        self,
        order_id=None,
        order_reference=None,
        shipping_id=None,
        tracking_url=None,
        label_data_pdf=None,
        export_docs_pdf=None,
        carrier=None,
        shipping_date=None,
    ):
        """Constructor for the RechnungsdruckWebAppControllersApiShipmentWithLabelResult class"""

        # Initialize members of the class
        self.order_id = order_id
        self.order_reference = order_reference
        self.shipping_id = shipping_id
        self.tracking_url = tracking_url
        self.label_data_pdf = label_data_pdf
        self.export_docs_pdf = export_docs_pdf
        self.carrier = carrier
        self.shipping_date = APIHelper.RFC3339DateTime(shipping_date) if shipping_date else None

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
        order_reference = dictionary.get("OrderReference")
        shipping_id = dictionary.get("ShippingId")
        tracking_url = dictionary.get("TrackingUrl")
        label_data_pdf = dictionary.get("LabelDataPdf")
        export_docs_pdf = dictionary.get("ExportDocsPdf")
        carrier = dictionary.get("Carrier")
        shipping_date = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("ShippingDate")).datetime
            if dictionary.get("ShippingDate")
            else None
        )

        # Return an object of this model
        return cls(
            order_id,
            order_reference,
            shipping_id,
            tracking_url,
            label_data_pdf,
            export_docs_pdf,
            carrier,
            shipping_date,
        )
