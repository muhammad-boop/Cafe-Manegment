menu = {
  "Pizza":80,
  "Burger":50,
  "Pasta":70,
  "Fries":40,
  "Ice Cream":30,
  "Chocolate":20,
}
# Greet
print("Welcome to our Restaurant.What would you like to have?")
print("Pizza:RS80\nBurger:RS50\nPasta:RS70\nFries:RS40\nIce Cream:RS30\nChocolate:RS20")
# Get Oder
order = input('Enter Your order: ')
# Calculate Bill
bill = menu[order]
# Print Bill
print("Your Bill is Rs",bill)