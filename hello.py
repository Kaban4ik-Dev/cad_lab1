# hello.py — версия 2.2
def greet(name: str, m_from: str, punctuation: str = "!") -> str:
    return f"Hello, {name}, from {m_from}{punctuation}"

if __name__ == "__main__":
    print(greet("world", "MAI"))