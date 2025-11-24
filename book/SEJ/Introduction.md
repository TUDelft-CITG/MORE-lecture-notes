# Introduction to expert judgment

As engineers and scientists, we sometimes face situations where data is a challenge. For instance, we need to assess extreme or unforeseen events in the future, such as extreme water levels in the Port of Rotterdam in 2050, or we need to make decisions where there is insufficient data to quantify the variable of interest. In those cases, one option is to rely on experts opinions' to quantify those variables of interest. 

In this chapter, you will study Cooke's method[^1], also called the Classical method or Delft method, which is a *structured expert judgment* method. It assigns a weight to each expert based on their performance when estimating the uncertainty in a number of seed questions whose response is known for the analyst. These weights are then used to aggregate the experts' uncertainty estimates for the variables of interest (unknown variables). Thus, it is assumed that the performance for the seed questions is representative for the questions of interest. The following sections will cover the basics of the method; for an extensive description of the method, the reader is referred to [^2].

Some examples of application of the Classical method are the assessment of reservoir performance[^3], the reconstruction of historical records of water levels in a river[^4] or the estimation of the probabilities of failure of dikes for the Dutch part of the Rhine River[^5]. 

[^1]: Cooke, R. (1991). Experts in uncertainty: Opinion and subjective probability in science. Oxford University
Press.
[^2]: Cooke, R. M. and Goossens, L. L. H. J. (2008). TU Delft expert judgment data base. Reliability Engineering
System Safety 93(5), 657–674.
[^3]: Fathy, M., F. Kazemzadeh Haghighi, and M. Ahmadi
(2024). Uncertainty quantification of reservoir per formance using machine learning algorithms and structured expert judgment. Energy 288, 129906.
[^4]: Kindermann, P. E., Brouwer, W. S., van Hamel, A.,
van Haren, M., Verboeket, R. P., Nane, G. F., Lakhe, H., Prajapati, R., and Davids, J. C. (2020). Return level analysis of the hanumante river using structured expert judgment: A reconstruction of historical water levels. Water 12(11).
[^5]: Rongen, G., Morales-Nápoles, O., and Kok, M. (2022). Expert judgment-based reliability analysis of the dutch flood defense system. Reliability Engineering System Safety 224, 108535.