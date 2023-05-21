# Catalog of products
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount Rules
discount_rules = {
    "flat_10_discount": {"threshold": 200, "discount_amount": 10},
    "bulk_5_discount": {"threshold": 10, "discount_percentage": 5},
    "bulk_10_discount": {"threshold": 20, "discount_percentage": 10},
    "tiered_50_discount": {"total_quantity_threshold": 30, "single_product_quantity_threshold": 15, "discount_percentage": 50}
}

# Fees
gift_wrap_fee_per_unit = 1
items_per_package = 10
shipping_fee_per_package = 5

# Initialize variables
subtotal = 0
total_quantity = 0
discount_name = ""
discount_amount = 0
shipping_fee = 0
gift_wrap_fee = 0

# Get quantity and gift wrap information for each product
for product, price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product}: "))
    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ")

    # Calculate product total
    product_total = price * quantity

    # Apply discount rules
    applicable_discounts = {}
    for rule, parameters in discount_rules.items():
        if rule == "flat_10_discount" and subtotal > parameters["threshold"]:
            applicable_discounts[rule] = parameters["discount_amount"]
        elif rule == "bulk_5_discount" and quantity > parameters["threshold"]:
            applicable_discounts[rule] = (parameters["discount_percentage"] / 100) * product_total
        elif rule == "bulk_10_discount" and total_quantity > parameters["threshold"]:
            applicable_discounts[rule] = (parameters["discount_percentage"] / 100) * subtotal
        elif rule == "tiered_50_discount" and total_quantity > parameters["total_quantity_threshold"] and quantity > parameters["single_product_quantity_threshold"]:
            applicable_discounts[rule] = (parameters["discount_percentage"] / 100) * (quantity - parameters["single_product_quantity_threshold"]) * price

    # Apply the most beneficial discount
    if applicable_discounts:
        max_discount_rule = max(applicable_discounts, key=applicable_discounts.get)
        discount_name = max_discount_rule
        discount_amount = applicable_discounts[max_discount_rule]

    # Update subtotal and total quantity
    subtotal += product_total - discount_amount
    total_quantity += quantity

    # Calculate gift wrap fee
    if gift_wrap.lower() == "yes":
        gift_wrap_fee += quantity * gift_wrap_fee_per_unit

    # Calculate shipping fee
    if total_quantity % items_per_package == 0:
        shipping_fee += shipping_fee_per_package

    # Output product details
    print(f"\nProduct: {product}")
    print(f"Quantity: {quantity}")
    print(f"Total Amount: ${product_total}")

# Output order summary
print("\nORDER SUMMARY")
print(f"Subtotal: ${subtotal}")
print(f"Discount Applied: {discount_name} (${discount_amount})")
print(f"Shipping Fee: ${shipping_fee}")
print(f"Gift Wrap Fee: ${gift_wrap_fee}")
print(f"Total: ${subtotal + shipping_fee + gift_wrap_fee}")
