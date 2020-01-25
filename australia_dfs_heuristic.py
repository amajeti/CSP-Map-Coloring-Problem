#!/usr/bin/env python

import random
from Node import Node
import pdb
import time


colorlist = []


allstates = []
backtrack = 0

def pick_big_state(legal_colours):
    for k in sorted(legal_colours, key=lambda k: len(legal_colours[k]), reverse=True):
        #print k
        return k

def update_neighbors(statechanged,legal_colours,state_dict,color_assigned,states):
    for state in state_dict[statechanged]:
            #print(state)
            if color_assigned in list(filter(lambda x:x[0]==state,legal_colours))[0][1]:
                list(filter(lambda x:x[0]==state,legal_colours))[0][1].remove(color_assigned)


def init_colours(n):
    for i in range(n):
        colorlist.append(random.randint(0,255))

def generate_colours(states,i,num_colours,colours):
    t_list = []
    for j in range(num_colours):
        t_list.append(Node(colours[j],states[i]))

def getcolours(states,my_state_dict):
    list_col = []
    for i in states:
        list_col.append(my_state_dict.get(i,""))

    return list_col

    return t_list

def random_color(n):
    return tuple(colorlist)

def build_color_graph(num,numstates,states):
    colours = random_color(3)
    a = Node(colours[0],states[0])
    root = a
    my_states = {}
    for i in range(1,numstates,1):
        w = Node(colours[0],states[i])
        a.put_child(w)
        a.nextnode = w
        #a = w
        my_states[states[i]] = a

        for j in range(1,num,1):
            b = Node(colours[j])
            a.put_child(b)

        a = w

    print(root)
    print(root.next)
    print(root.next[1].next)

def init(states,state_dict,num_colours):
    colours = colorlist
    root = Node(colours[0],states[0])
    for j in range(num_colours):
        root.put_child(Node(colours[j],states[0]))

    return root


def dfs_heuristic_included(my_state_dict,state_dict,num_colours,currentstate,states,num,legal_colours):
    global backtrack
    allstates.append(my_state_dict.copy())
    for i in range(len(currentstate.next)):
        temp_legal_colours = legal_colours.copy()
        my_state_dict[currentstate.next[0].myname] = currentstate.next[i].mycolor

        if my_state_dict.get(currentstate.next[0].myname) in getcolours(state_dict[currentstate.next[0].myname],my_state_dict):
            #print("continued")
            continue
        if num == len(states) - 1:
            return 1,my_state_dict


        backtrack +=1
        update_neighbors(currentstate.next[0].myname,temp_legal_colours,state_dict,currentstate.next[i].mycolor,states)


        temp_legal_colours = sorted(temp_legal_colours,key=lambda x:len(x[1]))


        temp_colorlist = colorlist.copy()
        currentstate.next[i].next = generate_colours(states,num+1,num_colours,temp_colorlist)





        ans = dfs_heuristic_included(my_state_dict,state_dict,num_colours,currentstate.next[i],states,num+1,temp_legal_colours)
        if ans[0] == 1:
            return 1,my_state_dict

        continue

    return 0,my_state_dict



if __name__ == "__main__":
    num_colours = 4
    init_colours(num_colours)

    colorlist = ["red","blue","green","black"]

    legal_colours = []

    for state in states:
        legal_colours.append([state,colorlist.copy()])

    states=['wa','nt','q','nsw','v','sa']

    state_dict  ={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}


    my_state_dict = {}

    root = init(states,state_dict,num_colours)

    starttime = time.time()
    answer = dfs_heuristic_included(my_state_dict,state_dict,num_colours,root,states,0,legal_colours)

    endtime = time.time()
    count = 0
    for key in answer[1]:
        count+=1
        if answer[1][key] in getcolours(state_dict[key],my_state_dict):
            print("oops")


    time.sleep(10)
    print(answer)
    print("number of backtracks: "+ str(backtrack))
    print("Time taken: " + str(endtime - starttime) + "seconds")
