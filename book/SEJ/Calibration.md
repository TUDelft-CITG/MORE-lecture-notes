# Calibration score

Given that 3 quantiles are elicited, the realizations of the calibration questions should fall on one of the 4 inter-quantile intervals with probability vector $p = (0.05, 0.45, 0.45, 0.05)$.

```{figure} ./figures/P_vector.png
:name: p_vector
:width: 600px
---

---
P-vector
```

This probability vector can be compared with the sample distribution of the expert's inter-quantile intervals $s(e)$ computed as

$
    s_1(e) = \#\{i|x_i \leq 5\% \ quantile\}/N \\   
$

$ 
    s_2(e) = \#\{i|5\% < x_i \leq 50\% \ quantile\}/N  \\
$

$
    s_3(e) = \#\{i|50\% < x_i \leq 95\% \ quantile\}/N   \\
$

$
    s_4(e) = \#\{i|95\% < x_i \ quantile\}/N  \\
$

$
    s(e) = (s_1, s_2, s_3, s_4)
$

```{figure} ./figures/S_vector.png
:name: s_vector
:width: 600px
---

---
Example of an empirical s(e).
```

Note that $s(e)$ is computed per expert. The calibration score of each expert $Cal(e)$ can be then computed to assess the discrepancy between $p$ and $s(e)$ as

$$
    Cal(e) = 1 - \chi^2_3(2 n I(s,p)) \\      
    I(s,p) = \sum_{i=1}^4s_i \ln(s_i/p_i) \ \ \ \ \ \nonumber 
$$

where $n$ is the number of calibration questions. Low scores of $Cal(e)$ mean that the expert's assessment is unlikely to be statistically accurate.

## Let's see it with an example

Let's compute the calibration score for expert E using the 8 seed questions in {numref}`snippet_quest2`.

```{figure} ./figures/questions_2.png
:name: snippet_quest2
:width: 600px
---

---
Example of 4 seed questions with 5 experts (A, B, C, D, E). Each panel represents a seed question. The dots represent the 5th, 50th and 95th percentiles given by the expert.
```

First, we compute the $s(E)$  by counting the number of times that the realization falls in a given interquantile range. We obtain

$$
s(E) = (4/8, 3/8, 0, 1/8) \approx (0.5, 0.38, 0, 0.12)
$$

Using $s(E)$, we can compute $I(s,p)$ as

$$
    I(s,p) = 0.5 \ln{\frac{0.5}{0.05}}+0.38 \ln{\frac{0.38}{0.45}}+0 \ln{\frac{0}{0.45}}+0.12 \ln{\frac{0.12}{0.05}} = 1.19
$$

And finally the calibration score for expert E, $Cal(E)$ as

$$
    Cal(e) = 1 - \chi^2_3(2\cdot8\cdot1.19) = 0.00027    
$$

Therefore, expert E has a very low calibration score.

## It's your turn now!

Compute the calibration score for expert A. Which expert is more calibrated when comparing expert A and E? Note that the realization in the top right panel falls in the third interquantile range.


```{admonition} Solution
:class: tip, dropdown

First, we compute the $s(A)$ by counting the number of times that the realization falls in a given interquantile range. We obtain

$$
s(A) = (1/8, 3/8, 3/8, 1/8) \approx (0.12, 0.38, 0.38, 0.12)
$$

Using $s(A)$, we can compute $I(s,p)$ as

$$
    I(s,p) = 0.12 \ln{\frac{0.12}{0.05}}+0.38 \ln{\frac{0.38}{0.45}}+0.38 \ln{\frac{0.38}{0.45}}+0.12 \ln{\frac{0.12}{0.05}} = 0.082
$$

And finally the calibration score for expert A, $Cal(A)$ as

$$
    Cal(A) = 1 - \chi^2_3(2\cdot8\cdot0.082) = 0.73   
$$

Cal(A) = 0.73 >> Cal(E)=0.00027. Therefore, expert A is much more accurate than expert E.

Note that with 8 calibration question is impossible to get a vector $s$ that perfectly matches the vector $p$.
```
.