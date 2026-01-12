if __name__ == "__main__":
    plist = primes_up_to_r_segmented(100, segment_size=100_000)
    print(plist)
    print("count =", len(plist))
    print("734th prime =", nth_prime_r(734))
