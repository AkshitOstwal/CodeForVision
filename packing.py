import math

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
                     l[i].append(l[i][1]*)#costpercm2)

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
                     # now the packing will come in the shape of the cylinder
                     width=2*r
                     height_of_packet=factor*2*r
                     len_of_packet=(thickness*pieces)/factor
                     package_area=2(len_of_packet*width+len_of_packet*height_of_packet+height_of_packet*width)
                     l.append([factor,packing_area])

              for i in range (len(l)):
                     l[i].append(l[i][1]*)#costpercm2
                                 
       def cuboidal():
              length=0
              width=0
              height=0
              area=2(length*width+length*height+height*width)
              volume=length*width*height
              packing_shape_cubodial(self,area,length,width,height)
              
       def cylinderical():
              radius=0
              thickness=0
              area=2*math.pi*r*thickness+2*math.pi*r**2
              volume=math.pi*r**2*thickness
              packing_shape_cylindrical(area,radius,thickness)

class flour:
       print("class for flour")

# the things which are reactive with oxygen would require the free packing, they are gonna get packed in the packet
# containing nitrogen so it means that the prodct wont be actually arranged in the particular pattern.

class bingo:
       print("class for bingo")
       
class Noodles:
       print("class for noodles")
       
