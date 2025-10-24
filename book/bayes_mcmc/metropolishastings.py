import numpy as np


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
):
    samples = []
    current_sample = start_value

    for _ in range(num_samples):
        proposed_sample = draw_proposal_sample(current_sample, proposal_cov)

        # Acceptance probability
        acceptance_probability = compute_acceptance_probability(
            current_sample,
            proposed_sample,
            proposal_cov,
            compute_target_logpdf,
            compute_proposal_logpdf,
        )

        # Accept or reject the proposal
        if np.random.rand() < acceptance_probability:
            current_sample = proposed_sample  # Accept the proposal

        samples.append(current_sample)

    return np.array(samples)
