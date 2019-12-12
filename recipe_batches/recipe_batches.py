#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # initiate num of batches to return
    batches = []

    # loop over recipes
    for key, _ in recipe.items():
        # check if we have all the ingredients
        if key not in ingredients:
            return 0
        # do math to check if we have enough
        elif ingredients[key] - recipe[key] < 0:
            # if one ingredient is not enough, return 0
            return 0
        else:
            # calculate how many batches we can make per ingredient
            batches.append(ingredients[key] // recipe[key])

    # lowest num in batches = max num of WHOLE batches
    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
