emails = [ "alice@tec.mx", "proftecmm.mx", "stud@tecmm.mx"]

valid_emails = list(filter(lambda email: "@" in email and "." in email, emails))

#chain map () and filter ()
users = [
    {"name": "Alice", "age": 26, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 30, "active": False},
    {"name": "Diana", "age": 22, "active": True}
]

#task : obtener todos los nombres en mayusculas de todos los usuarios activos
#donde la edad sea mayor o igual a 18 años 
active_adults = list(map(lambda user: user["name"].upper(),filter(lambda user: user["active"] and user["age"] >= 18, users)))

print(active_adults)

