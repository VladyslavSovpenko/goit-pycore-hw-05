import re


def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    for n in re.finditer(pattern, text):
        yield float(n.group())


def sum_profit(text: str, func) -> float:
    return sum(func(text))


input_text = (
    "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими"
    "надходженнями 27.45 і 324.00 доларів.")

total_income = sum_profit(input_text, generator_numbers)
print(f"Загальний дохід: {total_income}")
