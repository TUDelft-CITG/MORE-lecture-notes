### Importance sampling

We have encountered the concept of importance sampling earlier in this course, but let us briefly revisit it here again to set us up for its use in particle filters. Consider the following example:

#### Example: phone survey

We conduct a phone survey about how much time per week people spent working. We want to derive statistics about the population’s workload. It is a common problem in surveys that the demographics of the survey respondents may not reflect the demographics of the general population:

<br>

```{figure} ../figures/importance_sampling_01.png

---

---
An illustration of importance sampling.
```
<br>

To compensate, we can make use of **importance sampling**, which introduces an importance weight that "corrects" each response by how much its demographic is over- or underrepresented. As we can see, in this example, it substantially increases the weight of adults, and substantially decreases the weight of pensioners, which were overrepresented in the survey:


<br>

```{figure} ../figures/importance_sampling_02.png

---

---
An illustration of importance sampling.
```
<br>

Multiplying the importance weight with the survey fraction of different demographics then lets us compute an aproximate estimate of the mean workload of the general population:

<br>

```{figure} ../figures/importance_sampling_03.png

---

---
An illustration of importance sampling.
```
<br>