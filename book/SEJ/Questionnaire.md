# How does the questionnaire for an structure expert judgment elicitation look like?

A questionnaire for an elicitation using Cooke's method contains two types of questions:

- **Seed or calibration questions**. Questions whose answer is or will be known by the analyst. For instance, if I am interested in air temperature, I might ask about the maximum daily temperature next Saturday. I might also want to use data from field or laboratory campaigns that are unknown by the experts.
- **Questions of interest**. Questions whose answer is unknown and are the main outcome of the elicitation: the variables we want to quantify.

For each question, the expert is asked to give some percentiles, typically three: 5\%, 50\%, and 95\%. From now on, we are going to assume that these three percentiles are elicited but note that it can be extended to a higher number of percentiles. 

Recall that 5\% percentile represents the realization of the random variable (values) whose non-exceedance probability is 0.05. Therefore, the 5\% percentile represents the quantity **below** which the expert thinks it is very unlikely to find the realization of the random variable. The 95\% represents then the quantity **above** which the expert thinks it is very unlikely to find the realization of the random variable.

## Looking at the responses of a questionnaire

In {numref}`snippet_quest`, the results for 4 seed questions are shown for 5 experts. There we can already start identifying some things. For instance, expert A is the one with the largest uncertainty for all the questions, as the distance between the 5th and the 95th percentile are the largest. On the other hand, expert E seems to be the most confident in most of the questions, despite for the question 'Question Overrun_fatal'. The expert could have been overconfident in the other questions.

```{figure} ./figures/crop.png
:name: snippet_quest
:width: 600px
---

---
Example of 4 seed questions with 5 experts (A, B, C, D, E). Each panel represents a seed question. The dots represent the 5th, 50th and 95th percentiles given by the expert.
```