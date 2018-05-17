#!/usr/bin/python

import sys
import json

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

    def get_max_adjacent(n, m, x, y):
        """Return the adjacent cell's corrdinates with the max number
        of carrots to x, y.  If all adjacent cells have already been eaten,
        then return none
        Args:
            n: The number of cols in garden
            m: The number of rows in garden
            x: The x point of the cell
            y: The y point of the cell
        """
        xa, ya = None, None
        max_carrots = 0
        # Go left, right
        for i in -1, 1:
            # Verify that we are not out of bounds before reaching adjacent cell
            if y + i > -1 and y + i < m and garden[x][y + i] > max_carrots:
                max_carrots = garden[x][y + i]
                xa, ya = x, y + i
        # Go Up, down
        for i in -1, 1:
            # Verify that we are not out of bounds before reaching adjacent cell
            if x + i > -1 and x + i < n and garden[x + i][y] > max_carrots:
                max_carrots = garden[x + i][y]
                xa, ya = x + i, y
        return xa, ya

    if not garden:
        return 0
    n = len(garden)
    m = len(garden[0])
    carrots = 0
    x, y = get_center(n, m)
    while x != None and y != None:
        # If number of carrots is negative, dont' count it
        if garden[x][y] > -1:
            carrots += garden[x][y]
        garden[x][y] = 0
        x, y = get_max_adjacent(n, m, x, y)
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

    print 'Number of carrots of eaten by bunny before falling asleep = %s' % (eat(garden))

if __name__ == '__main__':
    main()
