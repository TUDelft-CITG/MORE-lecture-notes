# Calibration score

Given that 3 quantiles are elicited, the realizations of the calibration questions should fall on one of the 4 inter-quantile intervals with probability vector $p = (0.05, 0.45, 0.45, 0.05)$.

```{figure} ./figures/P_vector.png
:name: snippet_quest
:width: 600px
---

---
```

This probability vector can be compared with the sample distribution of the expert's inter-quantile intervals $s(e)$ computed as

$$
    s_1(e) = \#\{i|x_i \leq 5\% \ quantile\}/N  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \nonumber\\      
    s_2(e) = \#\{i|5\% < x_i \leq 50\% \ quantile\}/N \nonumber \ \ \\
    s_3(e) = \#\{i|50\% < x_i \leq 95\% \ quantile\}/N  \nonumber \\
    s_4(e) = \#\{i|95\% < x_i \ quantile\}/N  \ \ \ \ \ \ \ \ \ \  \ \ \ \nonumber \\
    s(e) = (s_1, s_2, s_3, s_4) \ \ \ \ \ \ \ \ \ \  \ \ \  \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \
$$

```{figure} ./figures/s_vector.png
:name: snippet_quest
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