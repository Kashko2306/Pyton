def roman_to_integer(s: str) -> int:
    # Mapping of Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate through each character in the Roman numeral
    for char in s:
        current_value = roman_values[char]

        # If the current value is greater than the previous value,
        # it means we are in a subtractive situation
        if current_value > prev_value:
            total += current_value - 2 * prev_value  # Adjust for the previous addition
        else:
            total += current_value

        prev_value = current_value

    return total
