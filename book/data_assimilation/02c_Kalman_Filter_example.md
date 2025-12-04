## An example: Tracking the height of a satellite in orbit around earth

````{iframe-figure} ../_static/elements/element_lemniscate_KF.html
:name: element_lemniscate_KF
:aspectratio: 1.75 / 1

Adjust the various sliders and models, and observe how the Ensemble Kalman Filter's ability to track the true state changes in response. Which combinations work well, and why?
````

This sandbox illustrates the influence of forecast error, observation error, assimilation frequency, and model fidelity on the performance of a Kalman filter. SThis element implements the Kalman Filter for a simple model. Specifically, the true state of this model follows a lemniscate (the shape of an infinity symbol). You can choose between the following three models:

- The **true model** is a close approximation to the true lemniscate curve, in which every sample moves a small linear along the lemniscate's tangent vector. This results in a prediction trajectory that closely matches the underlying curve.

- The **extrapolation** setting evaluates the tangent once at every assimilation step, then linearly follows it in-between assimilation steps. This is a quite crude approximation to the true model, especially for long assimilation intervals.

- The **do nothing** setting predicts that the true state does not move at all. 

Explore the different models, and see how their behaviour changes for different assimilation intervals, observation errors, and forecast errors. The log density plot in the top right showcases the log probability of the true state given the state estimate. The higher this quantity is on average, the better your state estimate follows the (unknown) true state.