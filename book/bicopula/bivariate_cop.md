## Bivariate Copulas
To statistically describe dependent variables, we rely on the following components:

- **Marginal distributions**:  
  $f_X(x)$ and $f_Y(y)$, which describe the univariate behavior of $X$ and $Y$, respectively.  

- **Joint density function**:  
  $f_{X,Y}(x,y)$, which models the joint occurrence of the pair $(X, Y)$.  

- **Conditional distributions**:  
  $f(x \mid y_0)$ and $f(y \mid x_0)$, which describe the distribution of one variable (e.g., 
  $X$) when conditioned on a specific value of the other (e.g., $Y = y_0$).  

Together, these components form the foundation for analyzing and modeling multivariate dependencies (specifically bivariate), serving as a bridge between univariate analysis and more advanced multivariate statistical modeling.

```{figure} ..//bicopula/multivariate_elements.jpg

---

---
Graphical representation of bivariate elements for a statistical description of dependent variables.
```

We often have good knowledge of univariate distributions, such as the normal, gamma, or beta families, and these can be used to model marginal distributions \(f_X(x)\) and \(f_Y(y)\). When no suitable parametric form is available, the empirical cumulative distribution function provides a nonparametric alternative. However, specifying the marginals is only part of the task. We also want to model the joint distribution. In particular, we want a flexible way to model the joint behaviour between variables including asymmetries in their association and that is not constrained by the particular shapes or scales of the marginals.

To remove the effect of the marginals on the dependence structure, we rely on the probability integral transform (as we have seen in the previous setion), which maps each variable through its own cumulative distribution function. This produces new variables with uniform marginals on $[0,1]$, effectively removing the influence of scale and marginal behavior. What remains is the pure dependence structure, which can be modeled independently of the margins.

A **copula** is precisely the tool that captures this idea. More formally, a copula is the joint distribution function of standard uniform variables. Thus, it describes the dependence between random variables free from the influence of their individual marginal distributions. In the bivariate case, a copula $C$ is a distribution function defined on $[0,1] \times [0,1]$ with uniform marginals. If the copula is continuous, its density \(c\) is obtained by differentiating:

$$
c(u_1, u_2) = \frac{\partial^2}{\partial u_1 \, \partial u_2} ,
\qquad (u_1, u_2) \in [0,1] \times [0,1].
$$

The usefulness of copulas is guaranteed by **Sklar’s Theorem**, which states that any multivariate distribution $F_{X,Y}$ with marginals $F_X$ and $F_Y$ can be written as

$$
F_{X,Y}(x,y) = C(F_X(x), F_Y(y)).
$$

Conversely, combining any copula with any pair of marginal distributions yields a valid joint distribution. This result formally separates marginal behavior from dependence and provides a flexible and powerful framework for modeling multivariate data.


## Sklar's Theorem
