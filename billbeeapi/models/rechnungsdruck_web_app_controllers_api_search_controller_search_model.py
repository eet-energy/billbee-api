# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RechnungsdruckWebAppControllersApiSearchControllerSearchModel(object):

    """Implementation of the 'Rechnungsdruck.WebApp.Controllers.Api.SearchController.SearchModel' model.

    TODO: type model description here.

    Attributes:
        mtype (list of string): TODO: type description here.
        term (string): TODO: type description here.
        search_mode (SearchModeEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"mtype": "Type", "term": "Term", "search_mode": "SearchMode"}

    def __init__(self, mtype=None, term=None, search_mode=None):
        """Constructor for the RechnungsdruckWebAppControllersApiSearchControllerSearchModel class"""

        # Initialize members of the class
        self.mtype = mtype
        self.term = term
        self.search_mode = search_mode

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
        mtype = dictionary.get("Type")
        term = dictionary.get("Term")
        search_mode = dictionary.get("SearchMode")

        # Return an object of this model
        return cls(mtype, term, search_mode)
