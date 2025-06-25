
# Non-parametric Bayesian Networks

Challenges in all branches of science and engineering involve working in situations where uncertainty plays a significant role. As you have already seen, univariate continuous distributions can assist us in modelling uncertainty associated with a specific variable in order to quantitatively account for it. However, our problems of interest are typically complex and usually involve more than one variable: a _multivariate_ situation.

Consider, for example, when assessing algae blooms in a water body (e.g., a freshwater lake), different variables must be considered, such as nutrients in the water (nitrogen and phosphorus) and their concentration, dissolved oxygen and temperature of the water body, between others. Sometimes (although not frequently), these variables are not related to each other, so we can consider them _independent._ For example, one may assume (for simplicity) that the amount of nitrogen and phosphorous that reaches the lake is not be related to the water temperature of the lake. However, truly _independent_ situations rarely occur in reality, and the variables are _dependent_ on each other. For example, the concentration of nitrogen and phosphorous changes with time and the reaction rates are dependent on the temperature of the water; thus if you are interested in these quantities over time, temperature is certainly a _dependent variable_ of interest.

Dependent relationships can be quantified using _multivariate probability distributions_, as they allow us to model the distribution of not only one variable but several at the same time, thus accounting for their dependence.

**How can I model multivariate distributions?**

You have also seen that when the problem can be reduced to two random variables, bivariate copulas are capable of modelling their joint distribution. However, copulas in higher dimensions are not that convenient and different models need to be applied. Here, we will focus on models that combine bivariate copulas with graph theory to build _multivariate joint distributions_ in more than two dimensions. Specifically, this chapter is focus on non-parametric Bayesian Networks (NPBN), also named Gaussian copula-based Bayesian Networks.

Before you go further in this chapter, you can revisit some pre-knowledge concepts in the chapter [Fundamentals](fund), specifically the concepts of [covariance and correlation](cov) and the [multivariate Gaussian distribution](multi).