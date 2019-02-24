from ciphers import rabin_miller


def test_generate_prime_agrees_with_prime_checker():
    """Test that the generateLargePrime function returns a number that isPrime agrees is prime"""
    assert rabin_miller.isPrime(rabin_miller.generateLargePrime())
