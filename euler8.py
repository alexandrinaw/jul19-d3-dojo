def is_palindrome(n):
    num_string = str(n)
    return num_string == num_string[::-1]

def find_biggest_palindrome():
    products_of_three_digits = [i*j for i in range(100, 1000) for j in range(100, 1000)]

    palindromes = [x for x in products_of_three_digits if is_palindrome(x)]
    return max(palindromes)
