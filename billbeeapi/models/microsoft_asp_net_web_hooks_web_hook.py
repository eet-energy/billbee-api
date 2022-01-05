# -*- coding: utf-8 -*-

"""
billbeeapi

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class MicrosoftAspNetWebHooksWebHook(object):

    """Implementation of the 'Microsoft.AspNet.WebHooks.WebHook' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        web_hook_uri (string): TODO: type description here.
        secret (string): TODO: type description here.
        description (string): TODO: type description here.
        is_paused (bool): TODO: type description here.
        filters (list of string): TODO: type description here.
        headers (dict): TODO: type description here.
        properties (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "web_hook_uri": 'WebHookUri',
        "id": 'Id',
        "secret": 'Secret',
        "description": 'Description',
        "is_paused": 'IsPaused',
        "filters": 'Filters',
        "headers": 'Headers',
        "properties": 'Properties'
    }

    def __init__(self,
                 web_hook_uri=None,
                 id=None,
                 secret=None,
                 description=None,
                 is_paused=None,
                 filters=None,
                 headers=None,
                 properties=None):
        """Constructor for the MicrosoftAspNetWebHooksWebHook class"""

        # Initialize members of the class
        self.id = id
        self.web_hook_uri = web_hook_uri
        self.secret = secret
        self.description = description
        self.is_paused = is_paused
        self.filters = filters
        self.headers = headers
        self.properties = properties

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
        web_hook_uri = dictionary.get('WebHookUri')
        id = dictionary.get('Id')
        secret = dictionary.get('Secret')
        description = dictionary.get('Description')
        is_paused = dictionary.get('IsPaused')
        filters = dictionary.get('Filters')
        headers = dictionary.get('Headers')
        properties = dictionary.get('Properties')

        # Return an object of this model
        return cls(web_hook_uri,
                   id,
                   secret,
                   description,
                   is_paused,
                   filters,
                   headers,
                   properties)
