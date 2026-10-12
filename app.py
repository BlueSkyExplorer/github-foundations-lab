def greet(name: str) -> str:
    return f"Hello, {name.upper()}!"

def welcome(name: str) -> str:
    return f"Welcome to Github Foundations, {name}!"

if __name__ == "__main__":
    print(greet("Github"))
    print(welcome("Github"))