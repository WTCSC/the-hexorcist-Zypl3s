digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(number_string, original_base):
    total_value = 0
    power = 0

    for char in number_string[::-1]:
        total_value += (digits.index(char) * (original_base ** power))
        power += 1

    return total_value

def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return "0"
    else:
        result_string = ""

        while decimal_number > 0:
            remainder = decimal_number % target_base
            decimal_number = decimal_number // target_base
            char_to_add = digits[remainder]

            result_string = char_to_add + result_string

        return result_string

print("Welcome to the Hexorcist \n")

og = input("Enter the string you want to convert: ").upper()
og_base = int(input("Enter the base of the original string (2-36): "))
new_base = int(input("Enter the base you want to convert to (2-36): "))

print("\n" f"Converting from base {og_base} to base {new_base}... \n")

print(f"{og} in base {og_base} is equal to {from_decimal(to_decimal(og, og_base), new_base)} in base {new_base}")
