def two_tag_system(rules, initial_string):
    # Convert rules into dictionary for easy access
    rule_dict = {key: value for key, value in rules}

    # Start with initial string
    current_string = initial_string

    while True:
        print(current_string)  # Optional: Print current state

        if len(current_string) < 2 or current_string[0] not in rule_dict:
            break  # Not enough symbols to continue or no applicable rule; halt

        # Apply rule: remove first two symbols and append associated string
        head_symbol = current_string[0]
        current_string = current_string[2:] + rule_dict[head_symbol]

    return current_string

# Define your alphabet implicitly within your production rules
production_rules = [
    ('a', 'bc'),
    ('b', 'a'),
    ('c', 'aaa')
]

initial_str = "aaa"

# Run simulation
two_tag_system(production_rules, initial_str)
