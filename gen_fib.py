import functools
import itertools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def my_genn():
    """Сопрограмма, которая возвращает первые n элементов ряда Фибоначчи."""
    result = None
    while True:
        number_of_fib_elem = yield result  # Возвращаем последний результат
        fib_gen = fib_elem_gen()  # Новый генератор для каждого запроса
        result = list(itertools.islice(fib_gen, number_of_fib_elem))  # Генерируем элементы

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)  # Инициализация сопрограммы
        return gen
    return inner

my_genn = fib_coroutine(my_genn)

if __name__ == "__main__":
    gen = my_genn()  # Создаем сопрограмму

    print(gen.send(3))  # Получаем 3 элемента ряда Фибоначчи
    print(gen.send(5))  # Получаем 5 элементов ряда Фибоначчи
    print(gen.send(8))  # Получаем 8 элементов ряда Фибоначчи
