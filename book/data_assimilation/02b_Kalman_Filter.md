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
\boldsymbol{y}_{t} &= \boldsymbol{H}\boldsymbol{x}_{t} + \boldsymbol{\gamma}_{t} \\
\boldsymbol{\gamma}_{t} &\sim \mathcal{N}(\boldsymbol{\mu}=\boldsymbol{0}, \boldsymbol{\Sigma} = \boldsymbol{R})
\end{aligned}
$$

where

$$
\begin{aligned}
\boldsymbol{y}_{t} & \quad \text{observation prediction}\\
\boldsymbol{H} & \quad \text{observation operator}\\
\boldsymbol{x}_{t} & \quad \text{quantity of interest}\\
\boldsymbol{\gamma}_{t} & \quad \text{observation error}\\
\boldsymbol{R} & \quad \text{observation error covariance matrix}\\
\end{aligned}
$$

This may leave us with a number of questions: What is an "observation operator"? In practice, $\boldsymbol{H}$ is often just a matrix of ones and zeroes that extracts the observed states from the state vector $\boldsymbol{x}$:

$$
\begin{aligned}
\boldsymbol{y}_{t} = \left[
\begin{matrix}
y_{t,1} \\
y_{t,2} \\
y_{t,3} \\
\end{matrix}
\right]=\boldsymbol{H}\boldsymbol{x}_{t} + \boldsymbol{\gamma}_{t}&=\left[
\begin{matrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 1 \\
\end{matrix}
\right]\left[
\begin{matrix}
x_{t,1} \\
x_{t,2} \\
x_{t,3} \\ 
x_{t,4} \\
x_{t,5} \\
\end{matrix}
\right] + \left[
\begin{matrix}
\gamma_{t,1} \\
\gamma_{t,2} \\
\gamma_{t,3} \\
\end{matrix}
\right] \\
&=\left[
\begin{matrix}
x_{t,2} \\
x_{t,4} \\
x_{t,5} \\
\end{matrix}
\right] + \left[
\begin{matrix}
\gamma_{t,1} \\
\gamma_{t,2} \\
\gamma_{t,3} \\
\end{matrix}
\right] \\
&=\left[
\begin{matrix}
x_{t,2} + \gamma_{t,1} \\
x_{t,4} + \gamma_{t,2} \\
x_{t,5} + \gamma_{t,3} \\
\end{matrix}
\right]
\end{aligned}
$$

Of course, other linear operations (such as averaging) are also viable. The observation error $\boldsymbol{\gamma}_{t}$ reflects the imprecision in our measurements and has an interesting role: it blurs the deterministic relationship between $\boldsymbol{x}_{t}$ and $\boldsymbol{y}_{t}$, which permits multiple different $\boldsymbol{x}_{t}$ values to produce the same observation value $\boldsymbol{y}_{t}^{*}$, although usually with different probability density.

#### The forecast model

Likewise, the forecast model in the linear-Gaussian setting is usually defined as:

$$
\begin{aligned}
\boldsymbol{x}_{t+1} &= \boldsymbol{A}\boldsymbol{x}_{t} + \boldsymbol{\epsilon} \\
\boldsymbol{\epsilon} &\sim \mathcal{N}(\boldsymbol{\mu}=\boldsymbol{0}, \boldsymbol{\Sigma} = \boldsymbol{Q})
\end{aligned}
$$

where

$$
\begin{aligned}
\boldsymbol{x}_{t+1} & \quad \text{state at time }t+1\\
\boldsymbol{A} & \quad \text{linear model}\\
\boldsymbol{x}_{t} & \quad \text{state at time }t\\
\boldsymbol{\epsilon}_{t} & \quad \text{forecast error}\\
\boldsymbol{Q} & \quad \text{forecast error covariance matrix}\\
\end{aligned}
$$

If we start from a Gaussian filtering posterior $p(\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*})$, the mean and covariance of the filtering forecast are defined as:

$$
\begin{aligned}
\boldsymbol{\mu}_{t+1} &= \boldsymbol{A}\boldsymbol{x}_{t} + \boldsymbol{\epsilon}_{t} \\
\boldsymbol{\Sigma}_{t+1} &= \boldsymbol{A}\boldsymbol{\Sigma}_{\boldsymbol{x}_{t}}\boldsymbol{A}^\intercal + \boldsymbol{Q} \\
\end{aligned}
$$

#### The assimilation step

With these equations above, we can forecast a Gaussian distribution through time, and relate the states to observation predictions. Obtaining the filtering posterior in the assimilation step then becomes a simple application of the Gaussian conditioning operation:

$$
\begin{aligned}
\boldsymbol{\mu}_{\boldsymbol{x}}^* &= \boldsymbol{\mu}_{\boldsymbol{x}} - \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{y}}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{y}}^{-1}(\boldsymbol{\mu}_{\boldsymbol{y}} - \boldsymbol{y}^*) \\
\boldsymbol{\Sigma}_{\boldsymbol{x}}^* &= \boldsymbol{\Sigma}_{\boldsymbol{x}} - \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{y}}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{y}}^{-1}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{x}}
\end{aligned}
$$

Inserting the identities above, we obtain the following Equations:

$$
\begin{aligned}
\boldsymbol{\mu}_{\boldsymbol{x}}^* &= \boldsymbol{\mu}_{\boldsymbol{x}} - \overbrace{\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}}\boldsymbol{H}^\intercal\left(\boldsymbol{H}\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}}\boldsymbol{H}^\intercal + \boldsymbol{R}\right)^{-1}}^{\text{Kalman Gain }\boldsymbol{K}}(\boldsymbol{\mu}_{\boldsymbol{y}} - \boldsymbol{y}^*) &&= \boldsymbol{\mu}_{\boldsymbol{x}} - \boldsymbol{K} (\boldsymbol{\mu}_{\boldsymbol{y}} - \boldsymbol{y}^*) \\
\boldsymbol{\Sigma}_{\boldsymbol{x}}^* &= \boldsymbol{\Sigma}_{\boldsymbol{x}} - \underbrace{\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}}\boldsymbol{H}^\intercal\left(\boldsymbol{H}\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}}\boldsymbol{H}^\intercal + \boldsymbol{R}\right)^{-1}}_{\text{Kalman Gain }\boldsymbol{K}}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{x}} &&= \boldsymbol{\Sigma}_{\boldsymbol{x}} - \boldsymbol{K}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{x}}
\end{aligned}
$$

where the expression $\boldsymbol{K} = \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}}\boldsymbol{H}^\intercal\left(\boldsymbol{H}\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}}\boldsymbol{H}^\intercal + \boldsymbol{R}\right)^{-1}$ is defined as the so-called **Kalman Gain**.

#### Kalman Gain, or finding statistical compromise

The Kalman Gain is an interesting quantity. A closer look at its formulation reveals that it defines a compromise between the prior uncertainty $\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}}$ and the observation error $\boldsymbol{R}$. This allows us to distinguish two cases:
- $\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}} \ll \boldsymbol{R}\$: if the prior uncertainty is much lower than the observation error, then the Kalman Gain will be close to zero, which will nullify any update to the mean and covariance.
- $\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}} \gg \boldsymbol{R}\$: if the observation error is much lower than the prior uncertainty, then we trust the observations significantly more than our current prior estimate. This means we apply a strong update to the mean and covariance, moving the mean towards the observations and significantly reducing the magnitude of the covariance.

In consequence, one way of thinking about the Kalman Gain $\boldsymbol{K}$ is to view it as a compromise matrix that defines which side (*prior* or *observations*) -- if any -- the posterior distribution will favour. Of course, this is only one way of viewing the Kalman gain. The interactive figure below shows a geometric perspective on how conditioning a multivariate Gaussian PDF (with different prior uncertainty and observation error) on different values affects its mean and covariance:

````{iframe-figure} ../_static/elements/element_Gaussian_inference.html
:name: Gaussian_inference
:aspectratio: 1 / 1

The Kalman filter's position update relies on three primary variables: the prior uncertainty (yellow), the observation error (blue), and the observation value (green). Adapt these values by dragging the sliders and observe how the compromise solution (the posterior; red) changes in response.
````

