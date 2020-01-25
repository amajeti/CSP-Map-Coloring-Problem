#!/usr/bin/env python

import random
from Node import Node
import pdb
from mapcolor import colormap
import time


list_of_colours = []
allstates = []
backtrack = 0

def init_colours(n):
    for i in range(n):
        list_of_colours.append(random.randint(0,255))

def random_color(n):
    return tuple(list_of_colours)


def generate_colours(states,i,num_colours,colours):
    t_list = []
    for j in range(num_colours):
        t_list.append(Node(colours[j],states[i]))

    return t_list    

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

def getcolours(states,my_state_dict):
    list_col = []
    for i in states:
        list_col.append(my_state_dict.get(i,""))

    return list_col

def init(states,state_dict,num_colours):
    colours = list_of_colours
    root = Node(colours[0],states[0])
    for j in range(num_colours):
        root.put_child(Node(colours[j],states[0]))

    return root


def dfs(my_state_dict,state_dict,num_colours,current_state,states,num):
    global backtrack
    for i in range(len(current_state.next)):
        my_state_dict[current_state.next[0].myname] = current_state.next[i].mycolor   
        if my_state_dict.get(current_state.next[0].myname) in getcolours(state_dict[current_state.next[0].myname],my_state_dict):

            continue
       
        allstates.append(my_state_dict.copy())   
        if num == len(states) - 1:
            return 1,my_state_dict

        temp_list_of_colours = list_of_colours.copy()
        current_state.next[i].next = generate_colours(states,num+1,num_colours,temp_list_of_colours)  

        ans = dfs(my_state_dict,state_dict,num_colours,current_state.next[i],states,num+1)
        if ans[0] == 1:
            return 1,my_state_dict
        


        continue

    backtrack+=1
    return 0,my_state_dict 

    
if __name__ == "__main__":
    num_colours = 4
    init_colours(num_colours)
    list_of_colours = ["red","blue","green","black"]

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
'Mississippi':['Alabama', 'Arkanssas', 'Louisiana', 'Tennessee'],
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
    answer = dfs(my_state_dict,state_dict,num_colours,root,states,0)

    for key in answer[1]:
        if answer[1][key] in getcolours(state_dict[key],my_state_dict):
            print("oops")

    endtime = time.time()
    print("VERIFIED ANSWER")

    print(answer)

    print("NUMBER OF backtrack: "+ str(backtrack))
    print("TIME OF EXECUTION: " + str(endtime - starttime) + "seconds") 


    for i in range(0,len(allstates),50000):
        colormap(allstates[i])


    colormap(my_state_dict)

    time.sleep(10)


