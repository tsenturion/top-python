inp = [1, 1, 2, 2]

print(set(inp)) # делает множество уникальных значений

some_set = {1, 2, 3, 3}
print(some_set)
print(type({}))
print(type(set()))

zero2_set = set()
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3)
zero2_set.add(3) # добавление
print(zero2_set)
zero2_set.update(range(5))
print(zero2_set)
zero2_set.discard(1)
print(zero2_set)
zero2_set.remove(2)
print(zero2_set)
popped = zero2_set.pop()
print(zero2_set)
print(popped)
zero2_set.clear()
print(zero2_set)
union_set = {1, 2, 3}.union({13, 2})
union2_set = {1, 2, 3} | {13, 2}
print(union_set)
"""
.set() пустое
.set(iterable) итерируемый объект в множество
.add(element) добавление
.remove(element) удаляет с ошибкой если отсутствует
.pop() удаляет случайный без ошибки
.discard(element) удаляет без ошибки
.copy() копия 
.clear() удаляет полностью

.update(other) |= добавление элементов ищ другого множества
.intersection_update(other) &=  оставляет в множестве только общие элементы с другим множеством
.symmetric_difference_update(other) ^= есть в одном из множеств но не в обоих одновременно
.union(other) | объединение 
.intersection(other) & только общие элементы для обоих множеств
.difference(other) - есть в первом но нет во втором
.difference_update(other) ^ -= симметричная разность. Есть только в одном из множеств но не в обеих одновременно

.isdisjoint(other) True, если set и other не имеют общих элементов
.issubset(other) <= True если все эл set принадлежат other
.issuperset(other) >= True если все из other принадлежат set
"""

intersection_set = {1, 2, 3}.intersection({13, 2})
intersection2_set = {1, 2, 3} & {13, 2}
print(intersection_set)
difference_set = {1, 2, 3}.difference_update({3, 4, 5})
difference2_set = {1, 2, 3} - {3, 4, 5}

print(difference_set)
print(difference2_set)

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

"""
frozenset() пустое
frozenset(iterable) итерируемый объект в неизменяемое множество

copy

union
intersection
difference
symmetric_difference
isdisjoint
issubset
issuperset

"""
print(fs1 | fs2)
print(fs1 & fs2)
print(fs1 - fs2)
print(fs1 ^ fs2)
print(fs1 <= fs2)
print(fs1 >= fs2)

d = {
    frozenset([1, 2, 3]): "value1",
    frozenset([4, 5, 6]): "value2",
}

"""
на вход города
сгруппировать по уникальным наборам букв без учета регистра и повторений
возвращаем словарь по ключу из букв города
значение список городов с таким же набором букв
"""
cities = ['Moskov', 'Tokyo', 'Kyoto']
"""
{
    frozenset({'m', 's', 'c', 'o', 'w'}): ['Moskov'],
    frozenset({'t', 'k', 'y', 'o'}): ['Tokyo', 'Kyoto']
}
"""
def group_cities_by_unique_letters(cities):
    result = {}
    for city in cities:
        unique_letters = frozenset(city.lower())
        if unique_letters in result:
            result[unique_letters].append(city)
        else:
            result[unique_letters] = [city]
    return result

cities = ['Moskov', 'Tokyo', 'Kyoto']
grouped_cities = group_cities_by_unique_letters(cities)
print(grouped_cities)