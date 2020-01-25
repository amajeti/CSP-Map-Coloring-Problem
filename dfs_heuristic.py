#!/usr/bin/env python

import random
from Node import Node
import pdb
from mapcolor import colormap
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



    state_dict = {
'Alabama':['Florida', 'Georgia', 'Mississippi', 'Tennessee'],
'Arizona':['California', 'Colorado', 'Nevada', 'New Mexico', 'Utah'],
'Arkansas' :['Louisiana', 'Mississippi', 'Missouri', 'Oklahoma', 'Tennessee', 'Texas'],
'California':['Arizona', 'Nevada', 'Oregon'],
'Colorado':['Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Utah', 'Wyoming'],
'Connecticut':['Massachusetts', 'New York', 'Rhode Island'],
'Delaware':['Maryland', 'New Jersey', 'Pennsylvania'],
'Florida':['Alabama', 'Georgia'],
'Georgia':['Alabama', 'Florida', 'North Carolina', 'South Carolina', 'Tennessee'],
'Idaho':['Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
'Illinois':['Indiana','Iowa', 'Michigan', 'Kentucky', 'Missouri', 'Wisconsin'],
'Indiana':['Illinois', 'Kentucky', 'Michigan', 'Ohio'],
'Iowa': ['Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota', 'Wisconsin'],
'Kansas' :['Colorado', 'Missouri', 'Nebraska', 'Oklahoma'],
'Kentucky':['Illinois', 'Indiana', 'Missouri', 'Ohio', 'Tennessee', 'Virginia', 'West Virginia'],
'Louisiana':['Arkansas', 'Mississippi', 'Texas'],
'Maine':["New Hampshire"],
"Maryland":['Delaware','Pennsylvania','Virginia', 'West Virginia'],
'Massachusetts':['Connecticut', 'New Hampshire', 'New York', 'Rhode Island', 'Vermont'],
'Michigan':['Illinois', 'Indiana', 'Minnesota', 'Ohio', 'Wisconsin'],
'Minnesota':['Iowa', 'Michigan', 'North Dakota', 'South Dakota', 'Wisconsin'],
'Mississippi':['Alabama', 'Arkansas', 'Louisiana', 'Tennessee'],
'Missouri':['Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma', 'Tennessee'],
'Montana':['Idaho', 'North Dakota', 'South Dakota', 'Wyoming'],
'Nebraska' :['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming'],
'Nevada':['Arizona', 'California', 'Idaho', 'Oregon', 'Utah'],
'New Hampshire': ['Maine', 'Massachusetts', 'Vermont'],
'New Jersey':["Delaware", "New York", "Pennsylvania"],
'New Mexico':['Arizona', 'Colorado', 'Oklahoma', 'Texas', 'Utah'],
'New York':['Connecticut', 'Massachusetts', 'New Jersey', 'Pennsylvania', 'Rhode Island', 'Vermont'],
'North Carolina':['Georgia', 'South Carolina', 'Tennessee', 'Virginia'],
'North Dakota':['Minnesota', 'Montana', 'South Dakota'],
'Ohio':['Indiana', 'Kentucky', 'Michigan', 'Pennsylvania', 'West Virginia'],
'Oklahoma' :['Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico', 'Texas'],
'Oregon':["California", 'Idaho', 'Nevada', "Washington"],
'Pennsylvania':['Delaware', 'Maryland', 'New Jersey', 'New York', 'Ohio', 'West Virginia'],
'Rhode Island':['Connecticut', 'Massachusetts', 'New York'],
'South Carolina':['Georgia', 'North Carolina'],
'South Dakota':['Iowa', 'Minnesota', 'Montana', 'Nebraska', 'North Dakota', 'Wyoming'],
'Tennessee':['Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'North Carolina', 'Virginia'],
'Texas':['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma'],
'Utah':['Arizona', 'Colorado', 'Idaho', 'Nevada', 'New Mexico', 'Wyoming'],
'Vermont':['Massachusetts', 'New Hampshire', 'New York'],
'Virginia':['Kentucky', 'Maryland', 'North Carolina', 'Tennessee', 'West Virginia'],
'Washington':['Idaho', 'Oregon'],
'West Virginia':['Kentucky', 'Maryland', 'Ohio', 'Pennsylvania', 'Virginia'],
'Wisconsin':['Illinois', 'Iowa', 'Michigan', 'Minnesota'],
'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah']
}

    states = ['Alabama','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine',"Maryland",'Massachusetts',
        'Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
        'Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']


    states = ['Maine', 'Minnesota', 'South Dakota', 'Illinois', 'Utah', 'Wyoming', 'Texas', 'Idaho', 'Wisconsin', 'Connecticut', 'Pennsylvania', 'Kansas', 'West Virginia', 'North Carolina', 'Colorado', 'California', 'Florida', 'Vermont', 'Virginia', 'North Dakota', 'Michigan', 'New Jersey', 'Nevada', 'Arkansas', 'Mississippi', 'Iowa', 'Kentucky', 'Maryland', 'Louisiana', 'Alabama', 'Oklahoma', 'New Mexico', 'Rhode Island', 'Massachusetts', 'South Carolina', 'Indiana', 'Delaware', 'Tennessee', 'Georgia', 'Arizona', 'Nebraska', 'Missouri', 'New Hampshire', 'Ohio', 'Oregon', 'Washington', 'Montana', 'New York']




    legal_colours = []

    for state in states:
        legal_colours.append([state,colorlist.copy()])

    """
    
    states=['wa','nt','q','nsw','v','sa']

    state_dict  ={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']}
    """
    
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



    print(len(allstates))

    for i in range(0,len(allstates),200):
        colormap(allstates[i])


    colormap(my_state_dict)
    time.sleep(10)
    print("VERIFIED ANSWER")
    print(answer)
    print("NUMBER OF backtrack: "+ str(backtrack))
    print("TIME OF EXECUTION: " + str(endtime - starttime) + "seconds") 

    

