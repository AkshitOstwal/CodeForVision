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

#print(d)

class glass:
    airtight=1
    moisture_resistance=1
    transparent=1
    photosensitivity_resistance=1
    flammable=0
    resist_solvents=1
    def single_layer(self):
        self.name="Single layer glass"
        self.thickness=0.102 #cm
        self.tensile_strength=10.2 #newton/m^2
        self.temperature=200 #degree celcius
        self.weightpercm2=0.6    #gm
        self.puncture_resistance=0.21 #pascle
        self.costpercm2=0.08      #in Rs

    def double_layer(self):
        self.name="Double layer glass"
        self.thickness=0.318
        self.tensile_strength=30.2
        self.temperature=300
        self.weightpercm2=1.4
        self.puncture_resistance=0.42
        self.costpercm2=0.12

    def triple_layer(self):
        self.name="Triple layer glass"
        self.thickness=0.417
        self.tensile_strength=65.2
        self.temperature=300
        self.weightpercm2=1.9
        self.puncture_resistance=0.72
        self.costpercm2=0.21

class aluminium():
    moisture_resistance=1
    photosensitivity_resistance=1
    resist_solvents=1
    flammable=0
    def single_layer(self):
        self.name="Single sheet aluminium"
        self.airtight=0
        self.thickness=0.08 # cm
        self.tensile_strength=4.2   #in netwon per m^2
        self.temperature=150 #celcius
        self.weightpercm2=0.02 #gm
        self.puncture_resistance=0.13 #pascle
        self.costpercm2=0.09  # in rs

    def double_layer(self):
        self.name="Double sheet aluminium"
        self.airtight=1
        self.thickness=0.18
        self.tensile_strength=11.2
        self.temperature=180
        self.weightpercm2=0.08
        self.puncture_resistance=0.36
        self.costpercm2=0.25

    def triple_layer(self):
        self.name="Triple sheet aluminium"
        self.airtight=1
        self.thickness=0.27
        self.tensile_strength=33.4
        self.temperature=180
        self.weightpercm2=0.12
        self.puncture_resistance=0.55
        self.costpercm2=0.40

class cardboard():
    airtight=0
    toxic=0
    moisture_resistance=0
    photosensitivity_resistance=1
    flamable=1
    resist_solvents=0

    def single_wall(self):
        self.name="Single wall cardboard"
        self.thickness=0.20
        self.tensile_strength=9.4
        self.temperature=130
        self.weightpercm2=0.15
        self.puncture_resistance=0.20
        self.costpercm2=0.17

    def double_wall(self):
        self.name="Double wall cardboard"
        self.thickness=0.35
        self.tensile_strength=15.1
        self.temperature=130
        self.weightpercm2=0.23
        self.puncture_resistance=0.24
        self.costpercm2=0.40

    def coated(self):
        self.name="Coated cardboard"
        self.thickness=0.10
        self.tensile_strength=8.1
        self.temperature=150
        self.weightpercm2=0.11
        self.puncture_resistance=0.16
        self.costpercm2=0.28
        self.airtight=1
        self.moisture_resistance=1

class plastic:
    def polyethylene(self):
        self.name="polyethylene"
        self.airtight=0
        self.moisture_resistance=0
        self.photosensitivity_resistance=0
        self.tensile_strength=1.1
        self.puncture_resistance=0.65
        self.temperature=90
        self.thickness=0.01
        self.weightpercm2=0.001
        self.costpercm2=0.005
        self.resist_solvents=1
        self.flamable=1

    def hdpe(self):
        self.name="High density polyethylene"
        self.airtight=1
        self.moisture_resistance=1
        self.photosensitivity_resistance=0
        self.tensile_strength=30.3
        self.puncture_resistance=0.73
        self.temperature=220
        self.thickness=0.82
        self.flamable=0
        self.weightpercm2=0.09
        self.costpercm2=0.43
        self.resist_solvents=1

    def ldpe(self):
        self.name="Low density polyethylene"
        self.airtight=1
        self.moisture_resistance=1
        self.photosensitivity_resistance=0
        self.tensile_strength=18.3
        self.puncture_resistance=0.49
        self.temperature=170
        self.flamable=0
        self.thickness=0.22
        self.weightpercm2=0.04
        self.costpercm2=0.17
        self.resist_solvents=1

    def polystyrene(self):
        self.name="polystyrene"
        self.airtight=1
        self.moisture_resistance=1
        self.photosensitivity_resistance=1
        self.tensile_strength=8.3
        self.puncture_resistance=0.18
        self.temperature=120
        self.flamable=0
        self.thickness=0.82
        self.weightpercm2=0.11
        self.costpercm2=0.09
        self.resist_solvents=1

    def pvc(self):
        self.name="Polyvinyl chloride"
        self.airtight=1
        self.moisture_resistance=1
        self.photosensitivity_resistance=1
        self.tensile_strength=38.3
        self.puncture_resistance=3.78
        self.temperature=320
        self.flamable=0
        self.thickness=0.92
        self.weightpercm2=0.36
        self.costpercm2=0.60
        self.resist_solvents=1

# if element is brittle then consider bubble wrap
#print("helloo world")
# starting with the cardboard
count=0
count_list=[]
c1=cardboard()
c2=cardboard()
c3=cardboard()
c1.single_wall()
c2.double_wall()
c3.coated()
p1=plastic()
p2=plastic()
p3=plastic()
p4=plastic()
p5=plastic()
p1.polyethylene()
p2.hdpe()
p3.ldpe()
p4.polystyrene()
p5.pvc()
l=[c1,c2,c3,p1,p2,p3,p4,p5]
count_list=[]
#for i in l:
#    print(i.thickness,end=" ")
for i in l:
    count=0
    if float(d["moisture"])==i.moisture_resistance:
        count+=1
    if float(d["Pressure"])<i.tensile_strength:
        count+=1
    if (d["odour"]==1 or d["o2"]==1) and i.airtight==1:
        count+=1
    if float(d["templimit"])<i.temperature:
        count+=1
    if d["flammable"]!=i.flamable:
        count+=1
    if d["photosensitive"]==i.photosensitivity_resistance:
        count+=1
    count_list.append([i,count])

#print(count_list)
