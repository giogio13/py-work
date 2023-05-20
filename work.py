def find_smallest_of_three_numbers(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def minimum(x, y, z):
    return min(x, y, z)


def celsius_to_fahrenheit():
    celsius = float(input("ტემპერატურა ცელსიუსში: "))
    fahrenheit = (celsius * 9/5) + 32
    print("ტემპერატურა ფარენგეიტში:", fahrenheit)
def fahrenheit_to_celsius():
    fahrenheit = float(input("ტემპერატურა ფარენგეიტში: "))
    celsius = (fahrenheit - 32) * 5/9
    print("ტემპერატურა ცელსიუსში:", celsius)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if find_prime_numbers(num):
            primes.append(num)


def sum_of_numbers():
    n = int(input("რიცხვი: "))
    sum_result = (n * (n + 1)) // 2
    print("რიცხვების ჯამი 1-დან", n, "მდე არის:", sum_result)

def arithmetic_mean():
    n = int(input("რიცხვი: "))
    mean = n / 2
    print("საშუალო არითმეტიკული 1-დან", n, "მდე არის:", mean)

def sum_of_squares():
    n = int(input("რიცხვი: "))
    sum_squares = (n * (n + 1) * (2 * n + 1)) // 6
    print("კვადრატების ჯამი 1-დან", n, "მდე არის:", sum_squares)

def sum_of_even_numbers():
    n = int(input("რიცხვი: "))
    sum_even = 0
    for i in range(2, n+1, 2):
        sum_even += i
    print("ყველა ლუწი რიცხვის ჯამი 1-დან", n, "მდე არის:", sum_even)

def smallest_common_multiple():
    num1 = int(input("პირველი რიცხვი: "))
    num2 = int(input("მეორე რიცხვი: "))
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break
        greater += 1
    print("უმცირესი საერთო ჯერადი", num1, "და", num2, "არის:", lcm)

def find_divisors():
    num = int(input("რიცხვი: "))
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print("ყველა გამყოფი", num, "ის არის:", divisors)

menu = {
    1: (" სამ რიცხვში უმცირესის პოვნა", find_smallest_of_three_numbers),
    2: ("ტემპერატურს შკალის კონვერტორი ცელსიუსიდან ფარენგეიტში", celsius_to_fahrenheit),
    3: ("ტემპერატურს შკალის კონვერტორი ფარენგეიტიდან ცელსიუსში", fahrenheit_to_celsius),
    4: ("მოცემულ დიაპაზონში (1..n) ყველა მარტივი რიცხვის პოვნა", find_prime_numbers),
    5: ("1-დან n-მდე ყველა რიცხვის ჯამი", sum_of_numbers),
    6: (" 1-დან n-მდე ყველა რიცხვის საშუალო არითმეტიკული", arithmetic_mean),
    7: ("1-დან n-მდე ყველა რიცივის კვადრატების ჯამი", sum_of_squares),
    8: ("1-დან n-მდე ყველა ლუწი რიცხვის ჯამი", sum_of_even_numbers),
    9: ("ორი რიცხვის უმცირესი საერთო ჯერადი", smallest_common_multiple),
    10: ("მოცემული რიცხვის ყველა გამყოფის პოვნა ", find_divisors)
}


print("მენიუ:")
for key, value in menu.items():
    print(key, "-", value[0])


choice = int(input("აირჩიეთ (1-10): "))


if choice in menu:
    selected_func = menu[choice][1]
    selected_func()
else:
    print("არა.")