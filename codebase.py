#!/usr/bin/env python3

import pyrebase

config = {
  "apiKey": "AIzaSyByA7celafHSloxdOLA7_s-D097Ld10Jus",
  "authDomain": "firepack-66e50.firebaseapp.com",
  "databaseURL": "https://firepack-66e50.firebaseio.com",
  "projectId": "firepack-66e50",
  "storageBucket": "firepack-66e50.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

users=db.get()
#print(users.val())

#for user in users.each():
#    print(user.val())

d={}
for user in users.each():
    d[user.key()]=user.val()

print(d)

class glass:
    airtight=1
    moisture_resistance=1
    transparent=1
    photosensitivity_resistance=1
    flammable=0
    resist_solvents=1
    def single_layer(self):
        thickness=0.102 #cm
        tensile_strength=10.2 #newton/m^2
        temperature=200 #degree celcius
        weightpercm2=0.6    #gm
        puncture_resistance=0.21 #pascle
        costpercm2=0.08      #in Rs

    def double_layer(self):
        thickness=0.318
        tensile_strength=30.2
        temperature=300
        weightpercm2=1.4
        puncture_resistance=0.42
        costpercm2=0.12

    def triple_layer(self):
        thickness=0.417
        tensile_strength=65.2
        temperature=300
        weightpercm2=1.9
        puncture_resistance=0.72
        costpercm2=0.21

class aluminium():
    moisture_resistance=1
    photosensitivity_resistance=1
    resist_solvents=1
    flammable=0
    def single_layer(self):
        airtight=0
        thickness=0.08 # cm
        tensile_strength=4.2   #in netwon per m^2
        temperature=150 #celcius
        weightpercm2=0.02 #gm
        puncture_resistance=0.13 #pascle
        costpercm2=0.09  # in rs

    def double_layer(self):
        airtight=1
        thickness=0.18
        tensile_strength=11.2
        temperature=180
        weightpercm2=0.08
        puncture_resistance=0.36
        costpercm2=0.25

    def triple_layer(self):
        airtight=1
        thickness=0.27
        tensile_strength=33.4
        temperature=180
        weightpercm2=0.12
        puncture_resistance=0.55
        costpercm2=0.40

class cardboard():
    airtight=0
    toxic=0
    moisture_resistance=0
    photosensitivity_resistance=1
    flamable=1
    resist_solvents=0

    def single_wall(self):
        thickness=0.20
        tensile_strength=9.4
        temperature=130
        weightpercm2=0.15
        puncture_resistance=0.20
        costpercm2=0.17

    def double_wall(self):
        thickness=0.35
        tensile_strength=15.1
        temperature=130
        weightpercm2=0.23
        puncture_resistance=0.24
        costpercm2=0.40

    def coated():
        thickness=0.10
        tensile_strength=8.1
        temperature=150
        weightpercm2=0.11
        puncture_resistance=0.16
        costpercm2=0.28
        airtight=1
        moisture_resistance=1

class plastic:
    def polyethylene():
        airtight=0
        moisture_resistance=0
        photosensitivity_resistance=0
        tensile_strength=1.1
        puncture_resistance=0.65
        temperature=90
        thickness=0.01
        weightpercm2=0.001
        costpercm2=0.005
        resist_solvents=1
        flamable=1

    def hdpe():
        airtight=1
        moisture_resistance=1
        photosensitivity_resistance=0
        tensile_strength=30.3
        puncture_resistance=0.73
        temperature=220
        flamable=0
        thickness=0.82
        weightpercm2=0.09
        costpercm2=0.43
        resist_solvents=1

    def LDPE():
        airtight=1
        moisture_resistance=1
        photosensitivity_resistance=0
        tensile_strength=18.3
        puncture_resistance=0.49
        temperature=170
        flamable=0
        thickness=0.22
        weightpercm2=0.04
        costpercm2=0.17
        resist_solvents=1

    def polystyrene():
        airtight=1
        moisture_resistance=1
        photosensitivity_resistance=1
        tensile_strength=8.3
        puncture_resistance=0.18
        temperature=120
        flamable=0
        thickness=0.82
        weightpercm2=0.11
        costpercm2=0.09
        resist_solvents=1

    def pvc():
        airtight=1
        moisture_resistance=1
        photosensitivity_resistance=1
        tensile_strength=38.3
        puncture_resistance=3.78
        temperature=320
        flamable=0
        thickness=0.92
        weightpercm2=0.36
        costpercm2=0.60
        resist_solvents=1

# if element is brittle then consider bubble wrap
print("helloo world")
# starting with the cardboard
count=0
count_list=[]
c1=cardboard()
c1.single_wall()
if d["pressure"]<c1.tensile_strength:
    count+=1
if d["moisture"]==c1.moisture_resistance:
    count+=1
if (d["odour"]==1 or d["o2"]==1) and c1.airtight==1:
    count+=1
if d["temperature"]<c1.temperature:
    count+=1
