# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TemplateLink(Model):
    """Entity representing the reference to the template.

    :param uri: The URI of the template to deploy.
    :type uri: str
    :param content_version: If included, must match the ContentVersion in the
     template.
    :type content_version: str
    """ 

    _validation = {
        'uri': {'required': True},
    }

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'content_version': {'key': 'contentVersion', 'type': 'str'},
    }

    def __init__(self, uri, content_version=None):
        self.uri = uri
        self.content_version = content_version