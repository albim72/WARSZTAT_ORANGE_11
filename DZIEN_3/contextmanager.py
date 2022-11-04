class ContextManager:

    def __init__(self):
        print("wywołanie konstruktora init")

    def __enter__(self):
        print("wywołanie konstruktora enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("wywołanie konstruktora exit")


with ContextManager() as manager:
    print("operacje wewnątrz with...")
    print(type(manager))

mn = ContextManager()

print(type(mn))
