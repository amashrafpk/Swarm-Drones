from constants import Constants
import math
import numpy as np

def s(z,d):
    if z<0 or z>d:
        return 0
    else:
        return 1+math.cos((math.pi*(z+d))/(2*d))

def norm2(p1,p2):
    """ Scalar distance from p1 to p2 (without direction)"""
    return np.linalg.norm(p1-p2)

def unitary_vector(p1,p2):
    """ Results in a unitary vector going from p1 to p2  [p1 --> p2] """
    if (np.array_equal(p1,p2)):
        # return a random velocity for each
        return np.random.uniform(low=-1,high=1, size=(2,))
    return (p2-p1)/norm2(p1,p2)

def angle_between(vec1,vec2):

    def norm1(p):
        """Scalar magnitude of a vector from (0,0)"""
        return math.sqrt(p[0]*p[0]+p[1]*p[1])

    """ Compute angle between vector1 and vector2 """
    divisor = norm1(vec1)*norm1(vec2)
    dot_product = np.dot(vec1,vec2)
    
    # Ensure divisor is not zero to avoid error in division
    if divisor == 0: return 0 
    value = dot_product/divisor

    # Ensure a value between -1 and 1 is passed to acos function
    if value > 1: value = 1 
    elif value < -1: value = -1
    
    # Final computation for angle between vectors
    return math.degrees(math.acos(value))

def outside_area(x,y):
    """ Function to check if point is outside the permitted area """
    if (x<Constants.GEO_FENCE_WIDTH) or (y<Constants.GEO_FENCE_WIDTH) or \
        (x>Constants.LENGTH-Constants.GEO_FENCE_WIDTH) or (y>Constants.WIDTH-Constants.GEO_FENCE_WIDTH):
        return True
    return False
def closest_point_on_line_segment(x, p1, p2):
    """
    Returns the closest point on a line segment to point x.

    Args:
    - x: a 2D point
    - p1, p2: the endpoints of the line segment

    Returns:
    - a 2D point, the closest point on the line segment to x
    """

    # compute the direction vector of the line segment
    v = np.array(p2) - np.array(p1)

    # compute the vector from p1 to x
    w = np.array(x) - np.array(p1)

    # compute the scalar projection of w onto v
    c1 = np.dot(w, v)

    # if c1 is negative, the closest point is p1
    if c1 <= 0:
        return p1

    # compute the squared length of v
    l2 = np.dot(v, v)

    # if c1 is greater than the squared length of v, the closest point is p2
    if c1 >= l2:
        return p2

    # compute the projection of w onto v
    proj = c1 / l2 * v

    # compute the closest point
    closest = np.array(p1) + proj

    return closest


def reflection(v, n):
    """
    Returns the reflection of a vector v about a surface with normal n.

    Args:
    - v: a 2D vector
    - n: a 2D vector, the normal to the surface

    Returns:
    - a 2D vector, the reflection of v about the surface with normal n
    """

    # compute the projection of v onto n
    proj = np.dot(v, n) / np.linalg.norm(n)**2 * n

    # compute the perpendicular component of v
    perp = v - proj

    # compute the reflection of v about n
    reflected = perp - proj

    return reflected