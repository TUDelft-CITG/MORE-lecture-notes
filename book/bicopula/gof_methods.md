# Goodness-of-Fit Methods for Copulas

Goodness-of-fit (GoF) methods are used to evaluate how well a chosen copula model represents the dependence structure observed in the data. The general rationale is to compare empirical quantities with their theoretical counterparts derived from the selected model. The best-fitting copula is the one that most closely matches the empirical dependence observed in the data.

Here we summarize some of the most common GoF methods for copulas. The underlying assumption is that the marginal distributions have already been checked and adequately fitted, so that the focus is on modeling the dependence structure.

- **Cramér–von Mises statistic:** A general-purpose method that compares the empirical copula with the theoretical copula across the entire unit square. It provides a measure of the overall discrepancy between the model and the data.

- **Semi-correlation methods:** These methods focus specifically on the tails of the distribution. By dividing the data into quadrants, they investigate correlations within specific regions of the copula, allowing for a more detailed assessment of tail dependence.


Another method is the **Akaike Information Criterion (AIC).** Compared to the others, this is relative measure used for model comparison. While the absolute value of AIC does not carry an intrinsic meaning, it allows selecting the model that best balances fit and complexity among competing alternatives.


## Cramer Von Mises Test

This metric quantifies the distance between the empirical copula and the selected theoretical copula.

$$
CM_n = n \sum_{i = 1}^{n} \left( C_n(u_{1,i}, u_{2,i}) - C_{\theta}(u_{1,i}, u_{2,i}) \right)^2
$$

where $C_n$ and $C_{\theta}$ denote the empirical and theoretical copulas, respectively. A smaller value of $CM_n$ indicates a better fit, as it implies that the theoretical copula is closer to the empirical one (i.e., to the observed data).


## Semi-correlation

Semi-correlation investigates the dependence structure separately within each of the four quadrants of the copula domain. It is used to assess the ability of copula models to capture asymmetry (or symmetry) in the observed data.

The procedure consists of comparing the semi-correlations computed from the empirical data with those derived from the selected theoretical copulas. The closer the semi-correlations in each quadrant are between the theoretical copula and the empirical data, the better the model fit.

To compute the semi-correlation, the following steps are undertaken:

- Transform the uniform data using the standard normal distribution.
- Partition the transformed data into the four quadrants:  
  
  $$
  (n_{u_1} > 0,\; n_{u_2} > 0),\quad
  (n_{u_1} < 0,\; n_{u_2} > 0),\quad
  (n_{u_1} < 0,\; n_{u_2} < 0),\quad
  (n_{u_1} > 0,\; n_{u_2} < 0)
  $$
  
- Estimate the semi-correlation (Pearson's correlation coefficient) within each quadrant.
- Compare the resulting correlations.


## Aikaike Information Criterion 

The Aikaike Information Criterion (AIC) is a relative measure of dependence and it is used to compare different models. The smaller the AIC, the better the model fits the data. <br>

$AIC = 2k-2\ln({\hat {L}})$ <br>

where ${\hat {L}}$ is the likelihood function and $k$ is the number of parameters. Note that the term $k$ serves as a penalty parameter reflecting the principle of parsimony. Accordingly, the criterion favors more parsimonious models, i.e., those with fewer parameters, over more complex specifications.
