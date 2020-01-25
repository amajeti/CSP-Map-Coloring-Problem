#!/usr/bin/env python

import random
from Node import Node
import pdb
#from mapcolor import colormap
import time


colorlist = []

backtrack = 0

allstates = []
def init_colours(n):
    for i in range(n):
        colorlist.append(random.randint(0,255))

def random_colour(n):
    return tuple(colorlist)

def generatecols(states,i,number_of_colours,colours):
    t_list = []
    for j in range(number_of_colours):
        t_list.append(Node(colours[j],states[i]))

    return t_list

def getcolours(states,my_state_dict):
    list_col = []
    for i in states:
        list_col.append(my_state_dict.get(i,""))

    return list_col



def init(states,state_dict,number_of_colours):
    colours = colorlist
    root = Node(colours[0],states[0])
    for j in range(number_of_colours):
        root.put_child(Node(colours[j],states[0]))

    return root

def build_color_graph(num,numstates,states):
    colours = random_colour(3)
    a = Node(colours[0],states[0])
    root = a
    mystates = {}
    for i in range(1,numstates,1):
        w = Node(colours[0],states[i])
        a.put_child(w)
        a.nextnode = w
        #a = w
        mystates[states[i]] = a

        for j in range(1,num,1):
            b = Node(colours[j])
            a.put_child(b)

        #x.put_child(Node(colours[0],states[i]))
        a = w
            
    print(root)
    print(root.next)
    print(root.next[1].next)    

def forward_checking(my_state_dict,state_dict,number_of_colours,current_state,states,num):

    global backtrack
    allstates.append(my_state_dict.copy())
    for i in range(len(current_state.next)):
        time.sleep(0.000002)
        my_state_dict[current_state.next[0].myname] = current_state.next[i].mycolor   
        if my_state_dict.get(current_state.next[0].myname) in getcolours(state_dict[current_state.next[0].myname],my_state_dict):
            #print("continued")
            continue
   
        if num == len(states) - 1:
            return 1,my_state_dict

        temp_colorlist = colorlist.copy()
        remove_colours = getcolours(states[num+1],my_state_dict)
        temp_colorlist = [x for x in temp_colorlist if x not in remove_colours]
        current_state.next[i].next = generatecols(states,num+1,number_of_colours,temp_colorlist)
   

        ans = forward_checking(my_state_dict,state_dict,number_of_colours,current_state.next[i],states,num+1)
        if ans[0] == 1:
            return 1,my_state_dict

        continue
        
    backtrack +=1

    return 0,my_state_dict 



    



        


            
            
    
    
if __name__ == "__main__":
    number_of_colours = 4
    init_colours(number_of_colours)

    colorlist = ["red","blue","green","black"]


    
    states=['wa','nt','q','nsw','v','sa']

    state_dict  ={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}
    
   

    my_state_dict = {}


    print(states)

    root = init(states,state_dict,number_of_colours)

    starttime = time.time()
    answer = forward_checking(my_state_dict,state_dict,number_of_colours,root,states,0)
    endtime = time.time()
    count = 0 
    for key in answer[1]:
        count+=1
        if answer[1][key] in getcolours(state_dict[key],my_state_dict):
            print("oops")


    print("VERIFIED ANSWER")
    print(answer)
    print("NUMBER OF backtrack: "+ str(backtrack))
    print("TIME OF EXECUTION: " + str(endtime - starttime) + "seconds") 

    print(len(allstates))

#    for i in range(0,len(allstates),2000):
#        colormap(allstates[i])


#    colormap(my_state_dict)

    time.sleep(10)
    


