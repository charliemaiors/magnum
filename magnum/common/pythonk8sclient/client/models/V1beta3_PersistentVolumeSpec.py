#!/usr/bin/env python
"""
Copyright 2015 Reverb Technologies, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class V1beta3_PersistentVolumeSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'accessModes': 'list[V1beta3_AccessModeType]',
            
            
            'capacity': 'dict',
            
            
            'claimRef': 'V1beta3_ObjectReference',
            
            
            'gcePersistentDisk': 'V1beta3_GCEPersistentDiskVolumeSource',
            
            
            'hostPath': 'V1beta3_HostPathVolumeSource'
            
        }

        self.attributeMap = {
            
            'accessModes': 'accessModes',
            
            'capacity': 'capacity',
            
            'claimRef': 'claimRef',
            
            'gcePersistentDisk': 'gcePersistentDisk',
            
            'hostPath': 'hostPath'
            
        }       

        
        #all ways the volume can be mounted
        
        self.accessModes = None # list[V1beta3_AccessModeType]
        
        #a description of the persistent volume&#39;s resources and capacity
        
        self.capacity = None # any
        
        #the binding reference to a persistent volume claim
        
        self.claimRef = None # V1beta3_ObjectReference
        
        #GCE disk resource provisioned by an admin
        
        self.gcePersistentDisk = None # V1beta3_GCEPersistentDiskVolumeSource
        
        #a HostPath provisioned by a developer or tester; for develment use only
        
        self.hostPath = None # V1beta3_HostPathVolumeSource
        
