# Assignment Chapter 2: Variables and Basic Data Types

def create_person(name: str, age: int, height: float, student: bool) -> dict:
    """
    Create a dictionary with keys: name, age, height, student.
    Example: {"name": "Alice", "age": 20, "height": 1.65, "student": True}
    """
    return {
        "name" : name,
        "age" : age,
        "height" : height,
        "student" : student
    }


def age_next_year(age: int) -> int:
    """Return the person's age next year."""
    return age + 1


def is_adult(age: int) -> bool:
    """Return True if age is >= 18, else False."""
    return age >=18


def format_intro(name: str, age: int) -> str:
    """
    Return a string introduction like:
    'Hello Alice, you are 20 years old.'
    """
    return f"Hello {name}, you are {age} years old."


def favorite_fruits(fruits: list) -> list:
    """
    Add a new fruit 'mango' to the list and return it.
    """
    fruits.append("mango")
    return fruits