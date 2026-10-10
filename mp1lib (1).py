import numpy as np

def bsc(bits, p, rng):
    """Flip each bit independently with probability p."""
    bits = np.asarray(bits)
    errors = rng.random(bits.shape) < p
    return np.where(errors, 1 - bits, bits)


def packet_errors(n_pkt, n_bits, p, rng):
    """Simulate the number of bit errors in each packet."""
    return rng.binomial(n_bits, p, size=n_pkt)


def tv_distance(pmf1, pmf2):
    """Calculate the total variation distance between two distributions."""
    return 0.5 * np.sum(np.abs(np.asarray(pmf1) - np.asarray(pmf2)))


def attempts_until_clean(n_trials, q, rng):
    """Simulate the number of attempts until the first successful transmission."""
    return rng.geometric(q, size=n_trials)


if __name__ == "__main__":
    test_rng = np.random.default_rng(0)
    print(packet_errors(3, 1000, 0, test_rng))
    print(tv_distance([0.5, 0.5], [0.5, 0.5]))
    print(tv_distance([1, 0], [0, 1]))
    