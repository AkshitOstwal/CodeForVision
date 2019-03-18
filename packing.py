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
print(db.get().val())
while True:
    if db.get().val()==None:
        continue
    else:
        users=db.get()

        import orientation
        import pyrebase
        import codebase
        from codebase import count_list as count_list
        from orientation import area
        from orientation import for_display
        count_list.sort(key=lambda x: x[1], reverse=True)
        #print(count_list)
        l=[]
        max=0
        sam=[]

        for j in count_list:
            if(j[1]> count_list[0][1]-3):
                sam.append(j)
        #print("sam ",sam)

        d={}
        for user in users.each():
            d[user.key()]=user.val()
        #print(d)
        l=[]
        class biscuit:

            def __init__(self):
                print("This is for the biscuit of cubodial shape")

            def packing_shape_cuboidal(self,length,width,height):
                for i in sam:
                    l.append([round(area[0][2]*i[0].costpercm2,2),i[0].name])

                l.sort(key=lambda x: x[1])

            def cuboidal(self):
                #print("Hello")
                length=float(d["length"])
                width=float(d["width"])
                height=float(d["height"])
                volume=length*width*height
                self.packing_shape_cuboidal(length,width,height)

        if __name__ == "__main__":

            obj1=biscuit()
            obj1.cuboidal()
            print(l)
            db.child("ans").child("js").set(l)
            db.child("ans2").child("area").set(for_display)

        break
