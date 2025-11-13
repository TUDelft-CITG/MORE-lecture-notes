import numpy as np
import scipy.stats as stats


def compute_acceptance_probability(
    current_sample,
    proposed_sample,
    proposal_cov,
    compute_target_logpdf,
    compute_proposal_logpdf,
):
    """
    Compute the Metropolis-Hastings acceptance probability for a single proposal.

    Parameters
    ----------
    current_sample
        Current state (1D array).
    proposed_sample
        Proposed state (1D array).
    proposal_cov
        Parameter passed to the proposal log-pdf (e.g. covariance matrix or scalar).
    compute_target_logpdf
        Callable that returns the log of the target density at a given point.
    compute_proposal_logpdf
        Callable that returns the log of the proposal density q(y | x).

    Returns
    -------
    float
        Acceptance probability in [0, 1].
    """
    # Calculate acceptance ratio
    log_target_ratio = compute_target_logpdf(proposed_sample) - compute_target_logpdf(
        current_sample
    )

    log_proposal_ratio = compute_proposal_logpdf(
        current_sample, proposed_sample, proposal_cov
    ) - compute_proposal_logpdf(proposed_sample, current_sample, proposal_cov)

    log_acceptance_ratio = log_target_ratio + log_proposal_ratio

    # Acceptance probability
    return np.minimum(1, np.exp(log_acceptance_ratio))


def sample_metropolis_hastings(
    start_value,
    compute_target_logpdf,
    compute_proposal_logpdf,
    draw_proposal_sample,
    num_samples,
    proposal_cov=1.0,
    rng=None,
):
    """
    Run a Metropolis-Hastings random-walk sampler.

    Parameters
    ----------
    start_value
        Initial state (array-like).
    compute_target_logpdf
        Function returning log(target_pdf(x)).
    compute_proposal_logpdf
        Function returning log(q(y | x)).
    draw_proposal_sample
        Function that draws a proposal y ~ q(· | x). Signature: (x, proposal_cov, rng) -> y
    num_samples
        Number of iterations / samples to produce.
    proposal_cov
        Parameter (e.g. covariance) passed to draw_proposal_sample and compute_proposal_logpdf.
    rng
        Optional numpy random Generator.

    Returns
    -------
    samples, proposals, accepted
        samples: array of length num_samples with the chain states (after accept/reject).
        proposals: array of proposed states (length num_samples).
        accepted: boolean array indicating whether each proposal was accepted.
    """
    # use independent random state if none provided
    if rng is None:
        rng = np.random.default_rng()

    samples = []
    proposals = []
    accepted = []
    current_sample = start_value

    for _ in range(num_samples):
        proposed_sample = draw_proposal_sample(current_sample, proposal_cov, rng=rng)
        proposals.append(proposed_sample)

        # Acceptance probability
        acceptance_probability = compute_acceptance_probability(
            current_sample,
            proposed_sample,
            proposal_cov,
            compute_target_logpdf,
            compute_proposal_logpdf,
        )

        # Accept or reject the proposal
        accept = rng.random() < acceptance_probability
        accepted.append(accept)
        if accept:
            current_sample = proposed_sample  # Accept the proposal

        samples.append(current_sample)

    return np.array(samples), np.array(proposals), np.array(accepted)


def rejection_sampling(
    N, evaluate_target_pdf, evaluate_proposal_pdf, get_proposal_samples
):
    """
    Basic rejection sampling.

    Parameters
    ----------
    N
        Number of proposal samples to draw.
    evaluate_target_pdf
        Function returning p(x) for x (accepts vectorized input).
    evaluate_proposal_pdf
        Function returning q(x) for x (accepts vectorized input).
    get_proposal_samples
        Function that draws N proposal samples. Signature: (N, rng) -> array of shape (N, dim)
    rng
        Optional numpy random Generator.

    Returns
    -------
    proposal_samples, proposal_pdf, u, accept, M
        proposal_samples: array of proposals.
        proposal_pdf: proposal density evaluated at proposals.
        u: uniform draws used for acceptance decision.
        accept: boolean mask of accepted proposals.
        M: scaling constant used (max ratio).
    """
    # Generate samples from the proposal distribution
    proposal_samples = get_proposal_samples(N)

    # Compute the target and proposal pdf for each sample
    target_pdf = evaluate_target_pdf(proposal_samples)
    proposal_pdf = evaluate_proposal_pdf(proposal_samples)

    # Compute the ratio of the pdfs
    ratio = target_pdf / proposal_pdf

    # Determine the scaling constant
    M = ratio.max()

    # Accept or reject samples based on the ratio of the pdfs
    u = stats.uniform.rvs(size=N)
    accept = u < ratio / M
    return proposal_samples, proposal_pdf, u, accept, M
