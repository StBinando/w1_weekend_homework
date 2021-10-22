import pdb

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