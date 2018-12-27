employee = {
    "Mary":24,
    "Gru":40,
    "Dan":43,
    "Clara":30
}

print(employee)

print(employee["Mary"])

employee["Ham"] = 23

print(employee)

employee["Gru"] = 41

del employee["Dan"]

print(employee)

print(employee.keys())

a = employee.items()

print(a)