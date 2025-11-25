# Definition of Vine-Copula

Loosely speaking, vine copulas are regular vines whose nodes are associated with random variables and the edges are associated with *constant* conditional copulas. Vine copulas are also often referred to as "*simplified*" vine copulas. In this course we will not treat non-simplified vine copulas, hence, we use only the generic name *vine copula*. Slightly more formally, one may say that the joint distribution $F$ for the $d$ dimensional random vector $\textbf{X}=(X_1,\ldots,X_d)$ is a *vine copula* if a triplet $(\mathcal{F},\mathcal{V},\mathcal{B})$ is specified such that: 


1. $\mathcal{F} = (F_1,\ldots,F_d)$ is a vector of continuous invertible **marginal distribution** functions. 
2. $\mathcal{V}$ is a regular vine.
3. $\mathcal{B} = \{C_e|e\in E_i; i=1,\ldots,d-1\}$, where $C_e$ is a bivariate copula density and $E_i$ is the edge set of $T_i$ in $\mathcal{V}$. If $e=\{a,b\}$, $C_e$ is the copula associated with the conditional distribution of $X_{C_{e,a}}$ and $X_{C_{e,b}}$ given $\textbf{X}_{D_e}=\textbf{x}_{D_e}$. Moreover, $C_e$ does not depend on the specific value of $\textbf{x}_{D_e}$.

This last statement, that $C_e$ does not change for specific values of $\textbf{x}_{D_e}$ is called the *simplifying assumption*. If this assumption is relaxed, then we speak of *non-simplified vine copulas*. The copula $C_e$ corresponding to edge $e$ is denoted $C_{C_{e,a}C_{e,b};D_e}$ and the
corresponding density by $c_{C_{e,a}C_{e,b};D_e}$, respectively. Notice that $D_e$ is the conditioning set in the language of the previous section. 

When the conditoins of the triplet triplet $(\mathcal{F},\mathcal{V},\mathcal{B})$ are met, one may show that there is a unique d dimensional
distribution $F$ with density:

$$
f_{1,...d} (x_1,\ldots,x_d ) = f_1(x_1)\cdots f_d (x_d ) \prod_{i=1}^{d-1}\prod_{e\in E_i}
c_{C_{e,a}C_{e,b};D_e}\left(F_{C_{e,a} |D_e}(x_{C_{e,a}}|\textbf{x}_{D_e} ),F_{C_{e,b} |D_e}(x_{C_{e,b}}|\textbf{x}_{D_e} )\right)    
$$

such that for each $e \in E_i$, $i = 1,\ldots, d-1$, with $e = \{a, b\}$ we have for the
distribution function of $X_{C_{e,a}}$ and $X_{C_{e,b}}$ given $\textbf{X}_{D_e} = \textbf{x}_{D_e}$

$$
F_{C_{e,a},C{e,b}|D_e}(x_{C_{e,a}},x_{C_{e,b}}
|\textbf{x}_{D_e})= C_e\left(F_{C_{e,a}|D_e} (x_{C_{e,a}}
|\textbf{x}_{D_e}),F_{C_{e,b}|D_e}(x_{C_{e,b}}
|\textbf{x}_{D_e}) \right) 
$$

Thus, with the construction up to now, a *simplified regular vine copula* or a (*vine copula* for our purposes) is a regular whose nodes are associated with one dimensional random variables and the edges with (conditional) bivariate copulas that do not depend on the specific value of the conditioning variables. The density of the vine copulacan be written as the product of the individual densities and the (conditional) bivariate copulas attached to the edges of the regular vine.

As can be seen the conditional copulas are an important concept in the construction above. For this reason we remember its definition. 

Let $X$ be a random variable and $\textbf{Y}$ a random vector. Assume they have an absolutely continuous joint distribution. Let $Y_j$ be a component of $\textbf{Y}$ and denote the sub-vector of $\textbf{Y}$ with Let $Y_{-j}$ removed by Let $\textbf{Y}_{-j}$. In this case the conditional distribution of $X$ given $\textbf{Y} = \textbf{y}$ $F_{X|\textbf{Y}}(\cdot| \textbf{y})$ satisfies the following recursion

$$
F_{X|\textbf{Y}} (\cdot| \textbf{y}) = \frac{\partial C_{X,Y_j;\textbf{Y}_{-j}}(F_{X|Y_j}(x|\textbf{y}_{-j}), F_{Y_j|\textbf{Y}_{-j}}(y| \textbf{y}_{-j} ))}{\partial F_{Y_j |\textbf{Y}_{-j}(y_j | \textbf{y}_{-j} })}
$$

where $C_{X,Y_j;Y_{-j}}(\cdot, \cdot| y_{-j} )$ denotes the copula corresponding to $(X,Y_j)$ given $\textbf{Y}_{-j} = \textbf{y}_{-j}$.