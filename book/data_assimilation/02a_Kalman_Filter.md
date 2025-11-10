## The Kalman Filter

### The Gaussian special case

Fortunately, there exist a few special cases for which closed-form solutions exist. Perhaps the most important one of these special cases is the **Gaussian distribution**. As you may remember from previous courses, Gaussian PDFs $\mathcal{N}(\boldsymbol{\mu},\boldsymbol{\Sigma})$ are defined by two coefficients:
- a **mean** $\boldsymbol{\mu}$ that defines the center of a Gaussian distribution, and 
- a **covariance matrix** $\boldsymbol{\Sigma}$ that defines the spread and correlation of the marginal dimensions.

What makes the Gaussian case special is that the marginalization and conditioning of a Gaussian PDF always return another Gaussian PDF. In fact, both operations reduce to simple manipulations of the mean and the covariance:

<br>

```{figure} ../figures/13b_Gaussian_conditioning.gif

---

---
The marginal and conditional PDFs of a Gaussian PDF are also Gaussian PDFs.
```
<br>

#### Marginalization

Assume that we have a mean and a covariance matrix in three dimensions, defined as:

$$
\mathcal{N}\left(\boldsymbol{x} = \left[ \begin{matrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\mu_{1} \\
\mu_{2} \\
\mu_{3} \\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\sigma_{1}^2 && \Sigma_{1,2} && \Sigma_{1,3} \\
\Sigma_{2,1} && \sigma_{2}^2 && \Sigma_{2,3} \\
\Sigma_{3,1} && \Sigma_{3,2} && \sigma_{3}^2 \\
\end{matrix} \right]\right) 
$$

Marginalizing out $x_{2}$ then reduces to simply deleting the corresponding entry in $\boldsymbol{\mu}$ and the corresponding rows and columns in $\boldsymbol{\Sigma}$:

$$
\begin{aligned}
p(x_1,x_3) &= \int \mathcal{N}\left(\boldsymbol{x} = \left[ \begin{matrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\mu_{1} \\
\mu_{2} \\
\mu_{3} \\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\sigma_{1}^2 && \Sigma_{1,2} && \Sigma_{1,3} \\
\Sigma_{2,1} && \sigma_{2}^2 && \Sigma_{2,3} \\
\Sigma_{3,1} && \Sigma_{3,2} && \sigma_{3}^2 \\
\end{matrix} \right]\right) d x_{2} = \\
&\mathcal{N}\left(\boldsymbol{x} = \left[ \begin{matrix}
x_{1} \\
x_{3} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\mu_{1} \\
\cancel{\mu_{2}} \\
\mu_{3} \\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\sigma_{1}^2 && \cancel{\Sigma_{1,2}} && \Sigma_{1,3} \\
\cancel{\Sigma_{2,1}} && \cancel{\sigma_{2}^2} && \cancel{\Sigma_{2,3}} \\
\Sigma_{3,1} && \cancel{\Sigma_{3,2}} && \sigma_{3}^2 \\
\end{matrix} \right]\right) = \\
&\mathcal{N}\left(\boldsymbol{x} = \left[ \begin{matrix}
x_{1} \\
x_{3} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\mu_{1} \\
\mu_{3} \\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\sigma_{1}^2 && \Sigma_{1,3} \\
\Sigma_{3,1} && \sigma_{3}^2 \\
\end{matrix} \right]\right)
\end{aligned}
$$

#### Conditioning

Likewise, conditioning can be implemented with a manipulation of the mean and covariance matrix. In this case, it reduces to two short equations using linear algebra. Let $p(\boldsymbol{x},\boldsymbol{y})$ be defined as a Gaussian joint distribution:

$$
\mathcal{N}\left(\left[ \begin{matrix}
\boldsymbol{y} \\
\boldsymbol{x} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\boldsymbol{\mu}_{\boldsymbol{y}} \\
\boldsymbol{\mu}_{\boldsymbol{x}}\\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{y}} && \boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{x}} \\
\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{y}} && \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}} \\
\end{matrix} \right]\right).
$$

Then, the mean and covariance of a conditional Gaussian distribution $p(\boldsymbol{x}|\boldsymbol{y}^{*})$ can be obtained as:

$$
\begin{aligned}
\boldsymbol{\mu}_{\boldsymbol{x}}^* &= \boldsymbol{\mu}_{\boldsymbol{x}} - \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{y}}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{y}}^{-1}(\boldsymbol{\mu}_{\boldsymbol{y}} - \boldsymbol{y}^*) \\
\boldsymbol{\Sigma}_{\boldsymbol{x}}^* &= \boldsymbol{\Sigma}_{\boldsymbol{x}} - \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{y}}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{y}}^{-1}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{x}}
\end{aligned}
$$

### Gaussian Filtering: The Kalman Filter

These properties make Gaussian distributions an attractive choice for Bayesian inference. The Bayesian filter that leverages this special case is known as the **Kalman Filter** (KF). 

#### The filtering recursion

All filters fundamentally consist of two steps. We assume that we start with a state prior $\boldsymbol{x}_0$, where the subscript denotes that this variable describes the system state at time $t=0$, which follows a prior distribution $p(\boldsymbol{x}_0)$. We set the time $t=0$ and define a **forecast model** $p(\boldsymbol{x}_{t}|\boldsymbol{x}_{t-1})$ and an **observation model** $p(\boldsymbol{y}_{t}|\boldsymbol{x}_{t})$. A filter then repeats two stages:

1) **Assimilation step**
    - Augment the current state prior with the observation predictions

        $p(\boldsymbol{x}_{t},\boldsymbol{y}_{t}|\boldsymbol{y}_{1:t-1}^{*}) = \underbrace{p(\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t-1}^{*})}_{\text{filtering forecast}} \overbrace{p(\boldsymbol{y}_{t}|\boldsymbol{x}_{t})}^{\text{observation model}}$

    - Condition on the new observation

        $\underbrace{p(\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*})}_{\text{filtering posterior}} = p(\boldsymbol{x}_{t},\boldsymbol{y}_{t}|\boldsymbol{y}_{1:t-1}^{*}) / p(\boldsymbol{y}_{t}^{*}|\boldsymbol{y}_{1:t-1}^{*})$

    - Go to Step 2

2) **Forecast step**
    - Predict the next state

        $p(\boldsymbol{x}_{t+1},\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*}) = \underbrace{p(\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*})}_{\text{filtering posterior}} \verbrace{p(\boldsymbol{x}_{t+1}|\boldsymbol{x}_{t})}^{\text{forecast model}}$

    - Integrate out the past state

        $\underbrace{p(\boldsymbol{x}_{t+1}|\boldsymbol{y}_{1:t}^{*})}_{\text{filtering forecast}} = \int p(\boldsymbol{x}_{t+1},\boldsymbol{x}_{t}|\boldsymbol{y}_{1:t}^{*}) d \boldsymbol{x}_{t}$

    - Increment the time step $t := t+1$ and go back to Step 1

#### The Kalman filter

In the Kalman filter, we implement these operations for Gaussian PDFs. For this to work, we need the following assumptions:

1) The prior is Gaussian
2) The forecast model is linear and Gaussian
3) The observation model is linear and Gaussian

Together, these assumptions guarantee that all distributions involved are always Gaussian, which allows us to run the Kalman filter infinitely.

The interactive figure below shows how conditioning a multivariate Gaussian PDF on different values affects its mean and covariance:

````{iframe-figure} ../_static/elements/element_Gaussian_inference.html
:name: Gaussian_inference
:aspectratio: 1 / 1

The Kalman filter's position update relies on three primary variables: the prior uncertainty (yellow), the observation error (blue), and the observation value (green). Adapt these values by dragging the sliders and observe how the compromise solution (the posterior; red) changes in response.
````

