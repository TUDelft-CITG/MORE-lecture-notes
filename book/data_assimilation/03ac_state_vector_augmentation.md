### State-vector augmentation

So far, we have chiefly considered state variables $\boldsymbol{x}$ in our algorithms, but many models also include parameters $\boldsymbol{\theta}$ among the quantities of interest. Since parameters are often of similar importance to states, data assimilation is also often tasked with the inference of parameter posteriors. One way to achieve this in the EnKF is through **state-vector augmentation**. In a nutshell, we augment the vector (or ensemble matrix) of states $\boldsymbol{X}_{t}$ with the vector (or ensemble matrix) of parameters $\boldsymbol{\theta}_{t}$: 

$$
\tilde{\boldsymbol{X}_{t}} = [\boldsymbol{X}_{t},\boldsymbol{\theta}_{t}]
$$

In essence, this means that we pretend the parameters are states and gradually update them, as well. Of course, this also means that the forecast model and the observation operator must account for these parameters. For the forecast, it is common to assume an identity model (i.e., «do nothing») for the parameters:

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_{t} + \boldsymbol{\epsilon}
$$

#### An example

Consider a simple model in which we fire a cannonball off a cliff. The cannonball initially flies horizontally, but eventually falls to the ground. This model has two states and one parameter:

$$
\begin{aligned}
h & \quad\text{height} && \quad\text{state} \\
v & \quad\text{vertical velocity} && \quad\text{state} \\
g & \quad\text{gravitational constant} && \quad\text{parameter} \\
\end{aligned}
$$

The forecast model is a simple forward simulation across multiple timesteps: 

$$
\begin{aligned}
v_{t} &= v_{t-1} - g \cdot dt \\
h_{t} &= h_{t-1} + v_{t} \cdot dt \\
\end{aligned}
$$

where $dt$ is the time step length.

Now assume that we have made a mistake! As it turns out, we have centered the prior for the gravitational constant at zero. In consequence, only some of our simulated cannonballs – those with a positive gravitational constant – fall to earth. The others disappear into space:

````{iframe-figure} ../_static/elements/element_state_vector_augmentation_01.html
:name: state_vector_augmentation_01
:aspectratio: 3 / 1

Click the element to (re)start the simulation.
````

