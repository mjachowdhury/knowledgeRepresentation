# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:47:30 2020
@author: Ruairi.OReilly

NB - Create a directory at the top level of the aima repo with called 'labs'. 
This directory is for storing your lab work, each file should take the 
following naming convention

'W<Week_num>_Lab_<Surname>_<First name>_<Student Number>.py'
e.g.
'W1_Lab_Oreilly_Ruairi_R123456.py
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

from agents import TableDrivenVacuumAgent, TrivialVacuumEnvironment, Agent, Environment

"""
Q1 - Instantiate a Table driven vacummn agent and the trivial vacuum 
environment.

    a) Create a function called 'runEnvironment' that takes in the agent, 
    environment and the number of runs. 
    b) Each run should output the 
    'Run: <num>: Env. status: {(0, 0): <status>, (1, 0): <status>} Agent Performance: <num>'
    where num and status are pulled from the respective environment.
    c) Use your function to evaluate and compare running the table driven agent
    in 2,4 and 8 runs.
    d) What is the optimal status and sequence of actions in the context of the agents 
    performance?
    e) What is the least optimal status and sequence of actions in the context of the agents 
    performance?
"""
  
#RUN

def runEnvironment(env, agent, runs):
    env.add_thing(agent)
    
    # What is the status of the environment?
    print("Initial Environment status: ", env.status)
    
    for num in range(runs):
        print("\nRun: {}: Env. status: {} Agent Performance: {}".format(num, env.status, agent.performance))
        env.step()
    

def q1():
        
    # Instantiate the agent and see if it is alive
    testAgent1 = TableDrivenVacuumAgent()
    testAgent2 = TableDrivenVacuumAgent()
    testAgent3 = TableDrivenVacuumAgent()
    
    print("Is the agent alive? ",testAgent1.alive)
    
    #ENVIRONMENT
    environment1 = TrivialVacuumEnvironment()
    environment2 = TrivialVacuumEnvironment()
    environment3 = TrivialVacuumEnvironment()
    
    #RUNS
    runEnvironment(environment1, testAgent1, 2) 
    runEnvironment(environment2, testAgent2, 4) 
    runEnvironment(environment3, testAgent3, 8) 

""" Q2 - Puzzle

A farmer has to get a fox, a chicken, and a sack of feed across a 
river. He has a boat, and it can only carry him and one other thing

> If the fox and the chicken are left together, the fox will eat the chicken.
> If the chicken and the feed are left together, the chicken will eat the feed.

How does the farmer do it?

<Problem Solution>

The farmer and the chicken cross the river, (the fox and feed are safe 
together), he leaves the chicken on the other side and goes back across. The 
farmer then takes the fox across the river, and since he can't leave the fox 
and chicken together, he brings the chicken back. Again, since the chicken and 
feed can't be left together, he leaves the chicken and he takes the feed across
 and leaves it with the fox. He then returns to pick up the chicken and heads 
 across the river one last time

"""
    
""" Solution percept sequence

LOC A                   |           LOC B               |   Action
Farmer Chicken Feed Fox |                               | moveChicken
                        | Chicken                       | move
Feed Fox                |                               | moveFox
                        | Chicken Fox                   | moveChicken
Chicken Feed            |                               | moveFeed
                        | Feed Fox                      | move
Chicken                 |                               | moveChicken
                        | Chicken Feed Fox              | SUCCESS                        
"""


loc_A, loc_B = (0, 0), (1, 0)  # The two locations for the  world


"""-------------------------AGENT-------------------------"""
def TableDrivenFarmerAgent():
    """[Figure 2.3]"""
    
    table = {((loc_A, 'Chicken Feed Fox'),): 'moveChicken',
         ((loc_A, 'Chicken Feed Fox'), (loc_B, 'Chicken'),): 'move',
         ((loc_A, 'Chicken Feed Fox'), (loc_B, 'Chicken'), (loc_A, 'Feed Fox'),): 'moveFox',
         ((loc_A, 'Chicken Feed Fox'), (loc_B, 'Chicken'), (loc_A, 'Feed Fox'), (loc_B, 'Chicken Fox'),): 'moveChicken',
         ((loc_A, 'Chicken Feed Fox'), (loc_B, 'Chicken'), (loc_A, 'Feed Fox'), (loc_B, 'Chicken Fox'), (loc_A, 'Chicken Feed'),): 'moveFeed',
         ((loc_A, 'Chicken Feed Fox'), (loc_B, 'Chicken'), (loc_A, 'Feed Fox'), (loc_B, 'Chicken Fox'), (loc_A, 'Chicken Feed'), (loc_B, 'Feed Fox'),): 'move',
         ((loc_A, 'Chicken Feed Fox'), (loc_B, 'Chicken'), (loc_A, 'Feed Fox'), (loc_B, 'Chicken Fox'), (loc_A, 'Chicken Feed'), (loc_B, 'Feed Fox'), (loc_A, 'Chicken'),): 'moveChicken',
         ((loc_A, 'Chicken Feed Fox'), (loc_B, 'Chicken'), (loc_A, 'Feed Fox'), (loc_B, 'Chicken Fox'), (loc_A, 'Chicken Feed'), (loc_B, 'Feed Fox'), (loc_A, 'Chicken'), (loc_B, 'Chicken Feed Fox'),): 'SUCCESS'}
    
    return Agent(TableDrivenFarmerAgentProgram(table))

"""------------------------- AGENT PROGRAM-------------------------"""

def TableDrivenFarmerAgentProgram(table):
    """This agent selects an action based on the percept sequence.
    It is practical only for tiny domains.
    To customize it, provide as table a dictionary of all
    {percept_sequence:action} pairs. [Figure 2.7]"""
    percepts = []

    def program(percept):
        print("TableDrivenFarmerAgentProgram [Percept]: ", percept)   
        percepts.append(percept)
        action = table.get(tuple(percepts))
        print("TableDrivenFarmerAgentProgram [Action]: ", action)       
        return action

    return program


"""-------------------------ENVIRONMENT-------------------------"""

class TrivialFarmerEnvironment(Environment):
    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    def __init__(self):
        super().__init__()
        self.status = {loc_A: 'Chicken Feed Fox',
                       loc_B: ''}

      
    def thing_classes(self):
        return [TableDrivenFarmerAgent]    
        
    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        print("TrivialFarmerEnvironment [Percept]: ", self.status[agent.location])       
        return (agent.location, self.status[agent.location])

    def move(self, agent):        
        print("TrivialFarmerEnvironment->move()")
        if(agent.location == loc_A):
            agent.location = loc_B
        else:
            agent.location = loc_A
        
        
    def removeChicken(self, agent):     
        if self.status[agent.location] == 'Chicken Feed Fox':
            self.status[agent.location] = 'Feed Fox'
        elif self.status[agent.location] == 'Chicken Fox':
            self.status[agent.location] = 'Fox'
        elif self.status[agent.location] == 'Chicken Feed':
            self.status[agent.location] = 'Feed'
        else:
            self.status[agent.location] = ''
        
    def addChicken(self, agent):        
        if self.status[agent.location] == 'Feed Fox':
            self.status[agent.location] = 'Chicken Feed Fox'
        elif self.status[agent.location] == 'Fox':
            self.status[agent.location] = 'Chicken Fox'
        elif self.status[agent.location] == 'Feed':
            self.status[agent.location] = 'Chicken Feed'
        else:
            self.status[agent.location] = 'Chicken'
            
    def moveChicken(self, agent):
        self.removeChicken(agent)     
        self.move(agent)
        self.addChicken(agent)     
    
    def removeFox(self, agent):        
        if self.status[agent.location] == 'Chicken Feed Fox':
            self.status[agent.location] = 'Chicken Feed'
        elif self.status[agent.location] == 'Chicken Fox':
            self.status[agent.location] = 'Chicken'
        elif self.status[agent.location] == 'Feed Fox':
            self.status[agent.location] = 'Feed'
        else:
            self.status[agent.location] = ''
    
    def addFox(self, agent):
        if self.status[agent.location] == 'Chicken Feed':
            self.status[agent.location] = 'Chicken Feed Fox'
        elif self.status[agent.location] == 'Feed':
            self.status[agent.location] = 'Feed Fox'
        elif self.status[agent.location] == 'Chicken':
            self.status[agent.location] = 'Chicken Fox'
        else:
            self.status[agent.location] = 'Fox'
            
    def moveFox(self, agent):
        self.removeFox(agent)     
        self.move(agent)
        self.addFox(agent)     
    
    def removeFeed(self, agent):
        if self.status[agent.location] == 'Chicken Feed Fox':
            self.status[agent.location] = 'Chicken Fox'
        elif self.status[agent.location] == 'Chicken Feed':
            self.status[agent.location] = 'Chicken'
        elif self.status[agent.location] == 'Feed Fox':
            self.status[agent.location] = 'Fox'
        else:
            self.status[agent.location] = ''
    
    def addFeed(self, agent):
        if self.status[agent.location] == 'Chicken Fox':
            self.status[agent.location] = 'Chicken Feed Fox'
        elif self.status[agent.location] == 'Fox':
            self.status[agent.location] = 'Feed Fox'
        elif self.status[agent.location] == 'Chicken':
            self.status[agent.location] = 'Chicken Feed'
        else:
            self.status[agent.location] = 'Fox'
            
    def moveFeed(self, agent):
        self.removeFeed(agent)     
        self.move(agent)
        self.addFeed(agent)     
    
    
    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
               
        """      
        moveChicken
        move
        moveFox
        moveFeed
        moveChicken
        SUCCESS
       """ 
        if action == 'move':
            self.move(agent)
        elif action == 'moveChicken':
            self.moveChicken(agent)
            agent.performance -= 1
        elif action == 'moveFox':
            self.moveFox(agent)
            agent.performance -= 1
        elif action == 'moveFeed':
            self.moveFeed(agent)
            agent.performance -= 1
        elif action == 'SUCCESS':
            print('<<<<Successfully completed:', agent.performance)
        
    def default_location(self, thing):
        """Agents start in either location at random."""
        return loc_A


def q2():
    farmerAgent = TableDrivenFarmerAgent()
    farmerEnvironment = TrivialFarmerEnvironment()
    runEnvironment(farmerEnvironment, farmerAgent, 8)


"""-------------------------RUNTIME-------------------------"""

print("\n\n <<<<<<<<<<<<<<<<<<<<<Q1>>>>>>>>>>>>>>>>>\n")

q1()

print("\n\n <<<<<<<<<<<<<<<<<<<<<Q2>>>>>>>>>>>>>>>>>\n")

q2()

