# FrozenLake-v0 | Q-learning


I have implemented the Frozen Lake game using Q learning. 
You can find more information about the game here - https://gym.openai.com/envs/FrozenLake-v0/

![Frozen Lake](https://github.com/Nikhilkohli1/Data-Science-Machine-Learning/blob/master/Frozen%20Lake%20Q%20Learning/Frozen-Lake.png)


The agent controls the movement of a character in a grid world. Some tiles of the grid are walkable, and others lead to the agent falling into the water. Additionally, the movement direction of the agent is uncertain and only partially depends on the chosen direction. The agent is rewarded for finding a walkable path to a goal tile.

The episode ends when you reach the goal or fall in a hole. You receive a reward of 1 if you reach the goal, and zero otherwise.


### Q-learning Algorithm 

The Q function has 2 inputs, the state and the action and based on this it computes the maximum expected future reward. Here is the equation for it:

Q-learning can be implemented as follows:

	Q(s,a)+=α⋅[r+γ⋅maxαQ(s′)−Q(s,a)]

s: is the previous state

a: is the previous action

Q(): is the Q-learning algorithm

s’: is the current state

alpha: is the learning rate, set generally between 0 and 1. Setting the alpha value to 0 means that the Q-values are never updated, thereby nothing is learned. If we set the alpha to a high value such as 0.9, it means that the learning can occur quickly.

gamma: It is the discount factor that is set between 0 and 1. This model the fact that future rewards are worth less than immediate rewards.

max: is the maximum reward that is attainable in the state following the current one (the reward for taking the optimal action thereafter).

The algorithm can be interpreted as:

Initialize the Q-values table, Q(s, a).

Observe the current state, s.

Take an action, a, for that state based on the selection policy.

Pick that action, and observe the reward, r, as well as the new state, s’.

Now update the Q-value for the state with the help of the observed reward and the maximum reward possible for the next state.

Place the state to the new state, and repeat the process until a terminal state is reached.


I have used with the below base parameters for a Baseline performance - 

total_episodes = 5000        
total_test_episodes = 250    
max_steps = 99                

learning_rate = 0.7          
gamma = 0.8                

#### Exploration parameters

epsilon = 1.0                 
max_epsilon = 1.0            
min_epsilon = 0.01            
decay_rate = 0.01             

Then I tuned the parameters to see the effect of each on the agent's performance. 
I also tried few Reward policies other than the defined in the original problem. 

I will further work on Deep Q-learning and add it to this. 



