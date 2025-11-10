## An example: Tracking the height of a satellite in orbit around earth

This sandbox illustrates how observation and forcast error affect the tracking performance of an analytic Kalman filter for a satellite in orbit. The model predicts a perfect geo-synchronous orbit, whereas the true trajectory wobbles a fair bit. A data assimilation algorithm like the Kalman filter can recursively improve the model's predictions with the help of position measurements. Experiment with the following elements:

````{iframe-figure} ../_static/elements/element_Kalman_filter.html
:name: Gaussian_inference
:aspectratio: 2 / 1

Adjust the sliders for the observation error and forecast error, and see how the Kalman Filter's ability to track the true state changes in response. Which settings yield the highest log density?
````

- Toggling the **assimilate** checkbox begins begins position measurements, which pulls the model's position estimate towards observations which may or may not be closer to the true position of the satellite. Assimilation steps reduce uncertainty, and will eventually zero in on a (potentially compromised) position estimate in absence of forecast error.

- The **observation error** slider adjusts the standard deviation of the assumed observation error. Higher values reduce confidence in the assimilated measurements, limiting the influence of the observations on the position estimate and limiting the reduction in uncertainty during the observation steps. Lower values increase confidence in the measurements, and generally cause the position estimate to snap closer to the measurements during assimilation.

- The **forecast error** slider controls the model's forecast error. The forecast error represents the confidence in the validity of the model. Higher values increase uncertainty during prediction more substantially, generally leading to less confident predictions. Conversely, lower values represent greater confidence in the model and do not increase uncertainty in the position estimate as much.

The orange horizontal line in the top right subplot represents the average log density of the true state evaluated at the filter's position estimate. In most real system's, this quantity cannot be calculated, as the true state is unknown. For this synthetic experiment, however, it allows us to quantify the filter performance. Try to find a combination of observation and forecast errors that maximizes this log density and remains stable over extended periods of time.