# -*- coding: utf-8 -*-
"""
polysum Grader
Exercise for MITx 6.00.1x
"""

import math

def getRegularPolygonArea(n, s):
    """
    Gets the area of a n-regular polygon with side length s.

    Parameters
    ----------
    n : Integer
        Number of sides.
    s : Numeric
        Length of each side.

    Returns
    -------
    The area of a n-regular polygon with side s.

    """
    return (0.25*n*s**2)/(math.tan(math.pi/n))

def getRegularPolygonPerimeter(n, s):
    """
    Gets the perimeter of a n-regular polygon with side length s.

    Parameters
    ----------
    n : Integer
        Number of sides.
    s : Numeric
        Length of each side.

    Returns
    -------
    The perimeter of a n-regular polygon with side s.

    """
    return n*s

def polysum(n, s):
    """
    Sum the area and square of the perimeter of a regular polygon.

    Parameters
    ----------
    n : Integer
        Number of sides.
    s : Numeric
        Length of each side.

    Returns
    -------
    The sum, rounded to 4 decimal places.

    """
    # The regular polygon area
    area = getRegularPolygonArea(n, s)
    # The regular polygon area perimeter
    perimeter = getRegularPolygonPerimeter(n, s)
    
    return round(area + perimeter**2, 4)
