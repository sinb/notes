# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:34:08 2015

@author: hehe
"""

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
car_data = {
	"layout" : "rear mid-engine rear-wheel-drive layout",
	"name" : "Porsche Boxster",
	"productionYears" : [ ],
	"modelYears" : [ ],
	"bodyStyle" : "roadster",
	"assembly" : [
		"Finland",
		"Germany",
		"Stuttgart",
		"Uusikaupunki"
	],
	"class" : "sports car",
	"manufacturer" : "Porsche"
}
db = client.examples
db.autos.insert(car_data)