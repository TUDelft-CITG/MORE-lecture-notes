# Estimation of vine-copulas

Estimating the parameters of a vine copula is usually done *recursively* with the likelihood principle. The likelihood of a simplified  vine copula with parameters $\mathbf{\theta} = \{\theta_e, e \in E\}$and data $\textbf{u}$ is:

$$
    l(\mathbf{\theta}|\textbf{u}) = \prod_{k=1}^n \prod_{i=1}^{d-1}\prod_{e\in E_i}
c_{a_e,b_e;D_e}\left(C_{a_e |D_e}(u_{k,a_e}|\textbf{u}_{k,D_e}),C_{b_e |D_e}(u_{k,b_e}|\textbf{u}_{k,D_e})\right)    
$$

Notice that the associated parameters are not explicitly written in the likelihood equation but they are required in the sequential estimation. The estimation is done as follows. 

- Denote by $\theta_e$ the copula parameters for edge $e=(a_e,b_e|D_e)$ for all edges in the regular vine. 
- Let $\theta(T_i)$ be the parameters associated with $T_i$ in the regular vine and $\hat{\theta}(T_i)$
- Let $\hat{\theta}(T_{1\ldots,i-1})$ denote the collection of copula parameters estimated from $T_1$ to $T_{i-1}$ in the vine copula.

The sequential estimate of $\theta_e$ for edge $e=(a_e,b_e;D_e)$ in tree $T_i$ is based on the *pseudo-observations*

$$
    u_{k,a_e,|D_e,\hat{\theta}(T_{1,\ldots,i-1})}=C_{a_e|D_e}\left(u_{k,a_e}|u_{k,D_e},\hat{\theta}(T_{1,\ldots,i-1})\right) 
$$

$$
    u_{k,b_e,|D_e,\hat{\theta}(T_{1,\ldots,i-1})}=C_{b_e|D_e}\left(u_{k,b_e}|u_{k,D_e},\hat{\theta}(T_{1,\ldots,i-1})\right)    
$$

for $k=1,\ldots,n$, $\hat{\theta_e}$ is estimated by maximizing 

$$
\prod_{k= 1}^n 
c_{a_e,b_e;D_e}\left(u_{k,b_e,|D_e,\hat{\theta}(T_{1,\ldots,i-1})},u_{k,b_e,|D_e,\hat{\theta}(T_{1,\ldots,i-1})}\right)        
$$
    
Estimating the parameters of a particular vine copula as discussed up to there might seem straightforward. However, a big challenge is that there are too many regular vines! 

It is well known in the vine-copula community that there are $\frac{d!}{2}2^{\binom{d-2}{2}}$ [^1] regular vines on $d$ nodes. For 3 variables these are three regular vines, quite straightforward; for 4 variables there are already 24 regular vines. 480 for 5 variables, and 23,040 regular vines for 5 variables. To fit them all up to here seems possible on a personal computer. However, for 7 variables there are already 2,580,480 regular vines. Fitting them all to a particular data set requires the use of high performance computing for ease. Fitting all possible regular vines on 8 nodes to a data set is challenging in general since there are  660,602,880 of them! 
There are 380,507,258,880. To give you some perspective it is estimated that the Milky Way contains about 100–400 billion stars. Because there are so many regular vines on $d$ variables, algorithms to fit regular vines to data have been proposed, although, seldom benchmark. The most common algorithm for fitting a regular vine to data is usually called  Dißmann's algorithm. 

[^1]: Morales-Nápoles (2010). Counting Vines. In: Dependence Modeling: Vine Copula Handbook, pages 189-218. https://doi.org/10.1142/9789814299886_0009