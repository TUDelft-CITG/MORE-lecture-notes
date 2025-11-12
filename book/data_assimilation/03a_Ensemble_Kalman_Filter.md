## The Ensemble Kalman Filter

So why is a Monte Carlo approximation useful? We recall that one of the Kalman Filter's key assumptions was that the forecast model and observation model both had to be linear and Gaussian. These assumptions were critical to ensure that the prior distributions, joint distributions, and posteriors all remained Gaussian throughout the filtering recursion.

### Nonlinear dynamics

Working with ensembles allows us to partially circumvent this limitation. We can make use of nonlinear forecast models $M(\dot)$ and observation models $H(\dot)$:

$$
\begin{aligned}
\boldsymbol{Y}_{t}^{(i)} &= H(\boldsymbol{X}_{t}^{(i)}) + \boldsymbol{\gamma}_{t}, && \boldsymbol{\gamma}_{t} &\sim \mathcal{N}(\boldsymbol{\mu}=\boldsymbol{0}, \boldsymbol{\Sigma} = \boldsymbol{R}) \\
\boldsymbol{X}_{t+1}^{(i)} &= M(\boldsymbol{X}_{t}^{(i)}) + \boldsymbol{\epsilon}_{t}, && \boldsymbol{\epsilon}_{t} &\sim \mathcal{N}(\boldsymbol{\mu}=\boldsymbol{0}, \boldsymbol{\Sigma} = \boldsymbol{Q})
\end{aligned}
$$

where $\boldsymbol{X}_{t+1}^{(i)}$ denotes the $i$-th state sample in an ensemble of size $N$, and $\boldsymbol{Y}_{t}^{(i)}$ is its observation prediction equivalent. If $M(\dot)$ and $H(\dot)$ are nonlinear, the ensemble they produce will not follow a multivariate Gaussian distribution. However, we can still fit a mean and a covariance to this ensemble and thereby obtain a Gaussian approximation to the unknown ensemble distribution. This Gaussian approximation then allows us to apply the Kalman Filter's update equations.

We shall see how this works in the following sub-sections.