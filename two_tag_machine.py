def two_tag_system(rules, initial_string):
    rule_dict = {key: value for key, value in rules}

    current_string = initial_string

    while True:
        print(current_string) 

        if len(current_string) < 2 or current_string[0] not in rule_dict:
            break  # HALT

        # remove first two symbols and append associated string
        head_symbol = current_string[0]
        current_string = current_string[2:] + rule_dict[head_symbol]

    return current_string

production_rules = [
    ('a', 'bc'),
    ('b', 'a'),
    ('c', 'aaa')
]

initial_str = "aaa"

two_tag_system(production_rules, initial_str)
