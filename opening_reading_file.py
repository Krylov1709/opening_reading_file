from pprint import pprint

reading_file = "recipe.txt"

def reading_recipe(reading_file: str) -> dict:
    with open(reading_file, "r", encoding='utf-8') as open_file:
        recipe = {}
        for line in open_file:
            dish = line.strip()
            recipe[dish]=[]
            amount_ingredient = open_file.readline().strip()
            for i in range(int(amount_ingredient)):
                line = open_file.readline().strip().split('|')
                ingredient = {"ingredient_name": line[0], "quantity": line[1], "measure": line[2]}
                recipe[dish].append(ingredient)
            delet_line = open_file.readline()
    return recipe

def get_shop_list_by_dishes(dishes, person_count):
    recipe_dish = reading_recipe(reading_file)
    shop_list = {}
    for dish in dishes:
        if dish in recipe_dish:
            for ingredient in recipe_dish[dish]:
                if ingredient["ingredient_name"] not in shop_list:
                    amount = {"quantity": int(ingredient["quantity"])*person_count, "measure": ingredient["measure"]}
                    shop_list[ingredient["ingredient_name"]] = amount
                else:
                    shop_list[ingredient["ingredient_name"]]["quantity"] += int(ingredient["quantity"])*person_count
    return shop_list

shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос','Запеченный картофель'], 3)
pprint (shop_list)
