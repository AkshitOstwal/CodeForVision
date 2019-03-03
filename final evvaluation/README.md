# **Team CodeForVision**
## **Project name** <!---to be given-->

### Problem Statement :
Packaging format for food products need to be designed based on a simulation model.
This model should involve a multi body dynamics study to evaluate the maximum forces the final packaged food will be subject to during transit and handling.
A simulation has to be done basis forces that products undergo during the journey in the supply chain.

### Solution :
We are making a website and a desktop application that we take input parameters like :
Dimensions,State of product,Chemical properties,Durability of product,packaging material specified(ex. Tetrapack),etc of product.
[Full List](https://github.com/AkshitOstwal/CodeForVision/tree/Pre-release#constraints-and-factors-on-which-packaging-depends-on)
<!---change the link once it it added to master -->
We will use Machine Learning algorithm and\or network with these factors as a key properties with different weightage to get the lowest cost and maximum durability of the packaging.
The output dimensions, material and packaging decided by the algorithm will be used to simulate the packaging for testing and damage calculation purposes.

#### phase 1:
1. Make forntend of website.
1. Implementation of backend frameworks.
1. Either get data set from ITC or create a demo data set
1. Making the ML algorithm

 #### phase 2:
 
1. Making of Android App that will create database in Firebase by extracting contents for food packets.
1. Using ML KIT in Firebase.
1. Generate a script that will fetch json data from firebase to show data in the WebApp.
## Constraints and factors on which packaging depends on:
* Solid
    * all properties
       * Dimensions
       * Orientation of product
       * Fragile nature
       * Durability / use before
    * Manufacturing state
       * Powder
       * etc
    * Packaging Materials
       * Plastic
       * Cardboard
       * Metal / Tin
       * Glass
    * Costing 
       * Plastic :
       * Cardboard :
       * any other : 
    * etc
* Liquid

### **Important Links**
[Food Dynamics](http://www.ift.org/knowledge-center/read-ift-publications/science-reports/scientific-status-summaries/food-packaging.aspx)
 
# In the file of the COdebase.py there is the arbitary data of the material properties. 
# In the file of orientation.py ther is the logic of the orientation and area optimization. 
# In the file of packing.py there is the logic of the cost optmization, in this file we got to know the best material for the packing, minimum area of packing material, strength of the arrangement in the carboard box, lowest cost of the material and lightest weight. Material will     
