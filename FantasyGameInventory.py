
def display_inventory(inventory):
    print('Inventory:')
    total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        total += v
    print(f'Total number of items: {total}')
