# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class BillbeeInterfacesBillbeeAPIModelArticleSourceApiModel(object):

    """Implementation of the 'Billbee.Interfaces.BillbeeAPI.Model.ArticleSourceApiModel' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        source (string): TODO: type description here.
        source_id (string): TODO: type description here.
        api_account_name (string): TODO: type description here.
        api_account_id (long|int): TODO: type description here.
        export_factor (float): TODO: type description here.
        stock_sync_inactive (bool): TODO: type description here.
        stock_sync_min (float): TODO: type description here.
        stock_sync_max (float): TODO: type description here.
        units_per_item (float): TODO: type description here.
        custom (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "source": "Source",
        "source_id": "SourceId",
        "id": "Id",
        "api_account_name": "ApiAccountName",
        "api_account_id": "ApiAccountId",
        "export_factor": "ExportFactor",
        "stock_sync_inactive": "StockSyncInactive",
        "stock_sync_min": "StockSyncMin",
        "stock_sync_max": "StockSyncMax",
        "units_per_item": "UnitsPerItem",
        "custom": "Custom",
    }

    def __init__(
        self,
        source=None,
        source_id=None,
        id=None,
        api_account_name=None,
        api_account_id=None,
        export_factor=None,
        stock_sync_inactive=None,
        stock_sync_min=None,
        stock_sync_max=None,
        units_per_item=None,
        custom=None,
    ):
        """Constructor for the BillbeeInterfacesBillbeeAPIModelArticleSourceApiModel class"""

        # Initialize members of the class
        self.id = id
        self.source = source
        self.source_id = source_id
        self.api_account_name = api_account_name
        self.api_account_id = api_account_id
        self.export_factor = export_factor
        self.stock_sync_inactive = stock_sync_inactive
        self.stock_sync_min = stock_sync_min
        self.stock_sync_max = stock_sync_max
        self.units_per_item = units_per_item
        self.custom = custom

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
        source = dictionary.get("Source")
        source_id = dictionary.get("SourceId")
        id = dictionary.get("Id")
        api_account_name = dictionary.get("ApiAccountName")
        api_account_id = dictionary.get("ApiAccountId")
        export_factor = dictionary.get("ExportFactor")
        stock_sync_inactive = dictionary.get("StockSyncInactive")
        stock_sync_min = dictionary.get("StockSyncMin")
        stock_sync_max = dictionary.get("StockSyncMax")
        units_per_item = dictionary.get("UnitsPerItem")
        custom = dictionary.get("Custom")

        # Return an object of this model
        return cls(
            source,
            source_id,
            id,
            api_account_name,
            api_account_id,
            export_factor,
            stock_sync_inactive,
            stock_sync_min,
            stock_sync_max,
            units_per_item,
            custom,
        )
