import re

def camel_to_snake(camel_case_str):
    snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str).lower()
    return snake_case_str

def main():
    camel_case_str = input()
    snake_case_str = camel_to_snake(camel_case_str)
    print( snake_case_str)

if __name__ == "__main__":
    main()