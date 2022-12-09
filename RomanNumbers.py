ROMAN_NUMBERS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def roman_calculate(inp):
    total = 0
    for idx, letter in list(enumerate(inp)):
        current_number = ROMAN_NUMBERS[letter]
        try:
            next_number = ROMAN_NUMBERS[inp[idx + 1]]
        except:
            total += current_number
        else:
            if ROMAN_NUMBERS[letter] < ROMAN_NUMBERS[inp[idx + 1]]:
                total -= ROMAN_NUMBERS[letter]
            else:
                total += ROMAN_NUMBERS[letter]
    print(f"Calculation: {total}")
    


def check():
    prompt = input("Enter a Roman Number: ").upper()
    prompt_list = list(prompt)
    for letter in prompt_list:
        if letter not in ROMAN_NUMBERS.keys():
            print("Invalid Number!")
            check()
    roman_calculate(prompt)

if __name__ == "__main__":
    check()