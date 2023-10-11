# General information
This project introduces functions that calculate the area and perimeter of a circle, square, triangle and rectangle

# circle.py
- def area(r)

  - Функция возвращает площадь круга
    - Параметры:
    
      r (тип int) - радиус круга
    - Значение, возвращаемое функцией: 
    
      area (тип float) - площадь круга с радиусом r
    - Пример вызова:
    
            print(area(1))
            //3.14...
- def perimeter(r)

  - Функция возвращает периметр круга
    - Параметры:
    
      r (тип int) - радиус круга
    - Значение, возвращаемое функцией: 
    
      perimeter (тип float) - периметр круга с радиусом r
    - Пример вызова:
    
            print(perimeter(1))
            //6.28...

# rectangle.py
- def area(a, b)

  - Функция возвращает площадь прямоугольника
    - Параметры:
    
      a (тип int), b (тип int) - смежные стороны прямоугольника
    - Значение, возвращаемое функцией: 
    
      area (тип int) - площадь прямоугольника со смежными сторонами a и b
    - Пример вызова:
    
            print(area(2,4))
            //8
- def perimeter(a,b)

  - Функция возвращает периметр прямоугольника
    - Параметры:
    
      a (тип int), b (тип int) - смежные стороны прямоугольника
    - Значение, возвращаемое функцией: 
    
      perimeter (тип int) - периметр прямоугольника со смежными сторонами a и b
    - Пример вызова:
    
            print(perimeter(3,5))
            //16

# square.py
- def area(a)

  - Функция возвращает площадь квадрата
    - Параметры:
    
      a (тип int) - сторона квадрата
    - Значение, возвращаемое функцией: 
    
      area (тип int) - площадь квадрата со стороной a
    - Пример вызова:
    
            print(area(2))
            //4
- def perimeter(a)

  - Функция возвращает периметр квадрата
    - Параметры:
    
      a (тип int) - сторона квадрата
    - Значение, возвращаемое функцией: 
    
      perimeter (тип int) - периметр квадрата со стороной a
    - Пример вызова:
    
            print(perimeter(3))
            //12

# triangle.py
- def area(a, h)

  - Функция возвращает площадь треугольника
    - Параметры:
    
      a (тип int) - основание треугольника, h (тип int) - высота треугольника
    - Значение, возвращаемое функцией: 
    
      area (тип float) - площадь треугольника с основанием a и высотой h
    - Пример вызова:
    
            print(area(2, 4))
            //4.0
- def perimeter(a, b, c)

  - Функция возвращает периметр квадрата
    - Параметры:
    
      a, b, c (тип int) - стороны треугольника
    - Значение, возвращаемое функцией: 
    
      perimeter (тип int) - периметр треугольника со сторонами a, b, c
    - Пример вызова:
    
            print(perimeter(1,2,3))
            //6
  
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = 0,5 * ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Commit history
* 70edc17 (origin/new_features_408175) Исправлена ошибка
* deeb837 Добавлен новый файл
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added