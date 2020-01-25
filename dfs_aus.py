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

def color_what(states,mystatedict):
    listcol = []
    for i in states:
        listcol.append(mystatedict.get(i,""))

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

def dfs(mystatedict,statedict,numcolors,current_state,states,num):
    global backtracks
    for i in range(len(current_state.next)):
        mystatedict[current_state.next[0].myname] = current_state.next[i].mycolor
        if mystatedict.get(current_state.next[0].myname) in color_what(statedict[current_state.next[0].myname],mystatedict):

            continue

        states_full.append(mystatedict.copy())
        if num == len(states) - 1:
            return 1,mystatedict

        temp_all_cols = all_cols.copy()
        current_state.next[i].next = gen_cols(states,num+1,numcolors,temp_all_cols)

        ans = dfs(mystatedict,statedict,numcolors,current_state.next[i],states,num+1)
        if ans[0] == 1:
            return 1,mystatedict

        continue

    backtracks+=1
    return 0,mystatedict


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

    mystatedict = {}
    root = init(states,statedict,numcolors)

    start_time = time.time()
    answer = dfs(mystatedict,statedict,numcolors,root,states,0)

    for key in answer[1]:
        if answer[1][key] in color_what(statedict[key],mystatedict):
            print("oops")

    end_time = time.time()

    print(answer)

    print("backtrack count: "+ str(backtracks))
    print("time taken: " + str(end_time - start_time) + "seconds")
