#/usr/bin/env python3

from  sklearn  import  tree
 
# creating dataset for aluminium/plastic/glass/cardboard/paper

# we are calculating moisture/pressure/mouldable/recyclable/transparent
#/flexible/tearable/temperature/corrosion/lightweight/heatsealable/airtight
#/flammable/photosensitivity/rxnwitho2/costpercm2/toxic
#puncture_resistance/elasticity/weight 

features=[[1,10.2,0,1,1,0,0,200,0,0,1,1,0,1,1,15,0,50,0,20.4],[1,30.2,0,1,1,0,0,300,0,0,1,1,0,1,1,25,0,75,0,30.4],[1,45.2,0,1,1,0,0,300,0,0,1,1,0,1,1,25,0,90,0,50.4],[1,4.2,0,1,0,1,0,150,1,0,0,0,0,0,0,0.15,1,8,0,3.4],[1,10.2,0,1,0,0,0,300,1,0,0,1,0,0,0,0.25,1,16,0,6.8],[1,20.2,0,1,0,0,0,300,1,0,0,1,0,0,0,0.40,1,25,0,9.4],[]]
label=["singlelayerglass","doublelayerglass","triplelayerglass","singlelayeraluminium","doublelayeraluminium","triplelayeraluminium",""]

# now calling  decision tree algo
algo=tree.DecisionTreeClassifier()
# time for training data
trained=algo.fit(features,label)

# now prediction 
output=trained.predict([[0,42,0,1,1,0,0,400,0,1,1,1,0,1,0,20,0,14,0,12]])
print(output)
