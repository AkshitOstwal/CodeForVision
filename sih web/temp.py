#/usr/bin/env python3

from  sklearn  import  tree
 
# creating dataset for aluminium/plastic/glass/cardboard/paper

#airtight
#recyclable
#toxic
#moisture_resistance
#flexible
#aandb_resist
#transparent
#photosensitivity_resistance
#flammable
#resist_solvents
#thickness
#tensile_strength
#temperature
#weightpercm2
#puncture_resistance
#costpercm2


features=[[1,1,0,1,0,1,1,1,0,1,0.102,10.2,200,0.6,0.21,0.08],[1,1,0,1,0,1,1,1,0,1,0.318,30.2,300,1.4,0.42,0.12],[1,1,0,1,0,1,1,1,0,1,0.417,65.2,300,1.9,0.72,0.21],[0,1,0,1,1,0,0,1,0,1,0.08,4.2,150,0.02,0.13,0.09],[1,1,0,1,1,1,0,1,0,1,0.18,11.2,180,0.08,0.36,0.25],[1,1,0,1,0,1,0,1,0,1,0.27,33.4,180,0.12,0.55,0.40],[0,1,0,0,1,0,0,1,1,0,0.09,4.2,90,0.03,0.14,0.04],[0,1,0,0,1,0,0,1,1,0,0.15,6.9,110,0.09,0.17,0.10],[0,1,0,0,0,0,0,1,1,0,0.20,9.4,130,0.15,0.20,0.17],[0,1,0,0,0,0,0,1,1,0,0.20,9.4,130,0.15,0.35,15.1,130,0.23,0.24,0.40],[1,1,0,1,1,0,0,1,1,1,0.10,8.1,150,0.11,0.16,0.28],[0,1,0,0,1,0,1,0,1,1,0.01,1.1,90,0.001,0.65,0.005],[1,1,0,1,0,1,1,0,0,1,0.82,30.2,220,0.09,0.73,0.43],[1,1,0,1,1,1,1,0,0,1,0.22,18.3,170,0.04,0.49,0.17],[1,1,0,1,0,0,0,1,0,1,0.82,8.3,120,0.11,0.18,0.09],[1,1,0,1,0,0,0,1,0,1,0.92,38.3,320,0.36,3.78,0.60]]

label=["singlelayerglass","doublelayerglass","triplelayerglass","singlelayeraluminium","doublelayeraluminium","triplelayeraluminium","single_faced"
,"double_faced","single_wall","double_wall","coated","polyethylene","hdpe","LDPE","polystyrene","pvc"]

# now calling  decision tree algo
algo=tree.DecisionTreeClassifier()
# time for training data
trained=algo.fit(features,label)

# now prediction 
output=trained.predict([[]])
print(output)
