# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:57:09 2017

@author: abhilash
"""

from flask import Flask
from flask import Response
from flask import json
from flask import render_template, redirect
from flask import request
from flask_restful import Api
from sqlalchemy.orm import sessionmaker
from quiver_model_def import *
#from flask import auth

 
app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])

    
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"
    elif request.method == 'POST':
        return "ECHO: POST\n"
    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"
    elif request.method == 'PUT':
        return "ECHO: PUT\n"
    elif request.method == 'DELETE':
        return "ECHO: DELETE"

@app.route('/messages', methods = ['POST'])
def api_message():
    if request.headers['Content‐Type'] == 'text/plain':
        return "Text Message: " + request.data
    elif request.headers['Content‐Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    elif request.headers['Content‐Type'] == 'application/octet‐stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    else:
        return "415 Unsupported Media Type ;)"


@app.route ('/login')
def login():
    return render_template('auth\login.html')
    
@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
    'hello' : 'world',
    'number' : 3
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'
    return resp
# for Rendering Web Pages
    
@app.route('/index', methods=['GET','POST'])
def render_index():
    return render_template('index.html')

@app.route('/scenarios', methods=['GET','POST'])
def render_scenarios():
    return render_template('scenarios.html')

@app.route('/requirementdetail/<int:reqt_id>', methods=['GET','POST'])
def render_requirementdetail(reqt_id):
    return render_template('requirement_detail.html',reqtid=reqt_id)

@app.route('/views', methods=['GET','POST'])
def render_views():
    return render_template('views.html')

@app.route('/people', methods=['GET','POST'])
def render_people():
    return render_template('people.html')

@app.route('/decisions', methods=['GET','POST'])
def render_decisions():
    return render_template('decisions.html')

#Addion pages

@app.route('/addproduct', methods=['GET','POST'])
def render_addproducts():
    #products = api_get_products()
    #con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    #Session = sessionmaker(bind=con)
    # create a Session
    #session = Session()
    # query from a class
    
    #products=session.query(Product)
    #products =Product.get_products(con,meta)
    
    return render_template('add_product.html')

@app.route('/addproductversion', methods=['GET','POST'])
def render_addproductversion():
    #products = api_get_products()
    #con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    #Session = sessionmaker(bind=con)
    # create a Session
    #session = Session()
    # query from a class
    
    #products=session.query(Product)
    #products =Product.get_products(con,meta)
    
    return render_template('add_product_version.html')    

@app.route('/addrequirements', methods=['GET','POST'])
def render_addrequirements():
    #products = api_get_products()
    #con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    #Session = sessionmaker(bind=con)
    # create a Session
    #session = Session()
    # query from a class
    
    #products=session.query(Product)
    #products =Product.get_products(con,meta)
    
    return render_template('scenario_add.html')    
    
# for RESTful Services


@app.route('/requirement/<int:reqt_id>', methods=['GET'])
def api_get_requirement_detail(reqt_id):
    # go to  database via ORM and get the  products
    # 1.connect to database
    # 2.
    # make JSON object out of products
    con, meta = connect('postgres', 'adarsh1', 'quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    # query from a class
    #Requirement=None
    requirement = session.query(Requirement).filter(Requirement.id==reqt_id).one()
    data = {
        'id': 1,
        'name': 'test'
    }

    class ReqtDet:
        def __init__(self, id,extid, title, desc, motivation, verification):
            self.Id=id
            self.extId = extid
            self.title = title
            self.desc = desc
            self.motivation = motivation
            self.verification = verification

        def __repr__(self):
            return self.title

        def __str__(self):
            # return self's name
            return self.title

        def to_json(self):
            json_data = {
                'id': self.Id,
                'externalid': self.extId,
                'title': self.title,
                'desc': self.desc,
                'motivation': self.motivation,
                'verification': self.verification

            }
            return json_data

    #for p in requirementQuery:
    #requirement=requirementQuery.first()
    RequireDetail= ReqtDet(requirement.id, requirement.externalId,requirement.title, requirement.desc, requirement.motivation,
                           requirement.verification)

    # dataList={ dataList}
    js = json.dumps(RequireDetail.to_json())
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp


@app.route('/products', methods = ['GET'])
def api_get_products():
    
    #go to  database via ORM and get the  products
    #1.connect to database
    #2.
    #make JSON object out of products
    con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    # query from a class
    
    products=session.query(Product)
    products =Product.get_products(con,meta)
    data = {
    'id' : 1,
    'name' : 'test'
    }
    dataList =[]
    class dataPdt:
        def __init__(self, id, name, desc, domain, business_seg):
            self.name = name
            self.id = id
            self.desc=desc
            self.domain=domain
            self.business_seg=business_seg
        def __repr__(self):
            return self.name
        def __str__(self):
        #return self's name
            return self.name
        def to_json(self):
            json_data ={
                'id': self.id,
                'name': self.name,
                'desc': self.desc,
                'domain': self.domain,
                'business_seg':self.business_seg
                
            }
            return json_data
            
    for p  in list(products):
        dataProd= dataPdt(p.id,p.name,p.desc,p.domain,p.business_segment)
         #data['id']=p.id
        #data['name']=p.name
        dataList.append(dataProd.to_json())
    
    #dataList={ dataList}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp

#Add

@app.route('/product/add', methods = ['PUT'])
def api_add_product():
    
    #go to  database via ORM and get the  products
    #1.connect to database
    #2.
    #make JSON object out of products
    con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    # query from a class
    if 'name' in request.json:
        name=request.json['name']
    if 'desc' in request.json:
        desc=request.json['desc']
    if 'domain' in request.json:
        domain=request.json['domain']
    if 'business_seg' in request.json:
        business_seg=request.json['business_seg']
    
    Pdt = Product(name=name,desc=desc,domain=domain,business_segment=business_seg) 
    session.add(Pdt)
    session.commit()
    #con.close()
    dataList={'add': '1'}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp

#Add Product Version

@app.route('/product/<int:id>/version/add', methods = ['PUT'])
def api_add_product_version(id):
    
    #go to  database via ORM and get the  products
    #1.connect to database
    #2.
    #make JSON object out of products
    con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    # query from a class
    if 'name' in request.json:
        name=request.json['name']
    if 'desc' in request.json:
        desc=request.json['desc']
    product=session.query(Product).filter(Product.id==id).one()
    PdtVer = Product_Version(name=name,desc=desc)
    PdtVer.product=product
    product.product_versions.append(PdtVer)
    session.add(PdtVer)
    session.commit()
    #con.close()
    dataList={'add': '1'}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp

#Add Requirements

@app.route('/<int:prod_id>/<int:vers_id>/requirements/add', methods = ['PUT'])
def api_add_requirement(prod_id,vers_id):
    
    #go to  database via ORM and get the  products
    #1.connect to database
    #2.
    #make JSON object out of products
    con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    # query from a class
    if 'externalId' in request.json:
        externalId=request.json['externalId']
    if 'title' in request.json:
        title=request.json['title']
   
    if 'desc' in request.json:
        desc=request.json['desc']
    if 'motivation' in request.json:
        motive=request.json['motivation']
    if 'verification' in request.json:
        verify=request.json['verification']
      
    if 'typeofreqt' in request.json:
        typeofreqt=request.json['typeofreqt']
    
    Reqt = Requirement(externalId=externalId,title=title,desc=desc,motivation=motive,
                       verification=verify,typeofreqt=typeofreqt) 
    #Get the Product Version
    product_version=session.query(Product_Version).filter(Product_Version.id==vers_id).filter(Product_Version.product_id==prod_id).one()
    #print(product_version.id)    
    Reqt.product_versions.append(product_version)
    product_version.Requirements.append(Reqt)
    session.add(Reqt)
    session.commit()
    #con.close()
    dataList={'add': '1'}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp


@app.route('/<int:prod_id>/<int:vers_id>/requirements/addmultiple', methods=['PUT'])
def api_add_multi_requirement(prod_id, vers_id):
    # go to  database via ORM and get the  products
    # 1.connect to database
    # 2.
    # make JSON object out of products
    con, meta = connect('postgres', 'adarsh1', 'quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    #reqt_list=0
    if 'requirements' in request.json:
        reqt_list = request.json['requirements']
    # Get the Product Version
    product_version = session.query(Product_Version).filter(Product_Version.id == vers_id).filter(
    Product_Version.product_id == prod_id).one()

    for  reqt in reqt_list:
        #reqt1= json.load(reqt)
        #print (reqt['title'])
        Reqt = Requirement(externalId=reqt['externalid'], title=reqt['title'], desc=reqt['desc'],
                           motivation=reqt['motivation'], verification=reqt['verification'], typeofreqt=reqt['typeofreqt'])
    # print(product_version.id)
        Reqt.product_versions.append(product_version)
        product_version.Requirements.append(Reqt)
        session.add(Reqt)
        session.commit()
    # con.close()
    dataList = {'add': '1'}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp

@app.route('/<int:prod_id>/<int:vers_id>/requirements/all', methods=['GET'])
def api_get_allrequirements(prod_id, vers_id):
    # go to  database via ORM and get the  products
    # 1.connect to database
    # 2.
    # make JSON object out of products
    con, meta = connect('postgres', 'adarsh1', 'quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    #reqt_list=0
    # Get the Product Version
    requirements = session.query(Requirement).join(Requirement.ProductVersions).filter(Product_Version.id ==vers_id).filter(Product_Version.product_id==prod_id)
    #subqueryload(Child.subelements)).all()
        #.options(joinedload).join(Product_Versions).filter(ProductVersions.has( product_id== prod_id))
    dataList = []

    class dataReqt:
        def __init__(self,Id, extId, title, desc, motivation, verification):
            self.id = Id
            self.extId = extId
            self.title = title
            self.desc = desc
            self.motivation = motivation
            self.verification = verification

        def __repr__(self):
            return self.name

        def __str__(self):
            # return self's name
            return self.title

        def to_json(self):
            json_data = {
                'id': self.id,
                'externalid': self.extId,
                'title': self.title,
                'desc': self.desc,
                'motivation': self.motivation,
                'verification': self.verification

            }
            return json_data

    for p in list(requirements):
        dataRqt = dataReqt(p.id,p.externalId, p.title, p.desc, p.motivation, p.verification)
            # data['id']=p.id
            # data['name']=p.name
        dataList.append(dataRqt.to_json())

    # con.close()
    #dataList = {'add': '1'}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp


@app.route('/upload', methods=['GET','POST'])
def uploadfile():
    # go to  database via ORM and get the  products
    # 1.connect to database
    # 2.
    # make JSON object out of products
    # create a Session
    # con.close()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
    dataList = {'add': '1'}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp

@app.route('/<int:id>/versions', methods = ['GET'])
def api_get_product_versions(id):
    
    #go to  database via ORM and get the  products
    #1.connect to database
    #2.
    #make JSON object out of products
    con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    # query from a class
    product_versions=session.query(Product_Version).filter(Product_Version.product_id==id)
    #product_versions =Product_Version.get(con,meta)
    dataList=[]
    for p  in list(product_versions):
        ProdVer= PdtVersion(p.id,p.name,p.desc)
        #ProdVer.setProduct(p.product)
         #data['id']=p.id
        #data['name']=p.name
        dataList.append(ProdVer.to_json())
        
    #con.close()
    #dataList={'add': '1'}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp

class PdtVersion:
        def __init__(self, id, name, desc):
            self.name = name
            self.id = id
            self.desc=desc
        def setProduct(self,product):
            self.product=product;
        def __repr__(self):
            return self.name
        def __str__(self):
        #return self's name
            return self.name
        def to_json(self):
            json_data ={
                'id': self.id,
                'name': self.name,
                'desc': self.desc
            }
            return json_data
   
#@app.route('/product/add', methods = ['PUT'])
#def api_add_product():
#    
#    #go to  database via ORM and get the  products
#    #1.connect to database
#    #2.
#    #make JSON object out of products
#    con,meta =connect('postgres','adarsh1','quiver2')
#    # create a configured "Session" class
#    Session = sessionmaker(bind=con)
#    # create a Session
#    session = Session()
#    # query from a class
#    if 'name' in request.json:
#        name=request.json['name']
#    if 'desc' in request.json:
#        desc=request.json['desc']
#    if 'domain' in request.json:
#        domain=request.json['domain']
#    if 'business_seg' in request.json:
#        business_seg=request.json['business_seg']
#    
#    Pdt = Product(name=name,desc=desc,domain=domain,business_segment=business_seg) 
#    session.add(Pdt)
#    session.commit()
#    #con.close()
#    dataList={'add': '1'}
#    js = json.dumps(dataList)
#    resp = Response(js, status=200, mimetype='application/json')
#    resp.headers['Link'] = 'http://requirementstrrength.com'
#    return resp

@app.route('/requirements', methods = ['GET'])
def api_get_requirements():
    
    #go to  database via ORM and get the  products
    #1.connect to database
    #2.
    #make JSON object out of products
    con,meta =connect('postgres','adarsh1','quiver2')
    # create a configured "Session" class
    Session = sessionmaker(bind=con)
    # create a Session
    session = Session()
    # query from a class
    
    requirements=session.query(Requirement)
    #requirements =Requirement.get_requirements(con,meta)
    
    dataList =[]
    class dataPdt:
        def __init__(self, id, name):
            self.name = name
            self.id = id
        def __repr__(self):
            return self.name
        def __str__(self):
        #return self's name
            return self.name
        def to_json(self):
            json_data ={
                'id': self.id,
                'name': self.name
                
            }
            return json_data
            
    for p  in list(requirements):
        dataProd= dataPdt(p.id,p.name)
         #data['id']=p.id
        #data['name']=p.name
        dataList.append(dataProd.to_json())
    
    dataList={'list': dataList}
    js = json.dumps(dataList)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://requirementstrrength.com'
    return resp
        
app.run('0.0.0.0', 8080,debug=True ) 