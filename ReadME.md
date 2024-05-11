# Spiking Neuron Simulation

pip install -r requirements.txt 
//
pip install pygame
Usage
Execute the simulation by running the Python script:

python izhikevich.py



## Overview
This Python application simulates a spiking neuron using a simplified two-dimensional model, The simulation visualizes the membrane potential and recovery variable in real time, illustrating how a neuron responds to stimuli and processes information.

## Model Description
The model implemented in this simulation is a reduced two-dimensional system, it consists of a fast voltage variable (`v`) and a slower recovery variable (`u`),  representing the activation and inactivation dynamics of ion currents such as potassium (K+) 

Model explanation:
Membrane Potential (v): models the neuron's membrane potential. It is influenced by the input current and its interaction with the recovery variable. The behavior of v is characterized by an N-shaped nullcline, which describes how the variable evolves in the absence of other influences.
Recovery Variable (u): Acting as a slower variable, u models the neuron's recovery properties, such as the activation and inactivation dynamics of ion channels. The dynamics of u are typically represented by a sigmoid-shaped nullcline, indicating how it contributes to the neuron's overall behavior over time.
Simulation Equations:
The model operates under two main equations:

Membrane Potential Update (v):
𝑣
˙
=
𝑘
(
𝑣
−
𝑣
𝑟
)
(
𝑣
−
𝑣
𝑡
)
−
𝑢
+
𝐼
v
˙
 =k(v−v 
r
​
 )(v−v 
t
​
 )−u+I
Here, k scales the interaction of the potential with its threshold (v_t) and resting values (v_r), and I represents the input current.
Recovery Variable Update (u):
𝑢
˙
=
𝑎
(
𝑏
(
𝑣
−
𝑣
𝑟
)
−
𝑢
)
u
˙
 =a(b(v−v 
r
​
 )−u)
This equation describes how the recovery variable updates based on its current value and the deviation of the membrane potential from its resting state, modulated by parameters a and b.
Model Parameters:
v_r: Resting membrane potential
v_t: Instantaneous threshold potential
v_peak: Spike cutoff potential, where the simulation artificially induces a spike
k, a, b: Parameters defining the time scales and interactions of the dynamics
Visualization
The visualization is implemented using Pygame. The graphical output shows the membrane potential (v) as a moving line graph, with the potential resetting (mimicking a neuron firing) when it reaches a predefined peak (v_peak). The recovery variable (u) is not directly visualized but affects the dynamics of v.

Features of the Visualization:
Real-time Plot: The membrane potential is plotted as a continuous line
Threshold Indicator: A horizontal line indicates the threshold potential
Dynamic Display: Values of v and u are displayed in real time at the top left corner of the screen, providing immediate feedback on the neuron's state.
Installation
To run this simulation, ensure Python and Pygame are installed on your system. Use the following command to install Pygame if it's not already installed:


