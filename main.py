# North Loop Provisions - Donut Shop Management System
# Your first Python program for Module 2

def welcome_message():
    """Display a welcome message for the donut shop."""
    print("🍩 Welcome to North Loop Provisions! 🍩")
    print("Crafting artisanal donuts in Minneapolis's North Loop")
    print("-------------------------------------------")

def show_menu():
    """Display our current donut menu."""
    menu = {
        "Classic Glazed": 3.50,
        "Maple Bacon": 4.50,
        "Spyhouse Coffee": 4.00,
        "MN Berry": 4.25,
        "Local Honey": 4.00
    }
    
    print("\nToday's Donut Menu:")
    print("------------------")
    for donut, price in menu.items():
        print(f"{donut}: ${price:.2f}")

# Main program
if __name__ == "__main__":
    welcome_message()
    show_menu()
    print("\nReady to serve our community with the finest donuts!")
     # Our complete menu organized by category
donut_menu = {
'Small Batch': [
'Wild Rice & Honey', # Made with native MN wild rice
'Maple Bacon', # Using Red Table Meat Co. bacon
'Swedish Cardamom' # Honoring our Nordic heritage
],
'Seasonal': [
'Apple Cider', # Local Honeycrisp apples
'Jucy Lucy', # Cheese-filled tribute to Minneapolis
'Lake of the Woods' # Wild blueberry glazed
],
'Local Collabs': [
'Spyhouse Coffee Cake',
'Fulton Beer & Pretzel',
'Sweet Science Ice Cream'
]
}

# Locally-sourced toppings
toppings = [
'House-made Sprinkles',
'Candied Hazelnuts', # From MN growers
'Bee Pollen', # From local apiaries
'Cookie Butter Drizzle'
]

# Track our morning sales with a dictionary
morning_sales = []

# Record our first sale
morning_sales.append({
'item': 'Wild Rice & Honey',
'quantity': 2,
'toppings': ['Bee Pollen'],
'time': '7:30 AM'
})

# Display our current menu -using a for loop
print("Today's Morning Menu:")
for category, items in donut_menu.items():
 print(category + ":")
for item in items:
 print(" - " + item)


 #Initialize our thoughtfully priced menu items
 small_batch_price = 5.50 # our signature donuts
 Seasonal_price = 6.50 # Using local seasonal ingredients
 Collab_price = 7.50 #Local business collaborations

 # Set our daily small-batch inventory 
 small_batch_inventory = 36 # Classic varieties
 seasonal_inventory = 24 # Made with local seasonal ingredients
 collab_inventory  = 12 #special collaboration items

 # Calculate our morning inventory value
 total_value = (small_batch_price * small_batch_inventory + Seasonal_price * seasonal_inventory + Collab_price * collab_inventory)

 # Format total value to 2 decimal places using string formatting 
 print("Morning inventory value: $" + str("{:.2f}".format(total_value)))



 #conditional statements

 # Customer information 
 purchase_total = 28 
 is_local_resident = True
 bike_comuter = True
 brought_mug = False

 #Initialize reward
 discount = 0

 if is_local_resident:
     discount += 0.10 # supporting our neighbors with 10% off

 if bike_comuter:
    discount += 0.05 #Encouring sustainable transport

 if brought_mug:
    discount += 0.05 #Reducing waste

if purchase_total >= 25:
    discount += 0.05 # Bulk order appreciation

 #caculate and display final discount
final_discount = discount * 100
print("Your community reward discount:" + str(final_discount) + "%")

