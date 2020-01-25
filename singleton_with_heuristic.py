#!/usr/bin/env python

import random
from Node import Node
import pdb
import time




colour_list = []

backtrack = 0

allstates = []


class State:
    def __init__(self,name,domain,status="not visited"):
        self.name=name
        self.neighbours=None
        self.colourname=None
        self.status=status
        self.domain=domain
        self.singleton=False

    def set_neighbours(self,neighbours):
        self.neighbours=neighbours
    def get_neighbours(self):
        return self.neighbours
    def set_color(self,colourname):
        self.colourname=colourname
    def set_parent(self,parent):
        self.parent=parent
    def set_domain(self,domain):
        self.domain=domain
    def get_domain(self):
        return self.domain
    def is_singleton(self):
        if self.singleton:
            return self.singleton
        return False



def init_colour(n):
    for i in range(n):
        colour_list.append(random.randint(0,255))

def random_color(n):
    return tuple(colour_list)

def build_color_graph(num,numstates,states):
    colour = random_color(3)
    a = Node(colour[0],states[0])
    root = a
    my_states = {}
    for i in range(1,numstates,1):
        w = Node(colour[0],states[i])
        a.put_child(w)
        a.nextnode = w
        #a = w
        my_states[states[i]] = a

        for j in range(1,num,1):
            b = Node(colour[j])
            a.put_child(b)

        #x.put_child(Node(colour[0],states[i]))
        a = w
            
    print(root)
    print(root.next)
    print(root.next[1].next)

def getcolour(states,my_state_dict):
    list_col = []
    for i in states:
        list_col.append(my_state_dict.get(i,""))

    return list_col

def gencols(states,i,num_colour,colour):
    t_list = []
    #colour = random_color(num_colour)
    for j in range(num_colour):
        t_list.append(Node(colour[j],states[i]))

    return t_list

def singleton(my_state_dict,statedict,num_colour,cur_state,states,num):
    #pdb.set_trace()
    #colormap(my_state_dict)
    global backtrack
    allstates.append(my_state_dict.copy())
    for i in range(len(cur_state.next)):
        my_state_dict[cur_state.next[0].myname] = cur_state.next[i].mycolor   
        if my_state_dict.get(cur_state.next[0].myname) in getcolour(statedict[cur_state.next[0].myname],my_state_dict):
            #print("continued")
            continue
        if num == len(states) - 1:
            return 1,my_state_dict

        tempcolourlist = colour_list.copy()
        removecolour = getcolour(states[num+1],my_state_dict)
        tempcolourlist = [x for x in tempcolourlist if x not in removecolour]
        cur_state.next[i].next = gencols(states,num+1,num_colour,tempcolourlist)


        ans = singleton(my_state_dict,statedict,num_colour,cur_state.next[i],states,num+1)
        if ans[0] == 1:
            return 1,my_state_dict

        continue
        
    backtrack +=1

    return 0,my_state_dict 


def init(states,statedict,num_colour):
    colour = colour_list
    root = Node(colour[0],states[0])
    for j in range(num_colour):
        root.put_child(Node(colour[j],states[0]))

    return root
    

if __name__ == "__main__":
    num_colour = 4
    init_colour(num_colour)

    colour_list = ["red","blue","green","black"]
    

    statedict = {
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
'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
"Hawai":[],
"Alaska":[]
}


    states = ['New Hampshire', 'Oklahoma', 'Tennessee', 'Illinois', 'New Mexico', 'Kentucky', 'West Virginia', 'Maryland', 'Maine', 'Wisconsin', 'Missouri', 'Minnesota', 'Montana', 'Massachusetts', 'South Carolina', 'North Dakota', 'Pennsylvania', 'Arizona', 'South Dakota', 'Ohio', 'Oregon', 'Alabama', 'Indiana', 'Rhode Island', 'Virginia', 'Idaho', 'Nevada', 'Nebraska', 'New York', 'Utah', 'Michigan', 'Kansas', 'Florida', 'Connecticut', 'Iowa', 'Wyoming', 'Louisiana', 'California', 'Vermont', 'Texas', 'Georgia', 'New Jersey', 'North Carolina', 'Washington', 'Delaware', 'Colorado', 'Mississippi', 'Arkansas']

    my_state_dict = {}
   

    root = init(states,statedict,num_colour)

    starttime = time.time()
    answer = singleton(my_state_dict,statedict,num_colour,root,states,0)
    endtime = time.time()
    count = 0 
    for key in answer[1]:
        count+=1
        if answer[1][key] in getcolour(statedict[key],my_state_dict):
            print("failed")


    print(answer)
    print("backtrack count: "+ str(backtrack))
    print("time taken: " + str(endtime - starttime) + "seconds") 





