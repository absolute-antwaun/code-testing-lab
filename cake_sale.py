print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~               ~~~~~~")
print("~~~~~~   Cake Sale   ~~~~~~")
print("~~~~~~               ~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")

print("Welcome To Our Cake Sale!")

print("Here are the cake for sale:")

print(" > * Cupcakes * < ")
print(" > * Macarons * < ")
print(" > * Cheesecake * < ")
print("")

cupcake_price = 0.40
macarons_price = 0.50
cheesecake_price = 0.70

cupcake = int(input("How many cupcakes do you plan to sell? "))
cupcake_total = cupcake * cupcake_price

macarons = int(input("How many macarons do you plan to sell? "))
macarons_total = macarons * macarons_price

cheesecake = int(input("How many cheesecakes do you plan to sell? "))
cheesecake_total = cheesecake * cheesecake_price

cake_sale = cupcake_total + macarons_total + cheesecake_total

print(f"You will make ${cake_sale} profit")
