products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
on_sale_products = []
for item in products:
    if item[2]:
        on_sale_products.append(item)
print(on_sale_products)

on_sale_products_2 = [product for product in products if product[2]]
print(on_sale_products_2)
