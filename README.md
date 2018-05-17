# QUESTION
Prompt: Write a function that takes the input, gives the output, and meets the conditions below.

Input: An N x M matrix of a garden. Each cell contains an integer representing the number of carrots in that part of the garden.

Output: The number of carrots Bunny eats before falling asleep.

Conditions: Bunny starts in the center of the garden. If there are more than one center cell, Bunny starts in the cell with the largest number of carrots. There will never be a tie for the highest number of carrots in a center cell. Bunny eats all of the carrots in his cell, then looks left, right, up, and down for more carrots. Bunny always moves to the adjacent cell with the highest carrot count. If there are no adjacent cells with carrots, Bunny falls asleep.

Example test cases:

garden1 = [[5, 7, 8, 6, 3],
[0, 0, 7, 0, 4],
[4, 6, 3, 4, 9],
[3, 1, 0, 5, 8]]

eat(garden1)
27 # starts at garden[1][2] = 7, eats 7 carrots, looks at the 8, 0, 3, and 0 adjacent, moves to the 8, repeat.

# Solution

The carrots.py can be called directly with the garden as a command line argument or def "eat" can be imported from carrots.py.

### Examples -

`./carrots.py '[[-1, -1, -1], [-2, -1, 2]]'`

`./carrots.py '[[5, 7, 8, 6, 3],[0, 0, 7, 0, 4],[4, 6, 3, 4, 9],[3, 1, 0, 5, 8]]'`

`./carrots.py '[[7, 6, 3], [-1, 8, 10]]'`

`/carrots.py '[[5, 3, 2, 1, 1], [7, 9, 0, 11, 2], [3, 4, 5, 6, 3], [8, 10, 4, 10, 9]]'`

`./carrots.py '[]'`

`./carrots.py '[[]]'`
