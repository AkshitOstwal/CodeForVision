import math
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
d={}
for user in users.each():
    d[user.key()]=user.val()
print(d)

obj=""
rad=""
for user in users.each():
    if user.key()=="name":
        obj=user.val()
    if user.key()=="radius":
        rad=user.val()

launch_packet_weight=50
weight_of_object=5

class biscuit:
    def __init__(self):
        print("this is the packing procedure for biscuits")
    def packing_shape_cubodial(self,area,length,width,height):
        pieces=launch_packet_weight/weight_of_object
        # height is the thickness of biscuit here
        l=[]
        cost_to_pack_single=area*#costpercm2 of material + #a small quantity
        factor=1
        height_of_packet=width
        len_of_packet=height*pieces
        # this is the area of the package when we are packaging
        # the object in the shape similar to the shape of object
        package_area=2(len_of_packet*width+len_of_packet*height_of_packet+height_of_packet*width)
        l.append([1,package_area])
        while factor<pieces:
            factor+=1
            height_of_packet=width*factor
            len_of_packet=(height*pieces)/factor
            package_area=2(len_of_packet*width+len_of_packet*height_of_packet+height_of_packet*width)
            print(package_area)
            l.append([factor,package_area])
              # for cost
            for i in range(len(l)):
                l[i].append(l[i][1]*)#costpercm2

    def packing_shape_cylindrical(self,area,radius,thickness):
        pieces=launch_packet_weight/weight_of_object
        l=[]
        cost_to_pack_single=area*costpercm2 # + a small quantity
        factor=1
        length_of_packet=thickness*pieces
        package_area=math.pi*radius**2*length_of_packet
        # when the packing is done in the shape of the object
        l.append([factor,packing_area])
        while factor<pieces:
            factor+=1
            # now the packing will come in the shape of the cuboid
            width=2*r
            height_of_packet=factor*2*r
            len_of_packet=(thickness*pieces)/factor
            package_area=2(len_of_packet*width+len_of_packet*height_of_packet+height_of_packet*width)
            l.append([factor,packing_area])

            for i in range (len(l)):
                l[i].append(l[i][1]*)#costpercm2

    def cuboidal():
        length=int(d["length"])
        width=int(d["width"])
        height=int(d["thickness"])
        area=2(length*width+length*height+height*width)
        volume=length*width*height
        packing_shape_cubodial(self,area,length,width,height)

    def cylinderical():
        radius=int(d["radius"])
        thickness=int(d["thickness"])
        area=2*math.pi*r*thickness+2*math.pi*r**2
        volume=math.pi*r**2*thickness
        packing_shape_cylindrical(area,radius,thickness)

if obj=="Biscuit":
    obj1=biscuit()
    if rad=="":
        obj1.cuboidal(self)
    else:
        obj1.cylinderical(self)


class floor:
       print("class for floor")

# the things which are reactive with oxygen would require the free packing, they are gonna get packed in the packet
# containing nitrogen so it means that the prodct wont be actually arranged in the particular pattern.

class bingo:
       print("class for bingo")

class Noodles:
       print("class for noodles")
