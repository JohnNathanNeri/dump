#ask the users name
name = input("please enter your name:")

#ask the user waht conversion he wants
farenheitToCelsius = "A"
celsiusToFarenheit = "B"

print("What conversion do you want?")
print("A. Farenheit To Celsius")
print("B. Celsius To Farenheit")
select = input("")

#ask the current tempereture
temperature = float(input("Enter the current temperature:"))

#calculation
if select == farenheitToCelsius:
    farenheitToCelsius = (5/9) * (temperature - 32)
    answer = farenheitToCelsius
    print(f"hello, {name}! {temperature} is equal to {answer} celsius.")
elif select == celsiusToFarenheit:
    celsiusToFarenheit = (9/5) * temperature + 32
    answer = celsiusToFarenheit
    print(f"hello, {name}! {temperature} is equal to {answer} farenheit.")
else:
    print("please use your brain and put a valid letter.")