# Information score

The information score $Inf(e)$ measures the degree to which the distribution of an expert is concentrated and is defined as

$$
    Inf(e) = \frac{\sum_{j=1}^m I_j(e)}{m}      
$$

where $m$ is the total number of questions and $I_j(e)$ is given by

$$
    I_j(e) = 0.05 \ln \frac{0.05}{q_5-L^*} + 0.45 \ln \frac{0.45}{q_{50}-q_5} \nonumber \\
    \ \ \ \ \ \ \ \ \ \ + 0.45 \ln \frac{0.45}{q_{95}-q_{50}}+ 0.05 \ln \frac{0.05}{U^*-q_{95}} \nonumber \\
    +\ln (U^* - L^*) \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 
$$

where $L^* = L - k(U-L)$ and and $U^* = U + k(U-L)$, with $L$ and $U$ being the lowest and highest value, respectively, obtained from the different experts and the realization if available and $k=0.1$. 

```{admonition} "Interpreting Information Score"
:class: tip

A high score of $Inf(e)$ means that the expert distribution is concentrated in a small region and, thus, is considered more informative.
```

