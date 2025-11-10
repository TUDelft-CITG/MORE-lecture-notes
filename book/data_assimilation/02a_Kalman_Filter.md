## The Kalman Filter

### The Gaussian special case

Fortunately, there exist a few special cases for which closed-form solutions exist. Perhaps the most important one of these special cases is the **Gaussian distribution**. As you may remember from previous courses, Gaussian PDFs $\mathcal{N}(\boldsymbol{mu},\boldsymbol{\Sigma})$ are defined by two coefficients:
- a **mean** $\boldsymbol{mu}$ that defines the center of a Gaussian distribution, and 
- a **covariance matrix** $\boldsymbol{\Sigma}$ that defines the spread and correlation of the marginal dimensions.
