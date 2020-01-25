#!/usr/bin/env python

#Australia Heuristics

import random
from Node import Node
import pdb
#from mapcolor import colormap
import time


colour_list = []


all_states = []
backtrack = 0

def getcolors(states,my_state_dict):
    list_col = []
    for i in states:
        list_col.append(my_state_dict.get(i,""))

    return list_col

def update_neighbors(state_changed,legalcolours,state_dict,colourassigned,states):
    for state in state_dict[state_changed]:
            #print(state)
            if colourassigned in list(filter(lambda x:x[0]==state,legalcolours))[0][1]:
                list(filter(lambda x:x[0]==state,legalcolours))[0][1].remove(colourassigned)


def pick_big_state(legalcolours):
    for k in sorted(legalcolours, key=lambda k: len(legalcolours[k]), reverse=True):
        return k


def random_color(n):
    return tuple(colour_list)


def init_colors(n):
    for i in range(n):
        colour_list.append(random.randint(0,255))

def generate_colors(states,i,num_colour,colors):
    t_list = []
    #colors = random_color(num_colour)
    for j in range(num_colour):
        t_list.append(Node(colors[j],states[i]))

    return t_list

def build_color_graph(num,numstates,states):
    colors = random_color(3)
    a = Node(colors[0],states[0])
    root = a
    my_states = {}
    for i in range(1,numstates,1):
        w = Node(colors[0],states[i])
        a.put_child(w)
        a.nextnode = w
        #a = w
        my_states[states[i]] = a

        for j in range(1,num,1):
            b = Node(colors[j])
            a.put_child(b)

        a = w
            
    print(root)
    print(root.next)
    print(root.next[1].next)


def init(states,state_dict,num_colour):
    colors = colour_list
    root = Node(colors[0],states[0])
    for j in range(num_colour):
        root.put_child(Node(colors[j],states[0]))

    return root


def heuristic_included(my_state_dict,state_dict,num_colour,current_state,states,num,legalcolours):
    global backtrack
    #pdb.set_trace()
    #colormap(my_state_dict)
    all_states.append(my_state_dict.copy())
    for i in range(len(current_state.next)):
        temp_legalcolours = legalcolours.copy()
        my_state_dict[current_state.next[0].myname] = current_state.next[i].mycolor   

        if my_state_dict.get(current_state.next[0].myname) in getcolors(state_dict[current_state.next[0].myname],my_state_dict):
            #print("continued")
            continue

        #my_state_dict[current_state.next[0].myname] = current_state.next[i].mycolor   
        if num == len(states) - 1:
            return 1,my_state_dict

        
        backtrack +=1
        update_neighbors(current_state.next[0].myname,temp_legalcolours,state_dict,current_state.next[i].mycolor,states)
        #big_statename = pick_big_state(legalcolours)
        
        temp_legalcolours = sorted(temp_legalcolours,key=lambda x:len(x[1]))



        #swap_ind = states.index(big_statename)

        #states[num+1],states[swap_ind] = states[swap_ind],states[num+1]


        temp_colour_list = colour_list.copy()
        remove_colors = getcolors(temp_legalcolours[num+1][0],my_state_dict)
        #temp_colour_list = temp_colour_list - remove_colors
        temp_colour_list = [x for x in temp_colour_list if x not in remove_colors]
        current_state.next[i].next = generate_colors(states,num+1,num_colour,temp_colour_list)


        #my_state_dict[current_state.next[i].next[0].myname] =   







        ans = heuristic_included(my_state_dict,state_dict,num_colour,current_state.next[i],states,num+1,temp_legalcolours)
        if ans[0] == 1:
            return 1,my_state_dict

        continue

    return 0,my_state_dict 





            
            
    
    
if __name__ == "__main__":
    num_colour = 3
    init_colors(num_colour)

    colour_list = ["red","blue","green","black"]


    legalcolours = []

    for state in states:
        legalcolours.append([state,colour_list.copy()])


    
    states=['wa','nt','q','nsw','v','sa']

    state_dict  ={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}

    
    my_state_dict = {}

    #print(states)
    root = init(states,state_dict,num_colour)

    starttime = time.time()
    answer = heuristic_included(my_state_dict,state_dict,num_colour,root,states,0,legalcolours)

    endtime = time.time()
    count = 0 
    for key in answer[1]:
        count+=1
        if answer[1][key] in getcolors(state_dict[key],my_state_dict):
            print("failed")



    print(len(all_states))


    print(answer)
    print("backtrack count: "+ str(backtrack))
    print("time taken: " + str(endtime - starttime) + "seconds") 

    



