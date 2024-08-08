#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    def sieve(max_n):
        """
        Generate a list of prime numbers up to max_n
        using the Sieve of Eratosthenes
        """
        is_prime = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if is_prime[p]:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        primes = []
        for p in range(2, max_n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes

    # Determine the maximum value of n across all rounds
    max_n = max(nums)
    primes = sieve(max_n)

    # Results for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Create a list to keep track of the current set
        current_set = [True] * (n + 1)
        prime_count = 0

        for prime in primes:
            if prime > n:
                break
            if current_set[prime]:
                # Maria picks this prime and removes multiples
                prime_count += 1
                for multiple in range(prime, n + 1, prime):
                    current_set[multiple] = False

        # Determine the winner for this round
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
