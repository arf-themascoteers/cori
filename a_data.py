x = 1
print(x)

x = [1,2,3]
print(x)

print(x[0])

x = [
    [1,2,3],
    [4,5,6]
]

print(x[0][1])
y = x[0]
print(y[1])

x = {
    "name" : "cori",
    "age" : 7
}

print(x["name"])
print(x["age"])

x = [
    {
        "name": "cori",
        "age": 7
    },
    {
        "name": "arif",
        "age": 5
    },
]

print(x[1]["name"])
person = x[1]
print(person["name"])


x = [
    {
        "name": "cori",
        "age": 7,
        "courses" : [
            "English", "Philosophy"
        ],
        "hobby" : [
            {
                "hobby_name":"Reading",
                "how_much" : 10
            },
            {
                "hobby_name": "Movie",
                "how_much": 3
            }
        ]
    },
    {
        "name": "arif",
        "age": 5
    },
]

print(x[0]["hobby"][1]["how_much"])
