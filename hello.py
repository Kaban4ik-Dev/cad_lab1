# hello.py — версия 2.1
def greet(name: str, punctuation: str = "!") -> str:
    return f"Hello, {name}{punctuation}"

if __name__ == "__main__":
    print(greet("world"))