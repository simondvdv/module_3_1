def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.lower(), string.upper()


def is_contains(string, list_to_search):
    count_calls()
    lowercase_list = [s.lower() for s in list_to_search]
    if string.lower() in lowercase_list:
        return True
    else:
        return False


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
