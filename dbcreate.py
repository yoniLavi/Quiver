# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 17:59:30 2017

@author: abhilash
"""

from quiver_model_def import connect,create_database

#Product, Product_Version, Requirement, CustomerNeed, PrimaryNeed, SecondaryNeed, LatentNeed
    
    

def create_database_tables():
    con,meta=connect('postgres','adarsh1','quiver2')
    create_database(meta,con)
    return 1
    