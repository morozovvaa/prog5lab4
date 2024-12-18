from gen_fib import my_genn

def test_fib_1():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"

def test_fib_2():
    gen = my_genn()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"

def test_fib_3():
    gen = my_genn()
    assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13], "Восемь первых членов ряда"

def test_fib_zero():
    gen = my_genn()
    assert gen.send(0) == [], "Крайний случай n = 0, должен быть пустой список"

def test_fib_one():
    gen = my_genn()
    assert gen.send(1) == [0], "Крайний случай n = 1, список должен содержать только [0]"

def test_fib_large():
    gen = my_genn()
    result = gen.send(15)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], "Пятнадцать первых членов ряда Фибоначчи"
