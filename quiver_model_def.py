# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 22:34:26 2017

@author: abhilash
"""

import sqlalchemy 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey,  Table
from sqlalchemy.orm import relationship,backref

def connect(user, password, db, host='localhost', port=5432):
 #''Returns a connection and a metadata object'''
 # We connect with the help of the PostgreSQL URL
 # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
 # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')
 # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con, meta


class Product(Base):
    __tablename__='products'
    id = Column(Integer,Sequence('seq_product_id', start=1, increment=1),primary_key=True)
    name = Column(String, unique=True)
    desc = Column(String)
    domain = Column(String)
    business_segment = Column(String)
    #backref and back_populates are same
    Versions = relationship("Product_Version", backref=backref('products',order_by=id))
    Scenarios = relationship("Scenario", back_populates="products")   
    def get_products(con, meta):
        query =con.execute( meta.tables['products'].select())
        return query
    def __repr__(self):
        return "<Products(name='%s', desc='%s', domain='%s', business_segment='%s')>" % (
        self.name, self.desc, self.domain, self.business_segment)

class Product_Version(Base):
    __tablename__='product_versions'
    id = Column(Integer,Sequence('seq_product_version_id', start=1, increment=1),primary_key=True)
    product_id=Column(Integer,ForeignKey('products.id'))

    name = Column(String, unique=True)
    desc = Column(String)
    product = relationship ("Product",backref=backref('product_versions',order_by=id))
    Requirements = relationship("Requirement",
                    secondary="product_version_requirement_assoc",
                    backref=backref('product_versions',order_by=id))
    def setProduct(self,product):
        self.product=product
        
    def __repr__(self):
        
        return "<Product Version(name='%s', desc='%s')>" % (
        self.name, self.desc)

product_version_requirement_assoc = Table('product_version_requirement_assoc', Base.metadata,
    Column('left_id', Integer, ForeignKey('product_versions.id'),primary_key=True),
    Column('right_id', Integer, ForeignKey('requirements.id'),primary_key=True)
)

customer_need_requirement_assoc = Table('customer_need_requirement_assoc', Base.metadata,
    Column('left_id', Integer, ForeignKey('customer_needs.id'),primary_key=True),
    Column('right_id', Integer, ForeignKey('requirements.id'),primary_key=True)
)
class Requirement(Base):
    __tablename__='requirements'
    id = Column(Integer,Sequence('seq_requrement_id', start=1, increment=1),primary_key=True)
    externalId=Column(String)
    title=Column(String)
    desc = Column(String)
    motivation = Column(String)
    verification = Column(String)
    typeofreqt=Column(Integer)
   #BackRef to Products required
    ProductVersions = relationship("Product_Version",
              secondary="product_version_requirement_assoc",
               backref=backref('requirements',order_by=id) )
              
    CustomerNeeds = relationship("CustomerNeed",
                    secondary="customer_need_requirement_assoc",
                    backref="requirements")
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)

class CustomerNeed(Base):
    __tablename__='customer_needs'
    id = Column(Integer,Sequence('seq_cust_need_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    role = Column(String)
    phaseinlifeycle = Column(String)
    
    requirementS = relationship("Requirement",
                    secondary="customer_need_requirement_assoc",
                    backref="customer_needs")    
   #BackRef to Products required
    primaryNeeds = relationship("PrimaryNeed", primaryjoin="CustomerNeed.id==PrimaryNeed.customer_needs_id", back_populates="customer_needs")
    latentNeeds = relationship("LatentNeed", primaryjoin="CustomerNeed.id==LatentNeed.customer_needs_id", back_populates="customer_needs")
   
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)

class PrimaryNeed(Base):
    __tablename__='primary_needs'
    id = Column(Integer,Sequence('seq_primary_need_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    customer_needs_id = Column(Integer, ForeignKey('customer_needs.id'))
    #BackRef to Needs required
    customer_needs = relationship("CustomerNeed", backref="primary_needs")
    #SecondaryNeeds = relationship("SecondaryNeed", primaryjoin=" PrimaryNeed.id==SecondaryNeed.primary_need_id", back_populates="primary_needs")
    
    def __repr__(self):
        return "<Primary Needs(title='%s', desc='%s')>" % (
        self.title, self.desc)

    
class LatentNeed(Base):
    __tablename__='latent_needs'
    id = Column(Integer,Sequence('seq_latent_need_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    customer_needs_id = Column(Integer, ForeignKey('customer_needs.id'))
    #BackRef to Primary Needs required
    customer_needs = relationship("CustomerNeed", backref="latent_needs")
   
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)
        
# New additionts to support Scenarios

class Source(Base):
    __tablename__='sources'
#    id = Column(Integer,Sequence('seq_source_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'), primary_key=True)
    #BackRef to Primary Needs required
    #scenarios = relationship("Scenario", backref="scenarios", uselist=False)
   
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)


class Stimulus(Base):
    __tablename__='stimuli'
    #id = Column(Integer,Sequence('seq_stimulus_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'), primary_key=True)
    #BackRef to Primary Needs required
    #scenarios = relationship("Scenario", backref="scenarios", uselist=False)
   
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)

class Artifact(Base):
    __tablename__='artifacts'
    #id = Column(Integer,Sequence('seq_artifact_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'), primary_key=True)
    #BackRef to Primary Needs required
    #scenarios = relationship("Scenario", backref="scenarios", uselist=False)
   
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)


class Environment(Base):
    __tablename__='environments'
    #id = Column(Integer,Sequence('seq_environment_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'), primary_key=True)
    #BackRef to Primary Needs required
    #scenarios = relationship("Scenario", backref="scenarios", uselist=False)
   
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)
        
class ResponseMeasure(Base):
    __tablename__='response_measures'
    #id = Column(Integer,Sequence('seq_resp_measure_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'), primary_key=True)
    #BackRef to Primary Needs required
    #scenarios = relationship("Scenario", backref="scenarios", uselist=False)
   
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)


class Scenario(Base):
    __tablename__='scenarios'
    id = Column(Integer,Sequence('seq_artifact_id', start=1, increment=1),primary_key=True)
    title=Column(String)
    desc = Column(String)
    #source_id=Column(Integer,None,ForeignKey('sources.id'))
    #stimulus_id=Column(Integer,None,ForeignKey('stimuli.id'))
    #artifact_id=Column(Integer,None,ForeignKey('artifacts.id'))
    #env_id=Column(Integer,None,ForeignKey('environments.id'))
    #respMeas_id=Column(Integer,None,ForeignKey('response_measures.id'))
    product_id=Column(Integer,ForeignKey('products.id'))
    products = relationship ("Product",backref="products")
    #BackRef to Primary Needs required
    source = relationship("Source", backref="scenarios")
    stimulus = relationship("Stimulus", backref="scenarios")
    artifact = relationship("Artifact", backref="scenarios")
    environment = relationship("Environment", backref="scenarios")
    responsemeasure = relationship("ResponseMeasure", backref="scenarios")
    
    def __repr__(self):
        return "<Requirement(title='%s', desc='%s')>" % (
        self.title, self.desc)

        
#def create_database( engine):
#    #Base.metadata.drop_all(engine)
#    Base.metadata.
#    Base.metadata.create_all(engine)
#    return 0
    
def create_database( metaData,con):
    #Base.metadata.drop_all(engine)
    Base.metadata.drop_all(con)
    Base.metadata.create_all(con)
    return 0