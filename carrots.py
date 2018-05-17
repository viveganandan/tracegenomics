#!/usr/bin/python

import sys
import json
from copy import deepcopy

def eat(garden):
    """Get max number of carrots bunny eats before falling asleep
    Args:
        garden: A n x m matrix that represents the garden with ints
        representing the number of carrots
    """
    def get_center(n, m):
        """Return center coordinates of garden
        Args:
            n: The number of cols in garden
            m: The number of rows in garden
        """
        # Center starting point
        x = (n - 1) / 2
        y = (m - 1) / 2
        # There could be more than one center, depending on if rows and or cols is even
        for i in range(x, n / 2 + 1):
            for j in range(y, m / 2 + 1):
                if garden[i][j] > garden[x][y]:
                    x, y = i, j
        return x, y

    def get_max_adjacent(n, m, x, y, eaten):
        """Return the adjacent cell's corrdinates with the max number
        of carrots to x, y.  If all adjacent cells have already been eaten,
        then return none
        Args:
            n: The number of cols in garden
            m: The number of rows in garden
            x: The x point of the cell
            y: The y point of the cell
            eaten: Garden that shows eaten carrots
        """
        xa, ya = None, None
        max_carrots = 0
        # Go left, right
        for i in -1, 1:
            # Verify that we are not out of bounds before reaching adjacent cell
            if y + i > -1 and y + i < m and eaten[x][y + i] > max_carrots:
                max_carrots = eaten[x][y + i]
                xa, ya = x, y + i
        # Go up, down
        for i in -1, 1:
            # Verify that we are not out of bounds before reaching adjacent cell
            if x + i > -1 and x + i < n and eaten[x + i][y] > max_carrots:
                max_carrots = eaten[x + i][y]
                xa, ya = x + i, y
        return xa, ya

    # Make sure we have a garden
    n = len(garden)
    if not n:
        return 0
    m = len(garden[0])
    if not m:
        return 0

    x, y = get_center(n, m)
    carrots = 0
    # copy over garden so we can update it with carrots eaten by bunny rather than mess with original garden
    eaten = deepcopy(garden)
    # starting at center, find next max adjacent with max number of carrots and continue until bunny has nothing to eat
    while x != None and y != None:
        # If number of carrots is less than 1, no point in counting it
        if eaten[x][y] > 0:
            carrots += eaten[x][y]
        # empty out cell since bunny has already eaten
        eaten[x][y] = 0
        x, y = get_max_adjacent(n, m, x, y, eaten)
    return carrots

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print 'Expecting a garden!'
        sys.exit(1)
    try:
        garden = json.loads(sys.argv[-1])
    except ValueError, e:
        print 'Garden is not a valid nxm matrix', str(e)
        sys.exit(1)

    print 'Number of carrots of eaten by bunny before falling asleep = %s' % (eat(garden))

if __name__ == '__main__':
    main()
