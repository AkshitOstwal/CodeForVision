import math
import orientation
import pyrebase
import codebase
from codebase import count_list as count_list
from orientation import area
config = {
  "apiKey": "AIzaSyByA7celafHSloxdOLA7_s-D097Ld10Jus",
  "authDomain": "firepack-66e50.firebaseapp.com",
  "databaseURL": "https://firepack-66e50.firebaseio.com",
  "projectId": "firepack-66e50",
  "storageBucket": "firepack-66e50.appspot.com"
}

count_list.sort(key=lambda x: x[1], reverse=True)
#print(count_list)

max=0
sam=[]

for j in count_list:
    if(j[1]> count_list[0][1]-3):
        sam.append(j)
print("sam ",sam)
firebase = pyrebase.initialize_app(config)

db = firebase.database()

users=db.get()
while(users.val()==None):
    pass
d={}
for user in users.each():
    d[user.key()]=user.val()
#print(d)

obj=""
rad=""
for user in users.each():
    if user.key()=="name":
        obj=user.val()
    if user.key()=="radius":
        rad=user.val()

class biscuit:
    l=[]
        #print("this is the packing procedure for biscuits")

    def packing_shape_cuboidal(self,area,length,width,height):

        for i in sam:
            l.append([sam[i],area[0][2]*sam[i].costpercm2])

        l.sort(key=lambda x: x[1])
        print(l)
'''

    def packing_shape_cylindrical(self,area,radius,thickness):
        l=[]
        for i in sam:
            pieces=launch_packet_weight/weight_of_object
            cost_to_pack_single=area*i[0].costpercm2 # + a small quantity
            factor=1
            length_of_packet=thickness*pieces
            package_area=math.pi*radius**2 *length_of_packet
            # when the packing is done in the shape of the object
            l.append([factor,packing_area,cost_to_pack_single])
            while factor<pieces:
                factor+=1
                # now the packing will come in the shape of the cuboid
                width=2*r
                height_of_packet=factor*2*r
                len_of_packet=(thickness*pieces)/factor
                package_area=2*(len_of_packet*width+len_of_packet*height_of_packet+height_of_packet*width)
                l.append([factor,packing_area])

        for i in range (len(l)):
                l[i].append(l[i][1]*i[0].costpercm2)

        l.sort(key=lambda x: x[2])
        #print("hello",l[0])
'''

    def cuboidal(self):
        #print("Hello")
        length=float(d["length"])
        width=float(d["width"])
        height=float(d["height"])
        area=2*(length*width+length*height+height*width)
        volume=length*width*height
        self.packing_shape_cuboidal(area,length,width,height)
'''
    def cylinderical(self):
        radius=float(d["radius"])
        thickness=float(d["thickness"])
        area=2*math.pi*r*thickness+2*math.pi*r**2
        volume=math.pi*r**2*thickness
        self.packing_shape_cylindrical(area,radius,thickness)
'''
if obj=="Biscuit":
    obj1=biscuit()
    obj1.cuboidal()