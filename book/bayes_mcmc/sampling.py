import numpy as np
import scipy.stats as stats


def compute_acceptance_probability(
    current_sample,
    proposed_sample,
    proposal_cov,
    compute_target_logpdf,
    compute_proposal_logpdf,
):
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
