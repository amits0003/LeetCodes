from itertools import product, permutations

"""
Combinatorial problems involve counting or generating combinations of elements from a set based on certain 
criteria or constraints. These problems often require exploring all possible combinations to find a solution.
I'll provide an example scenario of a combinatorial problem and demonstrate how you might approach it using Python.

Scenario: Generating Combinations
Let's say you have a set of colors, and you want to generate all possible combinations of colors for a set number 
of items. For simplicity, let's consider a scenario where you have three items, and the available colors are red,
green, and blue.

In this example, the generate_color_combinations function uses the itertools.product function to generate all 
possible combinations of colors for a given number of items. The repeat parameter is set to the number of items, 
so it will create combinations of that length."""


def generate_color_combinations(items, colors):
    # Use itertools.product to generate all combinations
    all_combinations = list(product(colors, repeat=items))
    return all_combinations


# # Example usage:
# items_count = 3
# available_colors = ['red', 'green', 'blue']
#
# combinations = generate_color_combinations(items_count, available_colors)
#
# # Display the generated combinations
# for combination in combinations:
#     print(combination)

"""
Scenario: Selecting Combinations with Constraints
Now, let's extend the scenario by adding a constraint. 
Suppose you only want combinations where each color appears at most once in a combination."""


def generate_color_combinations_with_constraints(items, colors):
    # Use itertools.permutations to generate combinations with constraints
    valid_combinations = [combination for combination in permutations(colors, items) if len(set(combination)) == items]
    return valid_combinations


# Example usage:
items_count = 3
available_colors = ['red', 'green', 'blue']

valid_combinations = generate_color_combinations_with_constraints(items_count, available_colors)

# Display the valid combinations
for combination in valid_combinations:
    print(combination)
