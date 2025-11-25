# Aggregation of expert opinions

Once $Cal(e)$ and $I_j(e)$ are calculated, they are combined into the Combined Score as

$$
    CS(e) = Cal(e) \cdot I_J(e)
$$

$CS(e)$ is used to combine the experts' opinions and calculate the Decision Maker using weights. If the same weight is given to all the experts regardless their performance, it is denominated Equal Weight Decision Maker (EWDM). Another option is to calculate the weights of the experts based on their $CS(e)$ as

$$
    w_i = \frac{CS(e_i)}{\sum_{j=1}^N CS(e_j)}
$$

where $w_i$ represents the weights for the expert $i$. It is also possible to restrict that only experts with $Cal(e)>0.05$ are considered in the calculations. Using the computed weights, the probability density function, PDF, and the cumulative distribution function, CDF, for a Decision Maker ($f_{DM}$ and $F_{DM}$, respectively) are given by

$$
    f_{DM} = \sum_{i=1}^N w_if_i \\
    F_{DM} = \sum_{i=1}^N w_iF_i \nonumber
$$

where $f_i$, $F_i$ and $w_i$ refer to the PDF, CDF and the weight of the expert $i$, respectively.