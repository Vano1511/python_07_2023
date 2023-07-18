while True: # проверка на дурака
    try:
        list_of_triangle_sides = list(map(float, input("Введите длины сторон треугольника через пробелы: ").split()))
        if list_of_triangle_sides[0] < 0 or list_of_triangle_sides[1] < 0 or list_of_triangle_sides[2] < 0:
            print("длина стороны не может быть отрицательной")
            continue
        break
    except:
        print("вы что то ввели неверно, нужны три положительные цифры")

flag = True  # проверка на треугольник
for side in list_of_triangle_sides:
    if sum(list_of_triangle_sides) - side <= side:
        print("это не треугольник")
        flag = False
        break

if flag:  # выясняем какой треугольник
    if len(set(list_of_triangle_sides)) == 1:
        print("треугольник равносторонний")
    elif len(set(list_of_triangle_sides)) == 2:
        print("треугольник равнобедренный")
    else:
        print("у треугольника все стороны разной длины")

