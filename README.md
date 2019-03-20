# **Optimal Solution for food Packaging**
## **Perfect Package**

### Origin of project:
This project is based on the problem statement provided by ITC (Indian Tobacco Company) in Smart India Hackathon 2019.
### Problem Statement :
YouTube link to the problem statement is [this](https://www.youtube.com/watch?v=miscGsDFmE0).
Packaging format for food products need to be designed based on a simulation model.
This model should provide the optimum results for the packing of the product mostly cost.
A simulation has to be done basis forces that products undergo during the journey in the supply chain.

### Solution :
A website in which the properties of the objects will be taken as an input and then select the best suitable material for that in which
object can sustain much longer also the most optimum orientation and design of the product which can minimize the area of packing.
In this whole process the cost optimization is the prime objective.

#### Stage 1:
- [x] 1. Make front end of website.
- [x] 2. Implementation of backend frameworks.
- [x] 3. Either get data set from ITC or create a demo data set.
- [x] 4. Prepare 'codebase.py' file. In this file there should be the demo dataset of some materials which are commonly used for packaging.

#### Stage 2:
- [x] A website that will take the inputs of the certain properties of the object from the user, store it in database and compare with the package material which is best suitable for that object.
This comparison is done between the data which is pre-loaded in file `codebase.py` and the user inputs. After a careful analysis of the properties of packing material which suits the object, a list is generated of suitable materials.
All the data in `codebase.py` is arbitary and random, real data can be used in the code to get the exact results.
Getting the data from the firebase using `pyrebase`.
<strong>Properties which are taken as an input from the users are: </strong>
   * Dimensions
   * State of product
   * Chemical properties
      * Reaction with oxygen
      * Photosensitive, etc.
   * Durability of product
   * Packaging material specified(ex. Tetrapack), etc.
   <br>
<strong>Constraints and factors on which packaging depends on:</strong>
For Solid:

    * All properties
      * Dimensions
      * Orientation of product
      * Fragile nature
      * Durability / use before, etc.
    * Manufacturing state
      * Powder
      * etc.
    * Packaging Materials
      * Plastic
      * Cardboard
      * Metal / Tin
      * Glass
    * Costing
      * Plastic
      * Cardboard
      * any other
    * etc.

The scope of this project is limited to the solid objects (mainly biscuit) but can be extended to the other objects as well.
For more information, please refer [this](https://github.com/AkshitOstwal/CodeForVision/issues/6)

#### Stage 3:

- [x] 1. Code `orientation.py`.
- [x] 2. Design an algorithm which will test all the possible arrangements of the object in the packing packet and then return the one which is occupies minimum surface area and is also durable.  
- [x] 3. Generate the best possible arrangement of product inside the packing, determine shape and surface area of the packing.
- [x] 4. Making front End for the results page.
- [x] 5. Making javascript for the processing page.

#### Stage 4:

- [x] 1. Code `packing.py`
- [x] 2. Now link the cost and properties of each material in `codebase.py` and the defined the best possible orientation with a logic in which we find out the most optimum packaging of the object.
- [x] 3. In that file we will link the codebase.py , orientation.py. From these files we find out the areas of all possible orientations and the best materials used for the objects.
- [x] 5. Linking the firebase and the python file.
- [x] 6. Importing the files `codebase.py` and `orientation.py` in `packing.py`.
- [x] 7. Sending data in the form of list from packing.py to the firebase and then from to the website.


### How to Execute the Project

* Install python3 in your system, for reference you can go through [this](https://docs.python-guide.org/starting/install3/linux/)
* In this project, the `packing.py` works as a server, which is needed to get started before running the website.

<strong> Steps to Run project </strong>
<ol>
  <li> Clone the repository in your local machine $ git clone repo_link </li>
  <li> Run the file packing.py , python3 packing.py .</li>
  <li> Open index.html.</li>
  <li> click on primary packing button.</li>
  <li> Enter the details of the product biscuit. </li>
  <li> Wait for the output. </li>
  <li> It will provide us with the cost and material of the product packing. It also gives us all the possible combinations and orientations of the product packing. </li> 
</ol>
    
### **Important Links**
[Food Dynamics](http://www.ift.org/knowledge-center/read-ift-publications/science-reports/scientific-status-summaries/food-packaging.aspx)
