class Awesome:
    'This is a sample class called Awesome.'
    def __init__(self):
        print("Hello from __init__ method.")


print(Awesome.__doc__)
print(Awesome.__name__)
print(Awesome.__dict__)
print(Awesome.__module__)
print(Awesome.__bases__)