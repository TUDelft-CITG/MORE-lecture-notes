# Monte Carlo methods and MCMC

From previous courses (e.g., MUDE), you might be familiar with the practical approach of propagating uncertainty by drawing random samples of input variables, running them through a model, and analyzing the resulting spread of outputs.
This *forward Monte Carlo* approach is widely used.

But why does this sampling-based approach actually work?
How do we generate the random samples we need in the first place?
And what can we do when this simple approach no longer works — for example, when we want samples from conditional distributions, or when the problem is high-dimensional and naive sampling becomes inefficient?

This chapter addresses these questions.
We begin with the idea of Monte Carlo integration, then explore how to generate samples from arbitrary probability distributions.
Finally, we look at cases where direct sampling becomes difficult, leading to Markov chain Monte Carlo (MCMC) methods.