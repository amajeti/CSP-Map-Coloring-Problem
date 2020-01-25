
import random as rand
import itertools
from copy import deepcopy
import time


full = []
backtrackings = 0
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
    #single_domain=[]
    for state in state_objects:
        if state.singleton==False and len(state.get_domain())==1:
            #print(len(state.domain))
            #print(state.domain)
            #print("hey",state.name)
            state.singleton=True
            color = state.domain[0]
            print("single_state_domain",state.domain)
            return state,color
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
        print(state.name)
        available_domain=deepcopy(state.domain)

        iter1 = 0
        for col in available_domain:
            iter1+=1
            state.curr_state="visited"
            state.type_color=col
            states_and_colors[state.name]=col

            updated_states=up_color(state,col)
            print("total updated states",len(updated_states))
            singleton_states,curr_state=singleton_propagtion(state_objects)
            print(len(singleton_states),curr_state)

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




