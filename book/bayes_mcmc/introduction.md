# Monte Carlo and MCMC methods

Start with how we often propagate uncertainty (e.g. in MUDE): Generate samples from inputs, run through model to get uncertainty in outputs?

- Why does this work → Monte Carlo
- How do we generate the initial samples? (Scipy does it for you, but how?)
- What if we want to sample conditional distributions (e.g. model outputs given a set of data)?