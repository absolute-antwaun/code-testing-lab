print("/------------------------------------/")
print("/                                    /")
print("/   Celsius / Fahrenheit Converter   /")
print("/                                    /")
print("/------------------------------------/")
print("")
print("")

option = input("Do you want the temperature in Celsius (C) or Fahrenheit (F)? ").lower
degree = int(input("What is the temperature in C/F? ")).lower

celsius = (degree - 32) * 5 / 9
fahrenheit = (degree * 9 / 5) + 32

if option == "C":
    print(f"The temperature is {celsius} degrees Celsius")
else:
    print(f"The temperature is {fahrenheit} degrees Fahrenheit")
