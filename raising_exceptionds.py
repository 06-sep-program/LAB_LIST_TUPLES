def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
            parts = user_input.strip().split()
            
            if len(parts) != 2:
                raise ValueError("Invalid format. Please enter value and unit separated by a space.")
            
            value_str, unit = parts
            temp_value = float(value_str)
            
            if unit.upper() == 'C':
                converted = celsius_to_fahrenheit(temp_value)
                print(f"Temperature in Fahrenheit: {converted:.2f} F")
                break
            elif unit.upper() == 'F':
                converted = fahrenheit_to_celsius(temp_value)
                print(f"Temperature in Celsius: {converted:.2f} C")
                break
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
                
        except ValueError as ve:
            print(f"Invalid input. Please try again.")
        except TypeError as te:
            print(f"Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "_main_":
    main()