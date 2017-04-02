import sys


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of input file")
args = parser.parse_args()
f= sys.argv[1]
agones=[]
with open(f) as graph1:
    for line in graph1:
        temp=[]
        i=0
        for x in line.split():
            if i==1: 
               temp.append(x)
            if i<1: 
               i=i+1
               temp.append(x)
        agones.append(temp)
day=0
agones_teliko=[]

while len(agones)>0:
    k=0
    daylist=[]
    for i in range(len(agones)):
        if k>0:
            flag=False
            for l in daylist:
                if agones[i][0] in l or agones[i][1] in l:
                    flag=True



            if flag==False:
                temp=[]
                temp.append(agones[i])
                temp.append(day)
                daylist.append(agones[i])
                agones_teliko.append(temp)
                
                    
        if k==0:
            temp=[]
            temp.append(agones[i])
            temp.append(day)
            daylist.append(agones[i])
            agones_teliko.append(temp)
            k= k +1
        
    day= day+1
    
    for i in daylist:
        
        agones.remove(i)
    daylist=[]
agones_teliko.sort(key=lambda x: x[0])

for i in range(len(agones_teliko)):
    print("(",agones_teliko[i][0][0],", ",agones_teliko[i][0][1],") ",agones_teliko[i][1])
                   
          
               
                


            

        
