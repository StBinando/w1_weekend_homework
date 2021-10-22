def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount_of_money):
    pet_shop["admin"]["total_cash"] += amount_of_money

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number_of_pets):
    pet_shop["admin"]["pets_sold"] += number_of_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    
    return breed_list

def find_pet_by_name(pet_shop, pet_name):
    pet_found = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_found = pet

    return pet_found

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount_of_cash):
    customer["cash"] -= amount_of_cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, purchased_pet):
    customer["pets"].append(purchased_pet)

def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet and customer["cash"]>=pet["price"]:
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])

        # function added to remove pet from original stock
        # not required in original integration tests
        remove_pet_by_name(pet_shop, pet["name"])