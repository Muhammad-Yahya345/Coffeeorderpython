# Print welcome message
print("🌟 Welcome to the Body Math Institute (BMI) 🌟\n")
print("Today we'll help you calculate your BMI - Body Mass Index 🏋️‍♂️\n")

# Ask for user's name
name = input("What is your name? 👤: ")
# Ask for height in meters (float)
print("\nPlease enter your height in meters (e.g. 1.75) 📏")
height = float(input("Height ➡️ "))  # Type casting string input to float

# Ask for weight in kilograms (float)
print("\nNow enter your weight in kilograms (e.g. 68.5) ⚖️")
weight = float(input("Weight ➡️ "))  # Type casting string input to float
# Calculate BMI using the formula: BMI = weight / (height × height)
bmi = weight / (height * height)

# Format BMI to two decimal places
bmi_rounded = round(bmi, 2)
# Get current date and time

# Print the BMI receipt
print("\n\n🧾 Generating your BMI Report...\n")
print("~" * 40)

# Output details
print("Name:", name, end=" 🧑‍💻\n")
print("Height:", height, "m", sep=" ", end=" 📏\n")
print("Weight:", weight, "kg", sep=" ", end=" ⚖️\n")
print("\nYour BMI is:", bmi_rounded, end=" 🧮\n")

# Print basic interpretation
print("\n\n📌 BMI Categories (for your reference only):")
print("Underweight: less than 18.5")
print("Normal: 18.5 - 24.9")
print("Overweight: 25 - 29.9")
print("Obese: 30 or more")

# Print date and time

print("Thank you for using the BMI Calculator! Stay healthy! 🌿💪\n")