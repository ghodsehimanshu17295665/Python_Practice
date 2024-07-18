# Highest Comman Factor

# num1 = int(input("Enter Number1:- "))
# num2 = int(input("Enter number2:- "))

# if num2 > num1:
#     min = num1
# else:
#     min = num2

# for data in range(min, 0, -1):
#     if num1 % data == 0 and num2 % data == 0:
#         hcf = data
#         break

# print(f"The HCF of these Two Number is {hcf}")

# num1 = int(input("Enter Number1:- "))
# num2 = int(input("Enter number2:- "))

# if num2 > num1:
#     min = num1
# else:
#     min = num2

# for data in range(1, min+1):
#     if num1 % data == 0 and num2 % data == 0:
#         hcf = data
#         lcm = num1 * num2 // hcf
# print(f"The HCF of these Two Number is {hcf}")
# print(lcm)

# def get_hcf(p, q):

#     while (q != 0):
#         r = p % q
#         p = q
#         q = r

#     return p


# def simplify(p, q):
#     p = int(input("Enter num1: "))
#     q = int(input("Enter Num2: "))

#     hcf = get_hcf(p, q)
#     print(p//hcf)
#     print(q//hcf)

def get_hcf(p, q):
    while q != 0:
        r = p % q
        p = q
        q = r
    return p


def simplify(p, q):
    hcf = get_hcf(p, q)
    simplified_p = p // hcf
    simplified_q = q // hcf
    return simplified_p, simplified_q, hcf


# Example usage:
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

simplified_numerator, simplified_denominator, hcf = simplify(numerator, denominator)
print(f"Simplified fraction: {simplified_numerator}/{simplified_denominator}")

print(f"HCF: {hcf}")
