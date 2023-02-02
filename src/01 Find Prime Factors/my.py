def get_prime_factors(num):
    factors = []
    now = num
    for devisor in range(2, int(num ** 0.5) + 1):
        while now % devisor == 0:
            factors.append(devisor)
            now //= devisor
    if now == num:
        factors.append(num)
    return factors


print(get_prime_factors(630))
print(get_prime_factors(13))
