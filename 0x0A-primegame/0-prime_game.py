#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """isWinner function
    Args:
        x  (int): the number of rounds
        nums  (Array): An Array
    Return: Name of the player that won the most rounds
    """
    if x <= 0 or not nums:
        return None

    # Helper function to get all primes up to max_num
    # using Sieve of Eratosthenes
    def sieve(max_num):
        """Sieve of Erastosthenes
        Args:
            max_nums  (int): maximum number
        """
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if is_prime[p]:
                for i in range(p * p, max_num + 1, p):
                    if is_prime[p]:
                        for i in range(p * p, max_num + 1, p):
                            is_prime[i] = False
            p += 1
        prime_nums = [p for p in range(2, max_num + 1) if is_prime[p]]
        return prime_nums

    # Get the maximun number in nums to limit the sieve range
    max_n = max(nums)
    primes = sieve(max_n)

    # Function to simulate the game for a single round
    def play_game(n):
        if n < 2:
            return 'Ben'  # Maria can not make a move

        current_nums = list(range(1, n + 1))
        move = 0  # for Maria, 1 for Ben

        while True:
            prime_found = False
            for prime in primes:
                if prime > n:
                    break
                if prime in current_nums:
                    prime_found = True
                    current_nums = [
                            num for num in current_nums if num % prime != 0
                            ]
                    break

            if not prime_found:
                break

            move = 1 - move

        return 'Ben' if move == 0 else 'Maria'

    # Play each game and count wins
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overal winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
