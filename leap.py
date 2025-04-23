def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    
    Rules:
    - Divisible by 4 AND
        - NOT divisible by 100 OR divisible by 400
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def main():
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Please enter a valid integer year.")

# Run the program
if __name__ == "__main__":
    main()