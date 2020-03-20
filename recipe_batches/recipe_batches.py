#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    num_of_times = []
    recipeKeys = recipe.keys()

    for i in recipeKeys:
        if i not in ingredients:
            print('Impossible')
            return 0
        else:
            division = (ingredients[i]//recipe[i])
            if division < 1:
                print('No batches can be made from the available ingredients',
                      ingredients[i], recipe[i])

            num_of_times.append(division)
    # print("num_of_times:", num_of_times)
    print(
        f"We can make {min(num_of_times)} batch from the ingredients available")

    return min(num_of_times)


recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
               'milk': 1288, 'flour': 9, 'sugar': 95})
recipe_batches({'milk': 100, 'butter': 50, 'flour': 5},
               {'milk': 132, 'butter': 58, 'flour': 51})
recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {
    'milk': 198, 'butter': 52, 'cheese': 10})
recipe_batches({'milk': 2}, {'milk': 200})
if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 52, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
