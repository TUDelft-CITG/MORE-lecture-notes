## The Particle Filter

As we have seen in the previous chapters, the EnKF can be a powerful option to implement linear data assimilation in the presence of nonlinear forecast and observation models. However, this often is not enough. In complex systems with complex dynamics, the uncertainties that arise often display non-Gaussian features, which demand true nonlinear data assimilation. Examples of such non-Gaussian features include **multi-modality** or **Pareto frontiers** (i.e., the existence of multiple, distinct or contiguous, equivalent possibilities).

In such settings, a particle filter can be a powerful alternative to the EnKF. In this section, we will introduce the principles behind a particle filter, and discuss its implementation.