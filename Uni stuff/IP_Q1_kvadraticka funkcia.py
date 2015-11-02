def f(x):
    result = (-5*(x**5)) + (69*(x**2)) - 47
    return result

print f(2)
print f(1)
print f(0)
print f(3)

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

    # I was correcting syntax here    
import math
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    return point_x * scale, point_y * scale
    
print project_to_distance(2, 7, 4)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    # Put your code here.
    return present_value*((1+rate_per_period)**periods)

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print future_value(500, .04, 10, 10)

def polygon(sides, length):
    return float(1.0/4 * (sides * length**2)) / float(math.tan(math.pi/sides))
    
print polygon(7, 3)