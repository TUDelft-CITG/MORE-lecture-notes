## The Kalman Filter

### The Gaussian special case

Fortunately, there exist a few special cases for which closed-form solutions exist. Perhaps the most important one of these special cases is the **Gaussian distribution**. As you may remember from previous courses, Gaussian PDFs $\mathcal{N}(\boldsymbol{mu},\boldsymbol{\Sigma})$ are defined by two coefficients:
- a **mean** $\boldsymbol{mu}$ that defines the center of a Gaussian distribution, and 
- a **covariance matrix** $\boldsymbol{\Sigma}$ that defines the spread and correlation of the marginal dimensions.

What makes the Gaussian case special is that the marginalization and conditioning of a Gaussian PDF always return another Gaussian PDF. In fact, both operations reduce to simple manipulations of the mean and the covariance:

#### Marginalization

Assume that we have a mean and a covariance matrix in three dimensions, defined as:

$$
\mathcal{N}\left(\boldsymbol{x} = \left[ \begin{matrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\mu_{1} \\
\mu_{2} \\
\mu_{3} \\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\sigma_{1}^2 && \Sigma_{1,2} && \Sigma_{1,3} \\
\Sigma_{2,1} && \sigma_{2}^2 && \Sigma_{2,3} \\
\Sigma_{3,1} && \Sigma_{3,2} && \sigma_{3}^2 \\
\end{matrix} \right]\right) 
$$

Marginalizing out $x_{2}$ then reduces to simply deleting the corresponding entry in $\boldsymbol{\mu}$ and the corresponding rows and columns in $\boldsymbol{\Sigma}$:

$$
\begin{aligned}
p(x_1,x_3) &= \int \mathcal{N}\left(\boldsymbol{x} = \left[ \begin{matrix}
x_{1} \\
x_{2} \\
x_{3} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\mu_{1} \\
\mu_{2} \\
\mu_{3} \\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\sigma_{1}^2 && \Sigma_{1,2} && \Sigma_{1,3} \\
\Sigma_{2,1} && \sigma_{2}^2 && \Sigma_{2,3} \\
\Sigma_{3,1} && \Sigma_{3,2} && \sigma_{3}^2 \\
\end{matrix} \right]\right) d x_{2} = \\
&\mathcal{N}\left(\boldsymbol{x} = \left[ \begin{matrix}
x_{1} \\
x_{3} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\mu_{1} \\
\cancel{\mu_{2}} \\
\mu_{3} \\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\sigma_{1}^2 && \cancel{\Sigma_{1,2}} && \Sigma_{1,3} \\
\cancel{\Sigma_{2,1}} && \cancel{\sigma_{2}^2} && \cancel{\Sigma_{2,3}} \\
\Sigma_{3,1} && \cancel{\Sigma_{3,2}} && \sigma_{3}^2 \\
\end{matrix} \right]\right) = \\
&\mathcal{N}\left(\boldsymbol{x} = \left[ \begin{matrix}
x_{1} \\
x_{3} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\mu_{1} \\
\mu_{3} \\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\sigma_{1}^2 && \Sigma_{1,3} \\
\Sigma_{3,1} && \sigma_{3}^2 \\
\end{matrix} \right]\right)
\end{aligned}
$$

#### Conditioning

Likewise, conditioning can be implemented with a manipulation of the mean and covariance matrix. In this case, it reduces to two short equations using linear algebra. Let $p(\boldsymbol{x},\boldsymbol{y})$ be defined as a Gaussian joint distribution:

$$
\mathcal{N}\left(\left[ \begin{matrix}
\boldsymbol{y} \\
\boldsymbol{x} \\
\end{matrix} \right], \boldsymbol{\mu} =  \left[ \begin{matrix}
\boldsymbol{\mu}_{\boldsymbol{y}} \\
\boldsymbol{\mu}_{\boldsymbol{x}}\\
\end{matrix} \right], 
\boldsymbol{\Sigma} = \left[ \begin{matrix}
\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{y}} && \boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{x}} \\
\boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{y}} && \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{x}} \\
\end{matrix} \right]\right).
$$

Then, the mean and covariance of a conditional Gaussian distribution $p(\boldsymbol{x}|\boldsymbol{y}^{*})$ can be obtained as:

$$
\begin{aligned}
\boldsymbol{\mu}_{\boldsymbol{x}}^* &= \boldsymbol{\mu}_{\boldsymbol{x}} - \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{y}}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{y}}^{-1}(\boldsymbol{\mu}_{\boldsymbol{y}} - \boldsymbol{y}^*) \\
\boldsymbol{\Sigma}_{\boldsymbol{x}}^* &= \boldsymbol{\Sigma}_{\boldsymbol{x}} - \boldsymbol{\Sigma}_{\boldsymbol{x},\boldsymbol{y}}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{y}}^{-1}\boldsymbol{\Sigma}_{\boldsymbol{y},\boldsymbol{x}}
\end{aligned}
$$