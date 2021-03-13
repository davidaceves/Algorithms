#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipeValue = list(recipe.values())
  ingredientValue = list(ingredients.values())

  batchAmounts = []

  # If recipe length > ingredients length, it can't be made
  if len(recipe) > len(ingredients): 
    return 0

  # Appends the amount of times a recipe ingredient is divisible by your own ingredients to the array 
  for i in range(0, len(recipe)):
    batchAmounts.append(int(ingredientValue[i] / recipeValue[i]))
    
  # The smallest amount is the maximum times a recipe can be made
  return min(batchAmounts)

recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })

recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 })

recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 })

recipe_batches({ 'milk': 2 }, { 'milk': 200})

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))