# ДОМАШНЄ ЗАВДАННЯ 1
dict_homework = {
    "key1": {
        "d": 44,
        "f": None,
        "s": {
            8: 44,
            9: None,
            10: {"mm": ["s", "GET ME", 7]},
        },
    },
    "key2": {
        "fff1": 44,
        "f": None,
    },
}

print(dict_homework["key1"]["s"][10]["mm"][1])

# ДОМАШНЄ ЗАВДАННЯ 2
# Добавить сумму транзакции, если add = True и среди продуктов есть "Хлеб"
# Должно выйти 172
transactions_homework = [
    {
        "add": True,
        "amount": 69,
        "products": [
            "Хлеб",
            "Масло",
            "Сок",
        ]
    },
    {
        "add": True,
        "amount": 30,
        "products": [
            "Сок",
        ]
    },
    {
        "add": True,
        "amount": 94,
        "products": [
            "Мука",
            "Хлеб",
            "Масло",
        ]
    },
    {
        "add": False,
        "amount": 24,
        "products": [
            "Конфеты",
            "Хлеб",
        ]
    },
    {
        "add": True,
        "amount": 9,
        "products": [
            "Хлеб",
            "Шоколад",
            "Гречка",
        ]
    },
    {
        "add": True,
        "amount": 91,
        "products": [
            "Апельсин",
            "Гречка",
        ]
    },
    {
        "add": True,
        "amount": 84,
        "products": [
            "Помидоры",
            "Сок",
        ]
    },
    {
        "add": False,
        "amount": 45,
        "products": [
            "Хлеб",
            "Гречка",
        ]
    },
    {
        "add": True,
        "amount": 9,
        "products": [
            "Лимон",
            "Сок",
        ]
    },
]

total_am = 0
for transaction in transactions_homework:
    if transaction["add"] and "Хлеб" in transaction["products"]:
        total_am += transaction["amount"]
print(total_am)
