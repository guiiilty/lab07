# Лабораторная работа №7
## Сложность: Rare
## Вариант №2
### Задание
1. Напишите две функции для решения задач своего варианта - с использованием рекурсии и без.
2. Оформите отчёт в README.md. Отчёт должен содержать:
    - Условия задач
    - Описание проделанной работы
    - Скриншоты результатов
    - Ссылки на используемые материалы
### Ход работы
- Функция для расчёта суммы вложенных списков.
    ```shell
    >>> sum_nested([1, [2, [3, 4, [5]]]])
    15
    ```
- Функция для расчёта $a_k = \frac{1}{2}(\sqrt{b_{k-1}} + \frac{1}{2}\sqrt{a_{k-1}}). a_1 = b_1 = 1.$

```python
import math

def sum_nested(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

def A(n):
    a = [1]
    b = [1]
    for k in range(2, n + 1):
        b_k_minus_1 = b[k - 2]
        a_k_minus_1 = a[k - 2]
        a_k = 0.5 * (math.sqrt(b_k_minus_1) + 0.5 * math.sqrt(a_k_minus_1))
        a.append(a_k)
        b.append(a_k)
    return a

nested_list = [1, [2, [3, 4, [5]]]]
print(sum_nested(nested_list))

n = 10
result = A(n)
print(result)
```
Вывод задачи в терминале
```shell
15
[1, 0.75, 0.649519052838329, 0.6044455866507423, 0.5830957404157936, 0.572705294181819, 0.5675797106814806, 0.5650341469843507, 0.5637656496086803, 0.563132469233379]

Process finished with exit code 0
```