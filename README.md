**Knowledge Representation**

**1. First Assignment**

**BUILDING  YOUR  WORLD**

Create a 2D world that will play host to a game to be played by your agent types. Providecontext for the mechanics of the 
world and the conditions under which the game is complete. The intent of this exercise is for you to demonstrate your 
understanding of how a problem canbe modeled abstractly.  To this end, provide a well a defined task environment, 
implementthreedifferentagent types and provide a PEAS description for each.

•  Critique the advantages and disadvantages of each agent type.
•  Demonstrate  each  agents  ability  to  perform  or  under-perform  in  the  2-dimensionalworld.
•  Discuss, and evaluate, the agents suitability to operate in world of varying sizes.

The solution should be implemented in Python, you may use any of the libraries made avail-able from the AIMA python repository
but they must be clearly referenced (see note on im-porting code under submission), you will be graded on your contribution and 
this should beclearly highlighted.

Write  a  clear  and  concise  description  of  the  agent-based  world.   The  purpose  of  this  is  toarticulate an understanding 
of the underlying concepts being implemented both from a the-oretical and practical perspective.

**SEARCHING  YOUR  WORLD**

•  Formulate  a  well  definedproblem statementand  identify  agoal-stateunder  whichyour game is complete.  
Why is this important to search?  As part of your solution youshould be including the initial state, the set 
of actions, the transition model, a goal testfunction and a path cost function.
•  Select threeuninformed searchtechniques and discuss their appropriateness to yourworld under appropriate 
headings for evaluating problem-solving performance. Im-plement theuninformed searchtechniques and discuss the results.
•  Select  threeinformed searchtechniques  and  discuss  their  appropriateness  to  yourworld under appropriate headings 
for evaluating problem-solving performance. Im-plement theinformed searchtechniques and discuss the results.

Write a clear and concise report detailing the search techniques performance in your agent-based game for the relevant agent types. 
The purpose of this is to articulate an understandingof the underlying concepts, and limitations, being implemented both from a 
theoretical andpractical perspective.

**FORWARD-CHAINING  AND BACKWARD-CHAINING**

Forward-Chaining and Backward-Chaining introduces the capacity for inference in an en-vironment.  How does this benefit the operation 
of an agent, in particularly in your world?Provide a short critical analysis of both approaches. Thereafter demonstrate their applicabil-ity 
by utilising them in your world.

**2. Second Assignment**

**PROBABILITY**

**PROBABILITY DISTRIBUTION TABLE**

You have been studying hard on your latest assignment and asked your fellow students forsome tips:
•  Tip 1 “Study hard and you will do well, fail to do so and you will not”1
•  Tip 2 “Get plenty of rest and you will do well, fail to do so and you will not”
•  Tip 3 “Set an an alarm and you will get up in time, fail to do so and you will not”.
You ask your fellow classmates which tips they adhere to and how frequently. After recordingtheir responses you derive the following table:

![pptKR](https://user-images.githubusercontent.com/22613344/118898251-121f9700-b904-11eb-8e4e-fd85af8f64c9.PNG)

Create a probability distribution table using appropriate variable names.

**BAYESIAN NETWORKS**

You have been given the following Random Variables:
•  Fossil Fuels
•  AI
•  GlobalWarming
•  Renewable Energy
•  Traffic
•  Employed

Construct a model of the world using these variables (Note: this is subjective but there shouldbe a rationale behind your world view 
and your thought process articulated).  Implement aBayesian Network.

•  Provide a visual depiction of the network
•  Detail the associated Conditional Probability Tables.
•  Demonstrate querying the network.

Write a clear and concise description regarding Bayesian Networks, the utility of such and theassociated pro’s and cons. 
Support this with examples where possible.

**LEARNING: DEVELOPING AND EVALUATING A MODEL**
 
 “Naive Bayes is a simple technique for constructing classifiers:  models that assign class la-bels to problem instances, 
 represented as vectors of feature values, where the class labels aredrawn from some finite set. There is not a single 
 algorithm for training such classifiers, but afamily of algorithms based on a common principle: all naive Bayes classifiers 
 assume that thevalue of a particular feature is independent of the value of any other feature, given the classvariable.”  
 You will be implementing a Naive Bayes classifier and discussing the theory be-hind its operation from the perspective of 
 probability, conditional independence, and Bayestheorem.
 
**DATA**
 
 Choose an appropriate multivariate datasets with a limited number of classes from:https://archive.ics.uci.edu/ml/index.phpTake 
 a subset of data from the dataset:
 
 •  Compute the “Prior” probabilities for each of the classes.
 •  Compute the probability of evidence.
 •  Compute the probability of likelihood of evidences (numerator).
 
 Articulate your understanding of each as applied to Bayesian networks.  Tip:  Demonstratethe suitability of a dataset or 
 highlight why it is not suitable.  Use appropriate visualisationsto aid your rationale.
 
 Write  a  clear  and  concise  description  regarding  the  dataset  and  its  appropriateness  for  aNaive Bayes Classifier 
 and probabilistic inference in general.
 
**NAIVE BAYES LEARNER**

Based on your studying and reviewing of “learning.ipynb” implement the Naive Bayes learnerand evaluate its performance for the selected dataset.   
Choose appropriate methodologiesand/or variants in its utilisation.  Present appropriate visualisations demonstrating its per-formance. 
Write a clear and concise description of the Naive Bayes Classifier considering theheadings outlined: probability, conditional independence, 
and Bayes theorem
