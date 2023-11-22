import math

def area(r):
    '''Принимает число r(радиус круга), возвращает площадь круга с радиусом r
    print(area(1))
    //3.14...'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r(радиус круга), возвращает периметр круга с радиусом r
    print(perimeter(1))
    //6.28...'''
    return 2 * math.pi * r
