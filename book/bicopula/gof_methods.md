# Goodness-of-Fit Methods for Copulas

Goodness-of-fit (GoF) methods are used to evaluate how well a chosen copula model represents the dependence structure observed in the data. The general rationale is to compare empirical quantities with their theoretical counterparts derived from the selected model. The best-fitting copula is the one that most closely matches the empirical dependence observed in the data.

Here we summarize some of the most common GoF methods for copulas. The underlying assumption is that the marginal distributions have already been checked and adequately fitted, so that the focus is on modeling the dependence structure.

- **Cramér–von Mises statistic:** A general-purpose method that compares the empirical copula with the theoretical copula across the entire unit square. It provides a measure of the overall discrepancy between the model and the data.

- **Semi-correlation methods:** These methods focus specifically on the tails of the distribution. By dividing the data into quadrants, they investigate correlations within specific regions of the copula, allowing for a more detailed assessment of tail dependence.


Another method is the **Akaike Information Criterion (AIC).** Compared to the others, this is relative measure used for model comparison. While the absolute value of AIC does not carry an intrinsic meaning, it allows selecting the model that best balances fit and complexity among competing alternatives.

By applying these methods, one can assess and compare different copula models to identify the one that most accurately represents the dependence structure in the data.
 

## semi-correlation
## Cramer Von Mises
