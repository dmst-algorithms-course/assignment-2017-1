#read the file
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("graph_file", help="Name of input file")
args = parser.parse_args()
#initial elements
nodes = []
dic = {}
# open the file
with open(args.graph_file) as graph_input:
    # make a list
    for line in graph_input:
        q = line.split()
        nodes.append(q)
        nodes.sort()
        # make a dictionary
counter1 = 0
for i in nodes:
    dic[counter1] = [i]
    counter1 = counter1 + 1

for k, v in dic.items():# for all the dictionary
    for pl in range(k): # for the current lines
        counter2 = 0
        for list in dic[pl]: # for my line
            if len(v) > 0:
                if v[0][0] in list: # if part1 in list
                    continue
                elif v[0][1] in list: # if part2 in list
                    continue
                else:
                    counter2 = counter2 + 1 # if nothing in list
                if counter2 == len(dic[pl]): # change the nodes & sort the dictionary
                    dic[pl].append(dic[k][0])
                    dic[k].remove(dic[k][0])
        if len(dic[k]) == 0:
            break
#new dictionary
dic2 = {}
count = 0
for k, v in dic.items():
    if len(v) > 0:
        dic2[count] = v
        count = count + 1
key=dic2.keys()
# make & print tuples
for v in nodes:
    for k in key:
        if (v in dic2[k]):
            print (tuple(v),k)
