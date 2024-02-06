#   print the prime number from 100 to 200

def prime_number_list():
    prime_numbers = []
    for number in range(100, 201):
        if all(number % i != 0 for i in range(2, number)):
            prime_numbers.append(number)

    return prime_numbers


# print(prime_number_list())


def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# print(is_prime_number(11))


# Write a Sort function to sort the elements in a list

def do_sorting():
    numbers = [2, 1, 5, 6, 4, 7]
    numbers.sort()

    return numbers


print(do_sorting())
