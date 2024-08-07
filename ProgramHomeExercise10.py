# Exercise 1
dict_details: dict = {
    "name": "Israel",
    "birth": 1948,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon Lezion", "Petah Tikva", "Ashdod"],
    "currency": "ILS",
    "area_kilometer": 22145,
    "gdp_billion": 450
}

print(dict_details.get("capital"));
print(list(dict_details.keys()));
print([key.upper() for key in dict_details.keys()]);
print(list(dict_details.values()));
print([len(str(value)) for value in dict_details.values()]);
print(list(dict_details.items()));
dict_details_copy: dict = dict_details.copy();
print('cpy', dict_details_copy);
dict_details_copy.clear();
print(dict_details_copy);
print(dict.fromkeys(dict_details.keys(), None));
del dict_details['currency'];
print(dict_details);
print(dict_details.pop('area_kilometer'));
print(dict_details);
dict_details.update({'national_sport': 'Soccer'});
print(dict_details);
dict_details['population_millions'] = 9.4;
print(dict_details);

# Exercise 2

action_dict: dict = {'add': 'Adding item', 'delete': 'Deleting an item', 'update': 'Updating item'}


def perform_action(action: str) -> str:
    return action_dict.get(action);


print(perform_action('delete'));

# Exercise 3
import statistics


def get_statistics(numbers: list[int]) -> dict:
    return {
        "average": statistics.mean(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "length": len(numbers),
        "sum": sum(numbers)
    };


print(get_statistics([20, 40, 60, 80]));

# Exercise 4
word: str = input("Please enter a string: ");
operation: str = input("Please enter operation name (lower, upper, length, reverse): ");
operation_dict: dict = {"lower": lambda w: w.lower(), "upper": lambda w: w.upper(),
                        "length": lambda w: len(w), "reverse": lambda w: w[::-1]};

result: str = operation_dict.get(operation)(word);
print(f"The result of your operation is: {result}");

# Exercise 5
# Will the dictionary sent to the dict_from_key_remove function change? Will it stay the same? why?
'''
Yes, the dictionary will change. The popitem() method removes the last key-value pair from the dictionary in place,
which modifies the original dictionary.
'''
# Will the dictionary sent to the all_clear function change? Will it stay the same? why?
'''
No, the dictionary will not change. this reassignment only changes the local reference dictionary within the function, 
not the original dictionary object passed to the function.
Therefore, the dictionary passed to this function will remain unchanged.
'''
# How can you clear the dictionary of arrays inside a function so that it does affect the dictionary from the outside?
'''
You can use the clear() method, which modifies the dictionary in place.
'''

# Exercise 6
# coordinates: dict = {'x': 10, 'y': 20};
# print(coordinates['x']) - Prints the value associated with the X key
# coordinates['x'] = 15 - Changes the value belonging to the X key from 10 to 15
# coordinates['z'] = 30 - Adds to the dictionary a new key named Z with the value 30

# Exercise 7

countries: list = [
             {'name': 'Israel', 'population': 9.3, 'birth': 1948},
             {'name': 'United States', 'population': 331.9, 'birth': 1776},
             {'name': 'Japan', 'population': 125.8, 'birth': 660},
             {'name': 'Australia', 'population': 25.7, 'birth': 1901},
             {'name': 'Canada', 'population': 38.0, 'birth': 1867}
            ];

print("Countries with population more then 30 million: ", list(filter(lambda c: c.get('population') > 30, countries)));
print("Countries born after 1800 year: ", list(filter(lambda c: c.get('birth') > 1800, countries)));
print("Countries born after 1800 year: ", list(filter(lambda c: c.get('birth') > 1800, countries)));
print("Countries names list: ", list(map(lambda c: c.get('name'), countries)));
print("Countries year of birth list: ", list(map(lambda c: c.get('birth'), countries)));
print("Sorted Countries year of birth list: ", sorted(countries, key=lambda c: c.get('birth')));
print("Sorted population number list: ", sorted(countries, key=lambda c: c.get('population')));
