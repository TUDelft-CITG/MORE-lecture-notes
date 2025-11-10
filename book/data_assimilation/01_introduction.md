# Data Assimilation

It is a trite but true saying that *"all models are wrong, but some are useful"*. And if we know our models are wrong, how can we account rigorously for this imperfection? An answer to this question may be found in **data assimilation** (DA).

Data assimilation is a term that refers to a broad set of Bayesian methods which systematically combine model predictions with observational data. The goal of these methods usually lies in obtaining better estimates of *model states* (usually: time-varying quantities like water table heights, temperatures, vehicle flow, etc) and/or *model parameters* (usually: static quantities like the material properties, subsurface geometries, or reaction rate constants). In practice, data assimilation is correct the drift of real-time dynamical models (e.g., in weather forecasting) or to infer properties of unobservable quantities (e.g., in reservoir engineering). 

Since such problems arise across nearly all scientific domains, data assimilation methods have found application in topics like robotics, the geosciences, financial prediction, environmental science, or civil engineering. These methods do not always share the same name: sometimes DA is referred to as *history matching*, other times as *digital twins*, other times still as *inverse modelling*.

In this chapter, we want to give you an overview to the broad idea behind data assimilation, and give you an introduction to **Bayesian filters**, data assimilation algorithms that correct dynamical models by assimilating real-time data.