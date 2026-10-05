users = [
    {"name": "Alice", "age": 26, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 30, "active": False},
    {"name": "Diana", "age": 22, "active": True}
]

resultado = [
    user["name"].upper()
    for user in users
    if user["active"] and user["age"] >= 18
]

print(resultado)