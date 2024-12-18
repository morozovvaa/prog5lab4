# Лабораторная работа 4. Ряд Фибоначчи с помощью итераторов

Лабораторная работа состоит из двух подзаданий: 
1. Создание сопрограммы на основе кода, позволяющей по данному n сгенерировать список элементов из ряда Фибоначчи.
2. Создание программы, возвращающей список чисел Фибоначчи с помощью итератора.


## Задание 1
Разработана сопрограмма (_корутина_), реализующая возвращение списка элементов ряда Фибоначчи. 

Сопрограмма для создания списка чисел Фибоначчи
```
def my_genn():
    """Сопрограмма, которая возвращает первые n элементов ряда Фибоначчи."""
    while True:
        number_of_fib_elem = yield  
        fib_gen = fib_elem_gen()  
        l = list(itertools.islice(fib_gen, number_of_fib_elem))  
        yield l  

```
Необходимые тесты в файле ```test_fib.py```.
![image](https://github.com/user-attachments/assets/85f6a8a7-170d-43e0-bc3e-e2c5b7247b2d)
![image](https://github.com/user-attachments/assets/96d839f9-6134-4d8d-9f1f-d261ef76eb66)



## Задание 2
Дополните код классом ```FibonacchiLst``` (пример такого класса представлен в even_numbers_iterator.py), который бы позволял перебирать элементы из ряда Фибоначчи по данному ей списку.
Итератор должен вернуть очередное значение, которое принадлежит ряду Фибоначчи, из данного ей списка.

```
class FibonacchiLst:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 0
        self.fib_set = self._generate_fibonacci_set(max(lst))
    
    def _generate_fibonacci_set(self, n):
        fib_set = set()
        a, b = 0, 1
        while a <= n:
            fib_set.add(a)
            a, b = b, a + b
        return fib_set
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.idx < len(self.lst):
            num = self.lst[self.idx]
            self.idx += 1
            if num in self.fib_set:
                return num
        raise StopIteration

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
fib_iterator = FibonacchiLst(lst)
print(list(fib_iterator))
```
