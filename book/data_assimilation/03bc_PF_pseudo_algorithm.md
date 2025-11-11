### Pseudo-algorithm

With a linear observation model $\boldsymbol{H}$, the EnKF can be implemented as follows:

- Draw $N$ samples from the prior $\boldsymbol{X}_{1} \sim p(\boldsymbol{x}_{1})$

- Set initial weights $\boldsymbol{w}_{1} := [w_{1}^{1},\dots,w_{1}^{N}] = [1/N,\dots,1/N]$

- For timestep $t$ from $1$ to $T$:

    1) **Assimilation step**

        - Update the particle weights

        $$
        \begin{aligned}
        \widehat{w}_{t}^{n} &= w_{t-1}^{n} p(\boldsymbol{y}^{*}_{t}|\boldsymbol{X}_{t}) && \\
        w_{t}^{n} &= \frac{\widehat{w}_{t}^{n}}{\sum_{i=1}^{N}\widehat{w}_{t}^{i}} && \forall n = 1,\dots,N \\
        \end{aligned}
        $$

        - **Optional:** resample the ensemble

        $$
        \begin{aligned}
        &i^{n} \sim \text{Resampling}(\boldsymbol{w}_{t}) && \\
        &\boldsymbol{X}_{t}^{n} \leftarrow \boldsymbol{X}_{t}^{i^{n}}, \quad w_{t}^{n} = 1/N && \forall n = 1,\dots,N 
        \end{aligned}
        $$

    2) **Forecast step**
        - Predict the next states

        $\boldsymbol{X}_{t+1} = \boldsymbol{M}( \boldsymbol{X}_{t}^{*}) + \boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}(\boldsymbol{0},\boldsymbol{Q})$

