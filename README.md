# Pythagorean Sieve on r

A recursive modular sieve for odd prime numbers based on Pythagorean geometry.

This repository contains a reference implementation of the **Pythagorean sieve on the inradius index r**, introduced in:

> **R. Amato**,  
> *A Pythagorean Sieve and a Recursive Modular Characterization of Odd Primes*,  
> International Journal of Applied Mathematics, Vol. 38, No. 12s (2025).

The method provides:
- a geometric reinterpretation of divisibility via the identity `r = (x − d)/2`,
- a modular sieve equivalent to Eratosthenes’ sieve,
- an **ordered generator of odd primes**,
- direct computation of the *n*-th prime.

---

## Installation

```bash
pip install pythagorean-sieve
