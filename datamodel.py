# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 08:49:21 2017

@author: abhilash
"""

class Product(object):
    def __init__(self, name, desc, domain, business_seg, parent=None):
        self.name = name
        self.desc = desc
        self.domain = domain
        self.business_seg=  business_seg
        self.parent = parent
    
    def __repr__(self):
        return '<Level %s>' % self.name

class ProductVersion(object):
    def __init__(self, name, product_name, desc, parent=None):
        self.name = name
        self.product_name = product_name
        self.desc = desc
        self.parent = parent
        self.requirements =[]
        self.customerneeds=[]
    def __repr__(self):
        return '<Level %s>' % self.name

class Requirement(object):
    def __init__(self, externalid, title, desc, motivation, verification, typeofreqt, parent=None):
        #self.id= id
        self.title = title
        self.externalid=externalid
        self.desc = desc
        self.motivation = motivation
        self.verification= verification
        self.typeofreqt= typeofreqt
        self.parent = parent
    
    def __repr__(self):
        return '<Level %s>' % self.name

class CustomerNeed(object):
    def __init__(self, id, title, desc, role, phaseinlifecycle,  parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.role = role
        self.phaseinlifecycle= phaseinlifecycle
        self.requirements= []
        self.primaryneeds = []
        self.latentneeds =[]
        self.parent=parent
    
    def __repr__(self):
        return '<Level %s>' % self.name

class PrimaryNeed(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.secondaryneeds= []
        self.latentneeds =[]
        self.parent=parent
    
    def __repr__(self):
        return '<Level %s>' % self.name   

class SecondaryNeed(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.latentneeds =[]
        self.parent=parent
    
    def __repr__(self):
        return '<Level %s>' % self.name 

class LatentNeed(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.parent=parent
    
    def __repr__(self):
        return '<Level %s>' % self.name 
        
#For Handling Scenarios
class Scenario(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.parent=parent
        
    def __repr__(self):
        return '<Level %s>' % self.name 

class Source(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.parent=parent
    
    def __repr__(self):
        return '<Level %s>' % self.name 


class Stimulus(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.parent=parent
        
    
    def setSource(self,Source):
        self.source=Source
    def setStimulus(self,Stimulus):
        self.stimulus=Stimulus
    def setArtifact(self,Artifact):
        self.artifact=Artifact
    def setEnvironment(self,Environment):
        self.environment=Environment
    def setResponseMeasure(self,ResponseMeasure):
        self.response_measure=ResponseMeasure
   
    def getSource(self):
        return self.source
    def getStimulus(self):
        return self.stimulus
    def getArtifact(self):
        return self.artifact
    def getEnvironment(self):
        return self.environment
    def getResponseMeasure(self):
        return self.response_measure
        
    def __repr__(self):
        return '<Level %s>' % self.name 

class Artifact(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.parent=parent
    
    def __repr__(self):
        return '<Level %s>' % self.name 


class Environment(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.parent=parent
    
    def __repr__(self):
        return '<Level %s>' % self.name 


class ResponseMeasure(object):
    def __init__(self, id, title, desc,parent=None):
        self.id= id
        self.title = title
        self.desc = desc
        self.parent=parent
    
    def __repr__(self):
        return '<Level %s>' % self.name 
        
