my_dict = {
    "імʼя": "Богдан",
    "скільки років": 16,
    "Деталі": {
        "ріст": 185,
        "вага": 70,
        "хоббі": "Баскетбол",
        "звідки родом": "Луцьк"
    },
    "активний": True
}

# Словники для зберігання типів даних
new_dict = {}


for key, value in my_dict.items():
    if isinstance(value, dict):
        temp_dict = {}
        for inner_key, inner_value in value.items():
            temp_dict[inner_key] = type(inner_value).__name__
        new_dict[key] = temp_dict
    else:
        new_dict[key] = type(value).__name__

print("Перший словник:")
print(my_dict)
print("\nСловник з типами даних:")
print(new_dict)
