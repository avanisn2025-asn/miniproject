


def convert_weather():
    print("--- Python Weather Converter ---")
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the current unit (C, F, or K): ").upper()

    if unit == 'C':
        f = (temp * 9/5) + 32
        k = temp + 273.15
        print(f"{temp}°C is {f:.2f}°F and {k:.2f}K")
    elif unit == 'F':
        c = (temp - 32) * 5/9
        k = c + 273.15
        print(f"{temp}°F is {c:.2f}°C and {k:.2f}K")
    elif unit == 'K':
        c = temp - 273.15
        f = (c * 9/5) + 32
        print(f"{temp}K is {c:.2f}°C and {f:.2f}°F")
    else:
        print("Invalid unit! Please use C, F, or K.")

convert_weather()