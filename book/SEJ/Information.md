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

A high score of $Inf(e)$ means that the expert distribution is concentrated in a small region. Therefore, it is considered more informative.

```

## Let's see it with an example

Let's compute the information score for expert E using the 8 seed questions in the following table. 

| Question | Realization | 5\% | 50\% |95\% |
| ----- | ----- | ----- | ----- | ----- |
| 1 | 25 | 10 | 40 | 60 |
| 2 | 0.0011 | 0.002 | 0.02 | 0.05 |
| 3 | 214 | 5 | 80 | 150 |
| 4 | 10840 | 30000 | 60000 | 200000 |
| 5 | 1 | 5 | 13 | 30 |
| 6 | 6 | 2 | 15 | 50 |
| 7 | 20 | 30 | 45 | 60 |
| 8 | 0.23 | 3 | 8 | 12 |

First, we compute the  $L^*$ and $U^*$. **Note that we assume we only have one expert when computing the support, $L^*$ and $U^*$. If we had more than one expert, they should be considered in their computation.**

$L = [10, 0.0011, 5, 10840, 1, 2, 20, 0.23]$

$U = [60, 0.05, 214, 200000, 30, 50, 60, 12]$

$L^* = L - k(U-L) = L - 0.1 (U - L) = [5, -0.00379, -15.9, -8076, -1.9, -2.8, 16, -0.947]$

$U^* = U + k(U-L) = L - 0.1 (U - L) = [65, 0.0549, 234.9, 218916, 32.9, 54.8, 64, 13.18]$

Using the computed support, we can compute $I_j(E)$ for each question as

$$
I_1(E) = 0.05 \ln \frac{0.05}{10-5} + 0.45 \ln \frac{0.45}{40-10} \\
+ 0.45 \ln \frac{0.45}{60-40}+ 0.05 \ln \frac{0.05}{65-60} +\ln (65 - 5) = 0.037
$$

And similarly for the missing questions obtaining $I_2(E)=0.055$, $I_3(E)=0.278$, $I_4(E)=0.323$, $I_5(E)=0.171$, $I_6(E)=0.124$, $I_7(E)=0.214$, $I_8(E)=0.205$.

Finally, we can compute $Inf(E)$ as

$$
    Inf(e) = (0.037+0.055+0.278+0.323+0.171+0.124+0.214+0.205)/8=0.176
$$

Note that the Information Score is not upper bounded in 1. The value fo the information score for expert E is quite low.



## It's your turn now!

Compute the information score assuming we have two experts A and E. You have the answers for expert A in the following table. Which expert is more informative when comparing expert A and E? Note that you need to requantify the Information Score of expert E with the new support.

| Question | Realization | 5\% | 50\% |95\% |
| ----- | ----- | ----- | ----- | ----- |
| 1 | 25 | 1 | 6 | 20 |
| 2 | 0.0011 | $10^{-9}$ | $10^{-4}$ | 0.002 |
| 3 | 214 | 5 | 150 | 900 |
| 4 | 10840 | 1000 | 10000 | 65000 |
| 5 | 1 | 5 | 65 | 95 |
| 6 | 6 | 0.1 | 6 | 50 |
| 7 | 20 | 2 | 40 | 99 |
| 8 | 0.23 | 0.1 | 5 | 40 |

```{admonition} Solution
:class: tip, dropdown

$L^* = [-4.9, -0.005, -84.5, -18900, -8.4, -4.89, -7.7, -3.89]$

$U^* = [65.9, 0.055, 989.5, 219900, 104.4, 54.99, 108.7, 43.99]$

For expert A and E, respectively:

$I_j(A)=[1.05, 3.55,0.29,1.26,0.093,0.41,0.04,0.4]$

$I_j(E)=[0.14, 0.067, 1.54,0.36,1.15,0.14,0.93,1.16]$

And finally the Information Scores for each expert:

$Inf(A) = 0.89$

$Inf(E) = 0.69$

Therefore, expert A is more informative than expert E, although the difference is not too large.

```
