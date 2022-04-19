def celciustofahrenheit(celsius):
    return (1.8*celsius)+32

celsius=float(input("Enter temperature in degree celsius : "))

fahrenheit=celciustofahrenheit(celsius)

print(f"Conversion of {celsius} degree celsius to farenhite is {fahrenheit}")