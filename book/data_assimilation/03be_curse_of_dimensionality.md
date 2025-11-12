### The curse of dimensionality

Since particle filters do not transform the ensemble, they are reliant on having sufficient samples in close proximity to high-probability regions. This can become a challenge in **high-dimensional settings**. Sampling the state space efficiently requires exponentially more samples with each dimension:

<br>

```{figure} ../figures/curse_of_dimensionality_01.png

---

---
Filling space with samples becomes exponentially more expensive with every new dimension.
```
<br>

This effect grows worse the more dimensions our joint distribution $p(\boldsymbol{x},\boldsymbol{y})$ has. Imagining this process becomes challenging beyond the three spatial dimensions we are used to, but you can gain an intuition by considering the case below: 

<br>

```{figure} ../figures/curse_of_dimensionality_02.png

---

---
What fraction of hypervolume of a unit cube is filled by a unit sphere?
```
<br>

As you can see, a hyper-sphere of radius one occupies increasingly little of the hyper-volume of a hyper-sphere of side length one in high-dimensional space. This contributes to the exacerbation of the curse of dimensionality. 

In practice, particle filters are thus rarely used in systems with more than perhaps a dozen parameters as the necessary ensemble size becomes prohibitive. There are particle filters that are more efficient by leveraging so-called "optimal proposals", but these are beyond the scope of this course. 