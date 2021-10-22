def get_pet_shop_name(pet_shop):
    '''Given the pet_shop dictionary, it returns the shop name'''
    return pet_shop["name"]


def get_total_cash(pet_shop):
    '''Given the pet_shop dictionary, it returns the total cash'''
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount_of_money):
    '''Given the pet_shop dictionary and an amount of money, it adds the specified amount to the total cash.
    A negative amount of money will result in the total cash decreased by that amount.
    
    It doesn't return any value'''
    pet_shop["admin"]["total_cash"] += amount_of_money


def get_pets_sold(pet_shop):
    '''Given the pet_shop dictionary, it returns the total number
    of pets sold'''
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, number_of_pets):
    '''Given the pet_shop dictionary and an amount of pets sold,
    it increseases the total number of pets sold by
    the amount specified.
    
    It doesn't return any value'''
    pet_shop["admin"]["pets_sold"] += number_of_pets


def get_stock_count(pet_shop):
    '''Given the pet_shop dictionary, it returns
    the total number of pets in the stock'''
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    '''Given the pet_shop dictionary and a specific breed type,
    it returns a LIST containing all pets of that specific breed.
    It returns an empty list if there are no pets of that breed.'''
    breed_list = []
    for pet in pet_shop["pets"]:
        breed_list.append(pet) if pet["breed"] == breed else None
    
    return breed_list


def find_pet_by_name(pet_shop, pet_name):
    '''Given the pet_shop dictionary and a pet name, it returns
    the full record of that specific pet.
    It returns the value "None" if a pet with that specific name
    is not part of the stock'''
    pet_found = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_found = pet
        # can't make it work as a ternary --- WHY?
        # pet_found.append(pet) if pet["name"] == pet_name else None

    return pet_found


def remove_pet_by_name(pet_shop, pet_name):
    '''Given the pet_shop dictionary and a pet name,
    it removes the record of the pet with that specific name
    from the stock.
    If the name if not found, the stock remains the same.'''
    for pet in pet_shop["pets"]:
        pet_shop["pets"].remove(pet) if pet["name"] == pet_name else None


def add_pet_to_stock(pet_shop, new_pet):
    '''Given the pet_shop dictionary it adds it to the stock'''
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    '''Given the customer dictionary,
    it returns the cash available by the customer'''
    return customer["cash"]


def remove_customer_cash(customer, amount_of_cash):
    '''Given the customer dictionary and an amount of cash,
    it subtract that amount from the cash available
    by that specific customer.
    
    It doesn't return any value'''
    customer["cash"] -= amount_of_cash


def get_customer_pet_count(customer):
    '''Given the customer dictionary,
    it returns the number of pets that specific customer
    already has'''
    return len(customer["pets"])


def add_pet_to_customer(customer, purchased_pet):
    '''Given the customer dictionary and a complete record
    (dictionary) of a new pet, it adds it to the LIST of the
    pets that specific customer already has.
    
    It doesn't return any value.'''
    customer["pets"].append(purchased_pet)


def customer_can_afford_pet(customer, pet):
    '''Given the customer dictionary and the distionary of a pet,
    it returns a BOOLEAN for whether or not the customer cash
    is equal or greater (can afford or not) that the price
    of that specific pet'''
    return customer["cash"] >= pet["price"]


def sell_pet_to_customer(pet_shop, pet, customer):
    '''Given the pet_shop, customer and pet dictionaries,
    it adds the pet record to the list of pets of the customer,
    and removes it from the stock.
    It increases the number of pets sold by one unit in the
    pet_shop dictionary, subtract the amount of money
    equal to the price of the pet from the cash available
    by the customer and adds it to the total cash in the pet_shop
    dictionary'''
    if pet and customer["cash"]>=pet["price"]:
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])

        # function added to remove pet from original stock
        # not required in original integration tests
        remove_pet_by_name(pet_shop, pet["name"])