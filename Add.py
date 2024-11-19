import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python addition.py <num1> <num2>")
        return

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(f"The sum is: {num1 + num2}")
    except ValueError:
        print("Error: Please provide valid numbers.")

if __name__ == "__main__":
    main()
