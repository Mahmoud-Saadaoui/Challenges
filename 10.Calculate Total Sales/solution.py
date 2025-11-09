def total_sales(products: list, tax: float):
    total = 0
    for prod in products:
        total += prod["price"] * prod["quantity"]
    total_with_tax = total * (1 + tax)
    return total_with_tax
