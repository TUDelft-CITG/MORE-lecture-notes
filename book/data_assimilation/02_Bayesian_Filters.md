# Bayesian filters

Fundamentally, all data assimilation (DA) algorithms leverage **Bayes' Theorem**. Before we dive into the methodological details, we should first establish some necessary vocabulary. In data assimilation, we usually care about the inference of **states** and/or **parameters** by assimilating **observations**:

- **states** are (typically) time-varying uncertain quantities of interest; typical examples of states would be quantities like soil moisture, temperature, wave height, stock price, blood pressure, or mechanical load. In this chapter, we will refer to states with the variable $\boldsymbol{x}$.
- **parameters** are (typically) time-invariable uncertain quantities of interest; typical examples include the gravitational constant, the porosity of a subsurface medium, the geometry of a dike, or the volatility in a certain stock price. In this chapter, we will refer to parameters with the variable $\boldsymbol{\theta}$.
- **observations** are properties of a system which we can measure or observe. These can be observations of states, parameters, or any combination thereof. In this chapter, we will refer to observations with the variable $\boldsymbol{y}^{*}$.

Data assimilation further requires two important pieces - a **forecast model** and an **observation model**:

- a **forecast model** is a conventional numerical or analytical model that predicts quantities of interests (states or parameters) based on other quantities of interest (states or parameters). From a statistical perspective, these models establish a statistical relationship between the states $\boldsymbol{x}$ and/or the parameters $\boldsymbol{\theta}$.
- an **observation model** relates these quantities of interest to our observations $\boldsymbol{y}^{*}$ by making **observation predictions** $\boldsymbol{y}$. From a statistical perspective, observation models establish a statistical relationship between the states $\boldsymbol{x}$ and parameters $\boldsymbol{\theta}$ with the observation predictions $\boldsymbol{y}$.

In broader literature, there are different types of DA algorithms which vary in scope and approach. The most common examples are:

- **Variational DA**: These methods seek to identify a *maximum a posteriori* estimate of the states and parameters, that is to say, the most probable combination of states and parameters. As such, they usually do not provide uncertainty estimates.
- **Bayesian smoothers** seek to infer the full posterior of the states and parameters $p(\boldsymbol{x}_{1:T},\boldsymbol{\theta}|\boldsymbol{y}_{1:T}^{*})$, that is to say, the best possible estimate of our quantities of interest. Example applications include subsurface reservoir characterization or forensic analysis.
- **Bayesian filters** only seek to infer the posterior of the latest states $p(\boldsymbol{x}_{T},\boldsymbol{\theta}|\boldsymbol{y}_{1:T}^{*})$ given all information so far. This makes filters very useful in systems in which we want to know the latest state, but do not necessarily care about improving hindsight. Example applications include stock trading, robotics, tracking, weather forecasting, or pump control.

In this chapter, we will focus only on **Bayesian filters**. However, much of the methodology can be applied directly to Bayesian smoothing applications, as well!

## A brief recapitulation of Bayes' Theorem

As established, Bayes' Theorem lies at the heart of DA. To begin, let us recall the basic principles of **Bayesian inference**. Assuming that we have two random variables $\boldsymbol{x}$ and $\boldsymbol{y}$ (ignoring parameters for the time being), Bayes' Theorem is defined as:

$$
\underbrace{p(\boldsymbol{x}|\boldsymbol{y}^{*})}_{\text{posterior}} = \frac{p(\boldsymbol{y}^{*},\boldsymbol{x})}{p(\boldsymbol{y}^{*})} = \frac{\overbrace{p(\boldsymbol{x})}^{\text{prior}}\overbrace{p(\boldsymbol{y}^{*}|\boldsymbol{x})}^{\text{likelihood}}}{\underbrace{p(\boldsymbol{y}^{*})}_{\text{model evidence}}}
$$

There are two separate things happening here:
1) We combine the **prior** $p(\boldsymbol{x})$ and the observation model $p(\boldsymbol{y}|\boldsymbol{x})$ into a joint probability distribution of $p(\boldsymbol{x},\boldsymbol{y})$ between the states $\boldsymbol{x}$ and observation predictions $\boldsymbol{y}$. Mind that the observation model yields a **likelihood** $p(\boldsymbol{y}^{*}|\boldsymbol{x})$ once we plug in a specific observation value $\boldsymbol{y}^{*}$.
2) We then condition this joint distribution $p(\boldsymbol{x},\boldsymbol{y})$ on a specific observation value $\boldsymbol{y}^{*}$ to obtain the **posterior** distribution $p(\boldsymbol{x}|\boldsymbol{y}^{*})$.