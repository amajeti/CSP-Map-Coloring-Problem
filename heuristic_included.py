#!/usr/bin/env python

import random
from Node import Node
import pdb
import time


colour_list = []


all_states = []
backtrack = 0

def pick_big_state(legalcolours):
    for k in sorted(legalcolours, key=lambda k: len(legalcolours[k]), reverse=True):
        #print k
        return k

def update_neighbors(state_changed,legalcolours,state_dict,colourassigned,states):
    for state in state_dict[state_changed]:
            #print(state)
            if colourassigned in list(filter(lambda x:x[0]==state,legalcolours))[0][1]:
                list(filter(lambda x:x[0]==state,legalcolours))[0][1].remove(colourassigned)


def init_colors(n):
    for i in range(n):
        colour_list.append(random.randint(0,255))

def random_color(n):
    return tuple(colour_list)

def init(states,state_dict,num_colour):
    colors = colour_list
    root = Node(colors[0],states[0])
    for j in range(num_colour):
        root.put_child(Node(colors[j],states[0]))

    return root

def generate_colors(states,i,num_colour,colors):
    t_list = []
    #colors = random_color(num_colour)
    for j in range(num_colour):
        t_list.append(Node(colors[j],states[i]))

    return t_list    

def getcolors(states,my_state_dict):
    list_col = []
    for i in states:
        list_col.append(my_state_dict.get(i,""))

    return list_col

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

        #x.put_child(Node(colors[0],states[i]))
        a = w
            
    print(root)
    print(root.next)
    print(root.next[1].next)


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

        if num == len(states) - 1:
            return 1,my_state_dict

        
        backtrack +=1
        update_neighbors(current_state.next[0].myname,temp_legalcolours,state_dict,current_state.next[i].mycolor,states)
        temp_legalcolours = sorted(temp_legalcolours,key=lambda x:len(x[1]))
        temp_colour_list = colour_list.copy()
        remove_colors = getcolors(temp_legalcolours[num+1][0],my_state_dict)
        #temp_colour_list = temp_colour_list - remove_colors
        temp_colour_list = [x for x in temp_colour_list if x not in remove_colors]
        current_state.next[i].next = generate_colors(states,num+1,num_colour,temp_colour_list)


        ans = heuristic_included(my_state_dict,state_dict,num_colour,current_state.next[i],states,num+1,temp_legalcolours)
        if ans[0] == 1:
            return 1,my_state_dict

        continue

    return 0,my_state_dict 
            
    
    
if __name__ == "__main__":
    num_colour = 4
    init_colors(num_colour)

    colour_list = ["red","blue","green","black"]
   




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

    states = ['Illinois', 'Oklahoma', 'California', 'Utah', 'Wyoming', 'Missouri', 'Michigan', 'Texas', 'Iowa', 'Delaware', 'Tennessee', 'Maryland', 'Kentucky', 'Montana', 'Minnesota', 'Connecticut', 'Louisiana', 'West Virginia', 'Pennsylvania', 'Nebraska', 'Kansas', 'Indiana', 'Rhode Island', 'Arizona', 'Florida', 'Massachusetts', 'South Dakota', 'Nevada', 'South Carolina', 'Ohio', 'New Hampshire', 'Idaho', 'Washington', 'Colorado', 'Oregon', 'New Jersey', 'Mississippi', 'Arkansas', 'Vermont', 'Wisconsin', 'Alabama', 'Georgia', 'Maine', 'New Mexico', 'North Carolina', 'New York', 'Virginia', 'North Dakota']



    legalcolours = []

    for state in states:
        legalcolours.append([state,colour_list.copy()])
  
    my_state_dict = {}
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

    



