## The detrending approach
In the detrending, approach we separate a time series $X_t$ into **deterministic** and **stochastic** components. In other words, the time series $X_t$ can be expressed as the sum of a deterministic component $ D(t) $, which captures the systematic effects such as trends or seasonality, and a stochastic component $ Y_t $:

$$
X_t = D(t) + Y_t
$$

By estimating $D(t)$ and removing it from $X_t$, the stochastic component $Y_t$ can be analyzed using standard statistical models, which require the data to be stationary.

For the specific case of a linear trend in the data, which could be tested for significance using the MK trend test, $X_t$ can be written as:
$$ X_t = \beta_0 + \beta_1 t + Y_t$$

where $\beta_0$ and $\beta_1$ are the intercept and slope of the deterministic component. In this framework, one can estimate $\beta_0$ and $\beta_1$ (e.g., using least squares), subtract the trend from the observations, and then develop statistical models exclusively for  $Y_t$. This approach is particularly useful when the focus is on understanding variability or extremes in the stochastic part without being influenced by the underlying trend.

Following a similar approach to the example of linear trend, data with a strong seasonal signal can be investigated, e.g., monthly temperature. In this case, $D(t)$ can be modeled as a *sinusoidal function*.
