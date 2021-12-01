def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'


print(get_info(**{'name': 'G', 'town': 'S', 'age': 20}))