# Список типів даних
list = [10, 'hello', 3.14, True, [1, 2, 3]]

data_types = [type(i) for i in list]

import collections

# Знаходження найчастішого типу даних
most_frequent_type = collections.Counter(data_types).most_common(1)[0][0]

# Виведення найчастішого типу даних
print("Найчастішим типом даних є:", most_frequent_type)