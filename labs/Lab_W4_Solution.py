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

from logic import *

"""

Given the following, can you prove that the unicorn is mythical? 
How about magical? Horned? 

“If the unicorn is mythical, then it is immortal, but if it is not mythical, 
then it is a mortal mammal. If the unicorn is either immortal or a mammal, then
 it is horned. The unicorn is magical if it is horned."

As human reasoners, we can see from the ﬁrst two statements, that if it is 
mythical, then it is immortal; otherwise it is a mammal. So it must be either 
immortal or a mammal, and thus horned. That means it is also magical. However, 
we can’t deduce anything about whether it is mythical. To provide a formal 
answer, we can enumerate the possible worlds (25 = 32 of them with 5 
proposition symbols), mark those in which all the assertions are true, and see 
which conclusions hold in all of those. 


Or, we can let the machine do the work—in this case, the PropKB as in 
logic.ipynb:
"""

mythical_kb = PropKB()

Mythical, Immortal, Mammal, Horned, Magical = expr('Mythical, Immortal, Mammal, Horned, Magical')

# "If the unicorn is mythical, then it is immortal" - Tell kb "Mythical => Immortal") 
mythical_kb.tell(Mythical | '==>' | (Immortal))
# "If the unicorn is not mythical, then it is NOT immortal AND a mammal" - Tell kb "˜Mythical => ˜Immortal ˆ Mammal"
mythical_kb.tell(~Mythical | '==>' | (~Immortal & Mammal))

# "If the unicorn is either immortal or a mammal, then it is horned" - Tell kb "Immortal | Mammal => Horned"
mythical_kb.tell((Immortal | Mammal) | '==>' | (Horned))

# "The unicorn is magical if it is horned" - Tell kb "Horned => Magical"
mythical_kb.tell(Horned | '==>' | Magical)


"""NOTE: The clauses derived from our propKB compared to those we told the KB.
This is achiveed via logical equivalence and converting them in Conjunctive
Normal form and storing them in the KB.
"""
# Output clauses
print(mythical_kb.clauses)

"""
Mythical ==> Immortal
~Mythical ==> ~Immortal & Mammal
Immortal | Mammal ==> Horned
Horned ==> Magical

RESULTED IN

(Immortal | ~Mythical), (~Immortal | Mythical), (Mammal | Mythical), (~Immortal | Horned), (~Mammal | Horned), (Magical | ~Horned)
"""

"""NOTE: we can’t deduce anything about whether it is mythical. See answers for
queries below. We are using ask_if_true as oppossed to ask due to implementation
in logic.py (see info on propkb in logic.ipynb for more info)"""

print("Is the unicorn mythical: ", mythical_kb.ask_if_true(Mythical))

print("Is the unicorn not mythical: ", mythical_kb.ask_if_true(~Mythical))

print("Is the unicorn magical: ", mythical_kb.ask_if_true(Magical))

print("Is the unicorn horned: ", mythical_kb.ask_if_true(Horned))

print("Is the unicorn a mammal: ", mythical_kb.ask_if_true(Mammal))



"""<<<<<<<<<<<<<<<<<C. Propositional logic and models>>>>>>>>>>>>>>>>"""


""" QC.a) Write a recursive algorithm PL_TRUE(s,m) that returns true if and only if the
 sentence s is true in the model m (where m assigns a truth value for every 
 symbol in s). The algorithm should run in time linear in the size of the 
 sentence. (Alternatively, use a version of this function from the online code
repository.) """

""" Pseudocode for evaluating the truth of a sentence wrt a model.
function PL-TRUE?(s, m) returns true or false
    if s = True then return true
    else if s = False then return false
    else if SYMBOL?(s) then return LOOKUP(s, m) else branch on the operator of s
        ¬: return not PL-TRUE?(ARG1(s), m)
        ∨: return PL-TRUE?(ARG1(s), m) or PL-TRUE?(ARG2(s), m) 
        ∧: return PL-TRUE?(ARG1(s), m) and PL-TRUE?(ARG2(s), m) 
        ⇒: (not PL-TRUE?(ARG1(s), m)) or PL-TRUE?(ARG2(s), m) 
        ⇔: PL-TRUE?(ARG1(s), m) iff PL-TRUE?(ARG2(s), m)
"""



"""
QC.b Give three examples of sentences that can be determined to be true or false 
in a partial model that does not specify a truth value for some of the symbols.

The question is somewhat ambiguous: we can interpret “in a partial model” to 
mean in all such models or some such models. For the former interpretation, 
the sentences False ∧ P , True ∨ ¬P , and P ∧ ¬P can all be determined 
to be true or false in any partial model. For the latter interpretation, we can
 in addition have sentences such as A ∧ P which is false in the partial 
 model {A = f alse}.

QC.c) Show that the truth value (if any) of a sentence in a partial model 
cannot be determined efficiently in general.

ANS: A general algorithm for partial models must handle the empty partial
 model, with no assignments. In that case, the algorithm must determine 
 validity and unsatisﬁability, which are co-NP-complete and NP-complete respectively.

QC.d) Modify your PL-TRUE? algorithm so that it can sometimes judge truth from partial models, while
retaining its recursive structure and linear run time. Give three examples of sentences whose truth in a
partial model is not detected by your algorithm.


t helps if and and or evaluate their arguments in sequence, terminating on false
 or true arguments, respectively. In that case, the algorithm already has the 
 desired properties: in the partial model where P is true and Q is unknown, 
 P ∨ Q returns true, and ¬P ∧ Q returns false. But the truth values of 
 Q ∨ ¬Q, Q ∨ T rue, and Q ∧ ¬Q are not detected


Qc.d) Investigate whether the modified algorithm makes TT-ENTAILS? more efficient.

Early termination in Boolean operators will provide a very substantial speedup. 
In most languages, the Boolean operators already have the desired property, so 
you would have to write special “dumb” versions and observe a slow-down.

"""
 

"""
Assume the following Wumpus World

4   S               B       P
3   W       S,G,B   P       B      
2   S               B
1   X       B       P       B
    1       2       3       4

Where P=Pit, B=Breeze, W=Wumpus, S=Stench, G=Glitter/Gold, X=Starting location
facing Right.
"""

#TODO