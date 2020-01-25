#!/usr/bin/env python

import random
from Node import Node
import pdb
import time

#!/usr/bin/env python

import random
from Node import Node
import pdb
import time


all_cols = []
states_full = []
backtracks = 0

def find_rand_color(n):
    return tuple(all_cols)

def initialize_cols(n):
    for i in range(n):
        all_cols.append(random.randint(0,255))

def color_what(states,mysdict):
    listcol = []
    for i in states:
        listcol.append(mysdict.get(i,""))

    return listcol

def build_graph(num,numstates,states):
    colors = find_rand_color(3)
    a = Node(colors[0],states[0])
    root = a
    mystates = {}
    for i in range(1,numstates,1):
        w = Node(colors[0],states[i])
        a.put_child(w)
        a.nextnode = w
        mystates[states[i]] = a

        for j in range(1,num,1):
            b = Node(colors[j])
            a.put_child(b)


        a = w


def init(states,statedict,numcolors):
    colors = all_cols
    root = Node(colors[0],states[0])
    for j in range(numcolors):
        root.put_child(Node(colors[j],states[0]))

    return root


def gen_cols(states,i,numcolors,colors):
    tlist = []
    for j in range(numcolors):
        tlist.append(Node(colors[j],states[i]))

    return tlist

def dfs_heuristic_included(mysdict,statedict,numcolors,currentstate,states,num,legal_colors):
    global backtracks
    all_states.append(mysdict.copy())
    for i in range(len(currentstate.next)):
        temp_legal_colors = legal_colors.copy()
        mysdict[currentstate.next[0].myname] = currentstate.next[i].mycolor

        if mysdict.get(currentstate.next[0].myname) in getcolors(statedict[currentstate.next[0].myname],mysdict):
            #print("continued")
            continue
        if num == len(states) - 1:
            return 1,mysdict


        backtracks +=1
        update_neighbors(currentstate.next[0].myname,temp_legal_colors,statedict,currentstate.next[i].mycolor,states)


        temp_legal_colors = sorted(temp_legal_colors,key=lambda x:len(x[1]))


        temp_colorlist = colorlist.copy()
        currentstate.next[i].next = generate_colors(states,num+1,numcolors,temp_colorlist)





        sol = dfs_heuristic_included(mysdict,statedict,numcolors,currentstate.next[i],states,num+1,temp_legal_colors)
        if sol[0] == 1:
            return 1,mysdict

        continue

    return 0,mysdict

if __name__ == "__main__":
    numcolors = 4
    initialize_cols(numcolors)
    all_cols = ["red","blue","green","black"]


    states=['wa','nt','q','nsw','v','sa']

    statedict  ={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}

    mysdict = {}
    root = init(states,statedict,numcolors)

    start_time = time.time()
    solution = dfs(mysdict,statedict,numcolors,root,states,0)

    for key in solution[1]:
        if solution[1][key] in color_what(statedict[key],mysdict):
            print("failed")

    end_time = time.time()


    print(solution)

    print("backtrack count: "+ str(backtracks))
    print("time taken: " + str(end_time - start_time) + "seconds")
