"""factorization examples"""


class PrimeFactorization:
    @staticmethod
    def factorization(number):
        ret = []
        for i in range(2, int(number ** 0.5) + 1):
            while number % i == 0:
                ret.append(i)
                number //= i

        if number > 1:
            ret.append(number)

        return ret


prime_factors = PrimeFactorization.factorization(32)
print(prime_factors)
# >>> [2, 2, 2, 2, 2]

prime_factors = PrimeFactorization.factorization(15)
print(prime_factors)
# >>> [3, 5]


class Practice:
    @staticmethod
    def factorization(num):
        ret = []
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                ret.append(i)
                num //= i

        if num >= 2:
            ret.append(num)

        return ret
