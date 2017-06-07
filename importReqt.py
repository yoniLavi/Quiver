# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:06:22 2017

@author: abhilash
"""
from flask import Flask
from flask import request
from flask import json
from flask import Response
from flask_restful import Resource, Api
from sqlalchemy.orm import sessionmaker
from quiver_model_def import Requirement
#Import Requirements into  Database

def importRequirementsFromFile(fileName):
    dataFile=open(fileName,'r')
    requirements= []
    discardHeader= dataFile.readline()
    for line in dataFile:
        values=line.split(',')
        Require = Reqt(values[0],values[1],values[2],values[3], values[4])
        requirements.append(Require)
        return requirements
    
def addtoRequirementsList(requirements):
    con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    # query from a class
    for reqt in requirements:
        print (reqt.title)
        Require = Requirement(externalid=reqt.id,title= reqt.title, desc=reqt.desc,motivation=reqt.motive,typeofreqt=1)
        session.add(Require)
    session.commit()
    return 1

class Reqt:
        def __init__(self, id, title, desc, motive,verify):
            self.title = title
            self.id = id
            self.desc= desc
            self.motive= motive
            self.verify=verify
            
        def __repr__(self):
            return self.name
        def __str__(self):
        #return self's name
            return self.name
        def to_json(self):
            json_data ={
                'id': self.id,
                'title': self.title,
                'desc': self.desc,
                'motive': self.motive,
                'verification':self.verify
                
                
            }
            return json_data
    
required= importRequirementsFromFile('requirementslistasExcel.csv')
addtoRequirementsList(required)