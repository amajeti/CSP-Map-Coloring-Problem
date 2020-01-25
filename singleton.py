import random as rand
import itertools
from copy import deepcopy
import time


full = []
backtracks = 0
class State:
    def __init__(self,name,domain,curr_state="not visited"):
        self.name=name
        self.joins=None
        self.type_color=None
        self.curr_state=curr_state
        self.domain=domain
        self.singleton=False


    def get_joins(self):
        return self.joins
    def set_joins(self,joins):
        self.joins=joins
    def set_parent(self,parent):
        self.parent=parent
    def set_color(self,type_color):
        self.type_color=type_color
    def get_domain(self):
        return self.domain
    def set_domain(self,domain):
        self.domain=domain

    def is_singleton(self):
        if self.singleton:
            return self.singleton
        return False

def exs_colors(state,domain):
    available_domain=domain.copy()
    for join in state.joins:
        col = join.type_color


        if col!=None and (col in available_domain) :
            available_domain.remove(col)
    return available_domain

def exs_states(state_objects):
    not_visited_states=[]
    for state in state_objects:
        if state.curr_state=="not visited":
            not_visited_states.append(state)
    return not_visited_states

def domain_alter(state,col):
    for join in state.join:
        if (join.curr_state=="not visited") and (col in join.domain):
            (join.domain).remove(col)

def single_domain_states(state_objects):
    for state in state_objects:
        if state.singleton==False and len(state.get_domain())==1:
            state.singleton=True
            col = state.domain[0]
            
            return state,col
    return None,None
def singleton_propagtion(state_objects):

    singleton_states={}
    while True:

        state,col = single_domain_states(state_objects)
        if state==None:
            return singleton_states,"sucess"
        else:
            singleton_states[state]=col
            for join in state.joins:
                if join.curr_state=="not visited" and col in join.domain:
                    if len(join.domain)==1:
                        return singleton_states,"unsucessful"
                    (join.domain).remove(col)


def arr_colors(domain,state_domain):
    dom1=deepcopy(domain)
    dom2=deepcopy(dom1)
    state_dom=deepcopy(state_domain)
    for col in dom1:
        count=0
        for state_color in state_dom:

            if col!=state_color:

                count+=1

        if count==len(state_dom):

            dom2.remove(col)

    return dom2


def up_color(state,col):
    updated_states=[]
    for join in state.joins:
        if join.curr_state=="not visited" and col in join.domain:
            (join.domain).remove(col)
            updated_states.append(join)
    return updated_states
def reset(state,domain,col,updated_states):

    pos = domain.index(col)

    for join in state.joins:
        if join.curr_state=="not visited" and (join in updated_states):
            (join.domain).insert(pos,col)
            dom1 = arr_colors(domain,join.domain)
            join.domain=deepcopy(dom1)
            #print("col after inserting",join.name,join.domain)
def singleton_reset(singleton_states,domain,colour):

    for state,col in singleton_states.items():
        pos = domain.index(col)

        for join in state.joins:
            if join.curr_state=="not visited" and (join.is_singleton()):

                (join.domain).insert(pos,col)
                dom1 = arr_colors(domain,join.domain)
                join.domain=dom1
        state.singleton=False


def csp(state_objects,domain,states_and_colors):
        global backtracks

        if len(states_and_colors)==len(state_objects):
            return states_and_colors

        un_assigned_states=exs_states(state_objects)

        state=un_assigned_states[0]

        available_domain=deepcopy(state.domain)

        iter1 = 0
        for col in available_domain:
            iter1+=1
            state.curr_state="visited"
            state.type_color=col
            states_and_colors[state.name]=col

            updated_states=up_color(state,col)

            singleton_states,curr_state=singleton_propagtion(state_objects)


            if curr_state!="unsucessful":
                result=csp(state_objects,domain,states_and_colors)
            else:
                result=curr_state
            if result!="unsucessful":
                return result
            del states_and_colors[state.name]
            state.type_color=None
            state.curr_state="not visited"

        backtracks+=1
        return "unsucessful"



def to_objects(states,domain):
    state_objs = []
    dom1=deepcopy(domain)
    for state in states:
        state_obj=State(state,dom1)
        state_objs.append(state_obj)
        dom1=deepcopy(dom1)
    return state_objs


def main():
    states=['wa','nt','q','nsw','v','sa']
    restriction_graph={
        'wa':['nt','sa'],
        'nt':['wa','q','sa'],
        'sa':['wa','q','nsw','nt','v'],
        'q':['nt','sa','nsw'],
        'nsw':['q','v','sa'],
        'v':['sa','nsw']
        }
    states= ['New Hampshire', 'Oklahoma', 'Tennessee', 'Illinois', 'New Mexico', 'Kentucky', 'West Virginia', 'Maryland', 'Maine', 'Wisconsin', 'Missouri', 'Minnesota', 'Montana', 'Massachusetts', 'South Carolina', 'North Dakota', 'Pennsylvania', 'Arizona', 'South Dakota', 'Ohio', 'Oregon', 'Alabama', 'Indiana', 'Rhode Island', 'Virginia', 'Idaho', 'Nevada', 'Nebraska', 'New York', 'Utah', 'Michigan', 'Kansas', 'Florida', 'Connecticut', 'Iowa', 'Wyoming', 'Louisiana', 'California', 'Vermont', 'Texas', 'Georgia', 'New Jersey', 'North Carolina', 'Washington', 'Delaware', 'Colorado', 'Mississippi', 'Arkansas']
    restriction_graph ={
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
            'Wyoming':['Colorado', 'Idaho', 'Montana', 'Nebraska', 'South Dakota', 'Utah'],
            'Hawaii':[],
            'Alaska':[]
            }



    '''states=['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE',
                 'QC', 'SK', 'YT']
    restriction_graph={
            'AB':['BC','NT','SK'],
            'BC':['NT','YT','AB'],
            'MB':['NU','ON','SK'],
            'NB':['NS','QC'],
            'NL':['QC'],
            'NT':['NU','SK','BC','AB','YT'],
            'NU':['MB','NT'],
            'ON':['QC','MB'],
            'YT':['NT','BC'],
            'SK':['AB','NT','MB'],
            'QC':['ON','NL','NB'],
            'NS':['NB'],
            'PE':[]
            }'''


    domain=["blue","green","red","orange"]
    state_objects = to_objects(states,domain)


    states_and_colors={}
    for state in state_objects:
        key = state.name
        values=restriction_graph[key]
        joins=[]
        for value in values:
            obj=[obj_form for obj_form in state_objects if obj_form.name==value ]
            joins.append(obj[0])

        state.set_joins(joins)




    st=csp(state_objects,domain,states_and_colors)




start_time = time.time()
main()
end_time = time.time()

print("Time taken = " + str(end_time- start_time) + " seconds")
print("Number of Backtracks= " + str(backtracks))

'''st1 = {'Oregon': 'blue', 'Delaware': 'blue', 'Arkansas': 'blue', 'Michigan': 'blue', 'Kentucky': 'blue',
 'North Dakota': 'blue', 'Wyoming': 'blue', 'Texas': 'green', 'Alabama': 'blue', 'Kansas': 'blue',
 'Missouri': 'green', 'Arizona': 'blue', 'Vermont': 'blue', 'South Carolina': 'blue', 'Rhode Island': 'blue',
 'Washington': 'green', 'South Dakota': 'green', 'Mississippi': 'green', 'Idaho': 'red', 'California': 'red',
 'Montana': 'orange', 'Maryland': 'green', 'Maine': 'blue', 'New York': 'green', 'Utah': 'orange', 'Indiana': 'red',
 'North Carolina': 'green', 'Louisiana': 'red', 'West Virginia': 'red', 'Nebraska': 'red', 'Tennessee': 'red',
 'Minnesota': 'red', 'Iowa': 'blue', 'New Mexico': 'red', 'Massachusetts': 'red',
 'Oklahoma': 'orange', 'Ohio': 'green', 'Connecticut': 'orange', 'Florida': 'green', 'Wisconsin': 'green',
 'Illinois': 'orange', 'Colorado': 'green', 'Pennsylvania': 'orange', 'New Jersey': 'red', 'Nevada': 'green',
 'Georgia': 'orange', 'New Hampshire': 'green', 'Virginia': 'orange'}'''
k = {'Kansas': 'blue', 'New Hampshire': 'blue', 'Idaho': 'blue', 'Louisiana': 'blue', 'New Jersey': 'blue',
 'Arkansas': 'green', 'Kentucky': 'blue', 'Maine': 'green', 'Minnesota': 'blue',
 'Missouri': 'red', 'West Virginia': 'green', 'North Carolina': 'blue', 'Massachusetts': 'green',
 'Michigan': 'green', 'Indiana': 'red', 'Illinois': 'orange', 'Virginia': 'red', 'Oklahoma': 'orange',
 'Montana': 'orange', 'North Dakota': 'green', 'Texas': 'red', 'Colorado': 'red', 'South Carolina': 'green',
 'Maryland': 'blue', 'California': 'blue', 'New York': 'orange', 'Florida': 'blue', 'Vermont': 'red',
 'Utah': 'orange', 'Georgia': 'red', 'Oregon': 'green', 'Wisconsin': 'red', 'Rhode Island': 'blue',
 'Nebraska': 'orange', 'New Mexico': 'blue', 'Mississippi': 'red', 'Alabama': 'green', 'Nevada': 'red',
 'Tennessee': 'orange', 'Iowa': 'green', 'South Dakota': 'red', 'Ohio': 'orange', 'Pennsylvania': 'red',
 'Washington': 'red', 'Wyoming': 'green', 'Arizona': 'green', 'Delaware': 'green', 'Connecticut': 'red'}
k={'Ohio': 'blue', 'Hawaii': 'blue', 'Vermont': 'blue', 'Maine': 'blue', 'Tennessee': 'blue',
'Oklahoma': 'blue', 'Colorado': 'green', 'Alabama': 'green', 'Oregon': 'blue',
 'Minnesota': 'blue', 'New Mexico': 'red', 'Mississippi': 'red', 'Kansas': 'red',
 'New Hampshire': 'green', 'Louisiana': 'blue', 'Rhode Island': 'blue', 'Montana': 'blue',
 'Wisconsin': 'green', 'Michigan': 'red', 'Arkansas': 'green', 'Maryland': 'blue',
 'Missouri': 'orange', 'Massachusetts': 'red', 'North Dakota': 'green', 'Nevada': 'green',
 'South Dakota': 'orange', 'Illinois': 'blue', 'Washington': 'green', 'Virginia': 'green',
 'Indiana': 'green', 'Alaska': 'blue', 'Connecticut': 'green', 'North Carolina': 'red',
 'New York': 'orange', 'New Jersey': 'blue', 'Iowa': 'red', 'Kentucky': 'red',
 'South Carolina': 'blue', 'West Virginia': 'orange', 'Idaho': 'orange',
 'Florida': 'blue', 'Delaware': 'green', 'Nebraska': 'blue', 'Arizona': 'orange',
'Wyoming': 'red', 'California': 'red', 'Utah': 'blue', 'Texas': 'orange', 'Pennsylvania': 'red',
 'Georgia': 'orange'}
print(list(k.keys()))


