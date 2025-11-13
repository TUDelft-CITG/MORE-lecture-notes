### Resampling

In the previous section, we have seen how we can use importance sampling to represent one distribution with samples from a different distribution. However, this only works a while. As we continue to assimilate more and more data, the posterior will drift away from the prior, and eventually only a single particle will carry all weight, which loses information about uncertainty. This process is known as **weight degeneracy**.

To combat weight degeneracy, particle filters make use of **resampling**. Resampling draws new unweighted i.i.d. samples from the weighted ensemble, which concentrates samples in high-probability regions. One of the simplest resampling strategies is multinomial resampling, which simply draws new samples from the weighted ensemble:

1) Create an empirical CDF from the weighted samples

    $$C_{k} = \sum_{i=1}^{k} w_{i}, \quad k = 1,\dots,N$$

2) Draw a random parent index from the ECDF

    $$u_{n} \sim \text{Uniform}(0,1), \quad \min j\text{ s.t. }u_{n} \leq C_{j}$$

3) Inherent parent's weights

    $$\boldsymbol{X}^{n} \leftarrow \boldsymbol{X}^{j}, \quad w_{n} = \frac{1}{N}$$

#### Example: resampling the 2D distribution

Note that resampling fundamentally does not improve the **effective sample size** (ESS). In fact, resampling generally decreases the ESS further. However, it concentrates samples in high-probability regions.

````{iframe-figure} ../_static/elements/element_importance_resampling.html
:name: importance_resampling
:aspectratio: 1.75 / 1

Select a 2D distribution to sample, and then select another distribution you want to approximate with importance sampling then resample. Observe how different resampling schemes reduce the effective sample size. (Here, I used a special form of the ESS that accounts for replicate samples.)
````

#### Stochastic Universal Resampling

Over time, repeated multinomial resampling will also lead to ensemble collapse, as even samples with non-zero weight can randomly fail to be resampled and consequently become lost. **Stochastic Universal Resampling** (SUR) is another resampling strategy but generally results in less loss of sample diversity. SUR only samples a single random offset $\gamma$, then samples the empirical cdf in regular increments.

<br>

```{figure} ../figures/SUR.png

---

---
A schematic illustration of Stochastic Universal Resampling.
```
<br>

SUR is less random and preserves more sample diversity than multinomial resampling:

````{iframe-figure} ../_static/elements/element_resampling.html
:name: importance_resampling_02
:aspectratio: 1.75 / 1

Select a resampling scheme and resample repeatedly to see how the ensemble diversity decays. Click "rejuvenate" to reintroduce diversity. Observe how SUR is less random, and preserves more sample diversity.
````
