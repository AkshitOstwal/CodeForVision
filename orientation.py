import pyrebase
import sympy
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


def print_factors(x):
    factors=[]
    for i in range(1, x ):
        if x % i == 0:
            factors.append(i)
    return factors

launch_packet_weight=int(d["launch"])
weight_of_one =int(d["weight"])
no_of_biscuits=int(launch_packet_weight/weight_of_one)
if sympy.isprime(no_of_biscuits) and no_of_biscuits>20:
    print("This is a prime number which will not provide a feasible solution")
else:
    factors=print_factors(no_of_biscuits)
#print(factors)
area=[]
flag=0
if d['radius']=='':
    flag=1
    #print("Biscuits are cuboidal ")
    h=float(d['height'])
    h=round(h,2)
    l=float(d['length'])
    l=round(l,2)
    w=float(d["width"])
    w=round(w,2)
else :
    r=float(d["radius"])
    r=round(r,2)
    t=float(d['thickness'])
    t=round(t,2)

for i in range (0,len(factors)):
    repeated_list=[]
    biscit_in_one_column=no_of_biscuits/factors[i]
    length=biscit_in_one_column*h
    breath=factors[i]*l
    height=w
    if factors[i]%2==0 and sympy.isprime(factors[i])==0:
        #print(factors[i])
        repeated_list=print_factors(factors[i])
        #print(repeated_list)
        repeated_list=repeated_list[1:]
        for k in repeated_list:
            w1=w*factors[i]/k
            h1=w*k
            #print("layers ",k ," ", "columns ", factors[i]/k," " ,2*(w1*h1+w1*length+h1*length))
            area.append([factors[i],k,2*(w1*h1+w1*length+h1*length)])
        #print(repeated_list)
    area.append([factors[i],1,2*(length*breath+length*height+breath*height)])

area.sort(key=lambda x: x[2])
for_display=[]
for i in area:
    column=i[0]/i[1]
    layer=i[1]
    Total =no_of_biscuits/(column*layer)
    for_display.append("column "+ str(column) + " " + "layers " +str(layer) + " " + "Total area " +str(i[2])+" "+ "No. of biscits per packet "+ str(Total)+"\n")

print(*for_display,sep="\n")
