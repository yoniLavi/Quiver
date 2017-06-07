# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:59:34 2017

@author: abhilash
"""

# for  rendering 
from flask import render_template, session, redirect, url_for
from .import main


#Views
# for Rendering Pages:

@main.route('/index', methods=['GET','POST'])
def render_index():
    return render_template('index.html')
