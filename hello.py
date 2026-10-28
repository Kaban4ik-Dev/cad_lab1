# hello.py — версия 2
def greet(name: str, m_from: str) -> str:
    return f"Hello, {name}, from {m_from}!"

if __name__ == "__main__":
    print(greet("world", "MAI"))