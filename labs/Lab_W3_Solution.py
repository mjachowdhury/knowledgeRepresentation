# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:16:38 2020

@author: Ruairi.OReilly
"""

"""
The following imports assume that your aima repo could is in the parent folder
of the current file.
"""
import os,sys,inspect

current_dir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from search import Problem

"""
Q1 - Missionaries and Cannibals - Uninformed search.

The missionaries and cannibals problem is usually stated as follows. Three 
missionaries and three cannibals are on one side of a river, along with a boat 
that can hold one or two people. 

Find a way to get everyone to the other side without ever leaving a group of 
missionaries in one place outnumbered by the cannibals in that place. This 
problem is famous in AI because it was the subject of the first paper 
that approached problem formulation from an analytical viewpoint (Amarel, 1968).

a) Formulate the problem precisely, making only those distinctions necessary to
     ensure a valid solution. Draw a diagram of the complete state space.
b) Implement and solve the problem optimally using an appropriate search 
    algorithm. Is it a good idea to check for repeated states?
c) Why do you think people have a hard time solving this puzzle, given that the
 state space is so simple?
"""


""" <Python doesn't really suite diagrams - not only state space>
   leftHandSide   Boat          RightHandSide

1   MMCC         | => MC => |        |
2   MMCC         | <= M <=  | C      |
3   MM           | => CC => | C      |
4   MMM          | <= C <=  | CC     |
5   MC           | => MM => | CC     |
6   MC           | <= MC <= | MC     |
7   CC           | => MM => | MC     |
8   CC           | <= C <=  | MMM    |
9   C            | => CC=>  | MMMC   |
10  C            | <= C <=  | MMMC   |
11               | => CC => | MMMCCC |
"""

 
"""
a) Here is one possible representation: A state is a six-tuple of integers 
listing the number of missionaries, cannibals, and boats on the first side, 
and then the second side of the river. The goal is a state with 3 missionaries 
and 3 cannibals on the second side. The cost function is one per action, and 
the successors of a state are all the states that move 1 or 2 people and 1 boat
 from one side to another.
""" 

class cannibalsAndMissionaries(Problem):

    # Representation = <no. can>, <no. of boats>, <no. of missionaries>, 
    # <no. can>,  <no. of boats>, <no. of missionaries>
        
   #([(3,0,3),(0,0,0)]), goal=([(0,0,0), (3,1,3)]) 
   #(3,0,3,0,0,0), goal=(0,0,0,3,1,3)
    
    def __init__(self, initial=[(3,3,1),(0,0,0)], goal=[(0,0,0),(3,3,1)]):
        """ Define goal state and initialize a problem """
        self.goal = goal
        Problem.__init__(self, initial, goal)


    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        
        
        """Return a list of (action . state) pairs.  An action is a triple of the
        form (delta-m delta-c delta-b), where a positive delta means to move from
        side 1 to side 2; negative is the opposite.  For example, the action (1 0 1)
        means move one missionary and 1 boat from side 1 to side 2."""
        
        possible_actions = ["101", "011", "201", "021", "111","101", "011", "201",
                "021", "111"]
        
        return possible_actions
        
        
    """
    
        LHS = state[0]
        RHS = state[1]
        
        if LHS[1]%2==0:
            currentState = LHS
        else:
            currentState = RHS
                              
        return possible_actions
    """


    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError    
    
"""
b. The search space is small, so any optimal algorithm works. For an example, 
see the file "search/domains/cannibals.lisp". It suffices to eliminate moves 
that circle back to the state just visited. From all but the first and last 
states, there is only one other choice.

http://people.eecs.berkeley.edu/~russell/code/search/domains/cannibals.lisp

c. It is not obvious that almost all moves are either illegal or revert to the
previous state. There is a feeling of a large branching factor, and no clear 
way to proceed.
"""



"""
Q2 - 8-puzzle & 8-queens - informed search

Generate a large number of 8-puzzle and 8-queens instances and solve them 
(where possible) by hill climbing (steepest-ascent and first-choice variants), 
hill climbing with random restart, and simulated annealing. Measure the search 
cost and percentage of solved problems and graph these against the optimal 
solution cost. Comment on your results.
"""


def test(initial, goal):
    state = initial
    #
    possible_actions = actions(state)
    
    LHS = state[0]
    RHS = state[1]
    
    print("LHS: ", LHS)
    print("RHS: ", RHS)
    leftHandSide = False
    rightHandSide = False
    
    # Which side of the environment are we on Left or Right - 1 denotes left, 
    # 0 denotes right
    if LHS[2]%2==1:
        leftHandSide = True
        print("IN LHS: ", leftHandSide)
    else:
        rightHandSide = True
        print("IN RHS: ", rightHandSide)
    
    if leftHandSide:
        currentState = LHS
        # Omitting right to left moves - checking state[2] - denotes location of boat
        print(possible_actions) 
        for action in possible_actions:
            print(action)
            boat_locale = action[2]
            print(boat_locale) 
            if int(boat_locale)%2==0:
                print("Removed: ", action)
                possible_actions.remove(action)
    else:
        currentState = RHS
                          
    return possible_actions

   
print(test(initial= [(3,3,1),(0,0,0)], goal=[(0,0,0),(3,3,1)]))


