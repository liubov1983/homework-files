from pprint import pprint


def get_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='UTF-8') as file:
        for line in file:
            recipe_name = line.strip()
            counter = int(file.readline())

            temp_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_list.append(
                    {'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity), 'measure': measure.strip()}
                )
            cook_book[recipe_name] = temp_list
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, file_name):
    recipe = {}
    cook_book = get_cook_book(file_name)

    for i in dishes:
        for dish in cook_book[i]:
            recipe[dish['ingredient_name']] = {'measure': dish['measure'], 'quantity': dish['quantity'] * person_count}
    return recipe


pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2, 'data.txt'))
