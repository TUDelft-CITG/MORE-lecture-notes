## The Kalman Filter

These properties make Gaussian distributions an attractive choice for Bayesian inference. The Bayesian filter that leverages this special case is known as the **Kalman Filter** (KF). 

### The filtering recursion

All filters fundamentally consist of two steps. We assume that we start with a state prior $\boldsymbol{x}_0$, where the subscript denotes that this variable describes the system state at time $t=0$, which follows a prior distribution $p(\boldsymbol{x}_0)$. We set the time $t=0$ and define a **forecast model** $p(\boldsymbol{x}_{t}|\boldsymbol{x}_{t-1})$ and an **observation model** $p(\boldsymbol{y}_{t}|\boldsymbol{x}_{t})$. A filter then repeats two stages:

1) **Assimilation step**
    - Augment the current state prior with the observation predictions

        $p(\boldsymbol{x}_{t},\boldsymbol{y}_{t}|\boldsymbol{y}_{1:t-1}^{*}) = \underbrace{p(\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t-1}^{*})}_{\text{filtering forecast}} \overbrace{p(\boldsymbol{y}_{t}|\boldsymbol{x}_{t})}^{\text{observation model}}$

    - Condition on the new observation

        $\underbrace{p(\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*})}_{\text{filtering posterior}} = p(\boldsymbol{x}_{t},\boldsymbol{y}_{t}|\boldsymbol{y}_{1:t-1}^{*}) / p(\boldsymbol{y}_{t}^{*}|\boldsymbol{y}_{1:t-1}^{*})$

    - Go to Step 2

2) **Forecast step**
    - Predict the next state

        $p(\boldsymbol{x}_{t+1},\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*}) = \underbrace{p(\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*})}_{\text{filtering posterior}} \overbrace{p(\boldsymbol{x}_{t+1}|\boldsymbol{x}_{t})}^{\text{forecast model}}$

    - Integrate out the past state

        $\underbrace{p(\boldsymbol{x}_{t+1}|\boldsymbol{y}_{1:t}^{*})}_{\text{filtering forecast}} = \int p(\boldsymbol{x}_{t+1},\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*}) d \boldsymbol{x}_{t}$

    - Increment the time step $t := t+1$ and go back to Step 1

### Let's Gaussianize this

In the Kalman filter, we implement these operations for Gaussian PDFs. For this to work, we need the following assumptions:

1) The prior is Gaussian
2) The forecast model is linear and Gaussian
3) The observation model is linear and Gaussian

Together, these assumptions guarantee that all distributions involved are always Gaussian, which allows us to run the Kalman filter infinitely. Let us first define what these elements are defined as:

#### The observation model

In the linear-Gaussian setting, the observation model is usually defined as:

$$
\begin{aligned}
\boldsymbol{y} &= \boldsymbol{H}\boldsymbol{x} + \boldsymbol{\gamma} \\
\boldsymbol{\gamma} &\sim \mathcal{N}(\boldsymbol{\mu}=\boldsymbol{0}, \boldsymbol{\Sigma} = \boldsymbol{R})
\end{aligned}
$$

where

$$
\begin{aligned}
\boldsymbol{y} & \quad \text{observation prediction}\\
\boldsymbol{H} & \quad \text{observation operator}\\
\boldsymbol{x} & \quad \text{quantity of interest}\\
\boldsymbol{\gamma} & \quad \text{observation error}\\
\boldsymbol{R} & \quad \text{observation error covariance matrix}\\
\end{aligned}
$$

This may leave us with a number of questions: What is an "observation operator"? In practice, $\boldsymbol{H}$ is often just a matrix of ones and zeroes that extracts the observed states from the state vector $\boldsymbol{x}$:

$$
\boldsymbol{y} = \left[
\begin{matrix}
y_{1} \\
y_{2} \\
y_{3} \\
\end{matrix}
\right]=\boldsymbol{H}\boldsymbol{x} + \boldsymbol{\gamma}=\left[
\begin{matrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1 \\
\end{matrix}
\right]\left[
\begin{matrix}
x_1 \\
x_2 \\
x_3 \\ 
x_4 \\
x_5 \\
\end{matrix}
\right] + \left[
\begin{matrix}
\gamma_{1} \\
\gamma_{2} \\
\gamma_{3} \\
\end{matrix}
\right]
$$


The interactive figure below shows how conditioning a multivariate Gaussian PDF on different values affects its mean and covariance:

````{iframe-figure} ../_static/elements/element_Gaussian_inference.html
:name: Gaussian_inference
:aspectratio: 1 / 1

The Kalman filter's position update relies on three primary variables: the prior uncertainty (yellow), the observation error (blue), and the observation value (green). Adapt these values by dragging the sliders and observe how the compromise solution (the posterior; red) changes in response.
````

