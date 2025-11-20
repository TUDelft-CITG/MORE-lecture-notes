# Introduction
In statistics and data analysis, we begin by observing a process or a phenomenon in nature, e.g., daily rainfall, traffic flow, or displacements, and record it over time, i.e., a time series. To describe the phenomenon observed while preserving the inherent uncertainty, we model the recorded observations via a suitable probability distribution. This allow us to make statistical statements and inferences, e.g., the probability of observing more than 10 mm of rainfall in a day is 0.5. 

For this representation to be valid, the main underlying assumption is that the observations collected are *independent and identically distributed (i.i.d.)*. In other words, each observation is drawn from the same distribution and does not depend on previous or future values. This assumption holds when the underlying process is *stationary* (a formal definition will follow).

When we assume that the observations are stationary and independent, we can describe them statistically by fitting a (non-)parametric probability distribution to the data and using that model to make inferences about the underlying process.

However, there are many cases in which the assumption of stationarity does not hold. For example,  

  * *Mean temperature*. Evidence of a changing climate has shown that temperature increases as a function of atmospheric CO$_2$ concentration.
  * *Daily rainfall*. In certain geographical regions, precipitation exhibits strong seasonal patterns due to climate cycles.
  * *Traffic flow*. Usually, it shows two prominent peaks each day, in the morning and evening rush hours.

In such cases, the condition of independence between observations is no longer satisfied since a specific moment in time, i.e., a specific season, or a given value of another variable, i.e., $CO_2$ level, can provide insight into sequential observations. Overall,  physical drivers, periodicity, or long-term trends lead to the mean, variance, or higher moments evolving systematically. Hence, assuming stationarity can lead to biased inferences.

Hence, the concept of **nonstationary analysis**: modeling data whose statistical characteristics evolve with time or with a physical explanatory variable. 

Here, we will explore two different approaches for addressing nonstationarity in the data. In both cases, we assume that the trend observed in the data can be modelled via a deterministic function. e.g., a linear trend over time or as a function of a physical covariate, for which an explicit mathematical formulation is available.

In the first approach, i.e., *detrending approach*, we separate the deterministic and stochastic components and develop a statistical model only for the stochastic component. In the second approach, i.e., *integrated approach*, the deterministic component is incorporated directly into the statistical model. We will apply the latter approach to extreme value analysis and review examples from the scientific literature.

<div style="background-color:#2b2b2b; border-left: 4px solid #888; padding: 12px; border-radius: 8px; color:#ddd;">

  <strong>Why.</strong> Real-world processes such as rainfall, temperature, or traffic flow often exhibit trends, cycles, or external influences that violate the assumptions of independence and stationarity.  

<strong>What.</strong> We are interested in statistical inferences of a nonstationary process, i.e., when its statistical properties, such as mean or variance, change systematically over time or with an explanatory variable.  

<strong>How.</strong> Nonstationary analysis addresses this behavior by allowing model parameters to vary with time or with physical covariates through explicit deterministic functions.
</div>

