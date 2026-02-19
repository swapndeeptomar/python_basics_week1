inventory = [
    {"product_id": "P101", "name": "Laptop", "category": "Electronics", "price": 1200, "quantity": 5},
    {"product_id": "P102", "name": "Desk Chair", "category": "Furniture", "price": 150, "quantity": 20},
    {"product_id": "P103", "name": "T-Shirt", "category": "Apparel", "price": 25, "quantity": 50},
    {"product_id": "P104", "name": "Mouse", "category": "Electronics", "price": 30, "quantity": 100},
    {"product_id": "P105", "name": "Coffee Table", "category": "Furniture", "price": 200, "quantity": 12},
    {"product_id": "P106", "name": "Jeans", "category": "Apparel", "price": 50, "quantity": 30},
    {"product_id": "P107", "name": "Monitor", "category": "Electronics", "price": 300, "quantity": 8}
]

for items in inventory:
    print(f"{items}\n")

total=0
for i in inventory:
    print(f"{i['price']} : {i['quantity']}")
    i_total=i['price']*i['quantity']
    print(f"Total Inventory Value is  : {i_total}")
    total+=i_total

print("Grand total inventory value is : ",total)

list=[]
for i in inventory:
    if i["quantity"]<15:
        print("Low stock item is",i['product_id'],i['name'])
        list.append(i['name'])
print(list)

high_price=0
high_item=None
for i in inventory:
    if i['price']>high_price:
        high_price=i['price']
        high_item=i
print(high_price)
print(high_item)

unique=set() 
for i in inventory:
    unique.add(i['category'])
print(f"Unique items are {unique}")

#using manual checking

unique1=[]
for i in inventory:
    cat=i["category"]
    if cat not in unique1:
        unique1.append(cat)
print(unique1)