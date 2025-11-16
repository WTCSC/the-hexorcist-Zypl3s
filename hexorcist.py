digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Converts input to a decimal / Base10
def to_decimal(number_string, original_base):
    total_value = 0
    power = 0

    for char in number_string[::-1]: # Itterates through the intial backwards to get each piece individually
        total_value += (digits.index(char) * (original_base ** power))
        power += 1

    return total_value

# Converts from decimal / Base10 to the base wanted
def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return "0"
    else:
        result_string = ""

        while decimal_number > 0: # 17 = A7, A = 107 is the remainder
            remainder = decimal_number % target_base
            decimal_number = decimal_number // target_base
            char_to_add = digits[remainder]

            result_string = char_to_add + result_string

        return result_string

print("Welcome to the Hexorcist \n")

# Initial conversion (C17)
og = input("Enter the string you want to convert: ").upper()
og_base = int(input("Enter the base of the original string (2-36): ")) # Original base (16)
new_base = int(input("Enter the base you want to convert to (2-36): ")) # Wanted base (10)

print("\n" f"Converting from base {og_base} to base {new_base}... \n")

print(f"{og} in base {og_base} is equal to {from_decimal(to_decimal(og, og_base), new_base)} in base {new_base}")
