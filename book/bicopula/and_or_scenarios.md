## AND and OR Hazard Scenarios

In the multivariate framework, there is no one-to-one relationship between marginal quantiles and the corresponding joint return period. While the return period in a univariate context is defined as the inverse of the exceedance probability of a threshold, in the multivariate case the notion of *exceedance* is no longer unique because hazardous events may occur in different regions of the joint space. A *hazard scenario* specifies how exceedance is defined for a pair of variables, i.e., which combinations of values are considered jointly hazardous. 

Two widely used hazard scenarios are the **AND** scenario (both variables exceed their thresholds simultaneously) and the **OR** scenario (at least one variable exceeds its threshold). These scenarios correspond to different definitions of multivariate exceedance probability and therefore lead to different joint return periods even when the same marginal quantiles are used. Copulas allow us to compute these probabilities through the dependence structure encoded in the copula function $C$.

### AND scenario (both variables exceed threshold)
In this hazard scenario, an event is hazardous only if both variables exceed their respective thresholds. The joint exceedance probability is:
$$
P(X_1 > x_1,\; X_2 > x_2)
= 1 - u_1 - u_2 + C(u_1, u_2),
$$
and the corresponding return period is:
$$
T_{\text{AND}} 
= \frac{1}{1 - u_1 - u_2 + C(u_1, u_2)}.
$$

### OR scenario (at least one variable exceeds threshold)
Here, an event is hazardous if either variable exceeds its threshold. The exceedance probability becomes:
$$
P(X_1 > x_1 \;\text{or}\; X_2 > x_2)
= 1 - C(u_1, u_2),
$$
leading to the return period:
$$
T_{\text{OR}} 
= \frac{1}{1 - C(u_1, u_2)}.
$$



```{figure} ..//bicopula/AndOr_fig.png

---

---
AND (red) and OR (blue) hazard scenarios
```