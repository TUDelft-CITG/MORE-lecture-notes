### Example: Lemniscate model

To see the EnKF in action, let us consider a small interactive example. In the element below, the true state follows a lemniscate (and infinity sign). Adjust the settings below and observe how and when the EnKF manages to track the true state. Try to develop an intuition for how the different settings affect the behaviour of the filter.

````{iframe-figure} ../_static/elements/element_lemniscate_EnKF.html
:name: lemniscate_enkf
:aspectratio: 1.75 / 1

Adjust the various sliders and models, and observe how the Kalman Filter's ability to track the true state changes in response. Which combinations work well, and why?
````