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

    for name in dishes:
        for dish in cook_book[name]:
            if dish['ingredient_name'] in recipe:
                recipe[dish['ingredient_name']]['quantity'] += dish['quantity'] * person_count
            else:
                recipe[dish['ingredient_name']] = {'measure': dish['measure'], 'quantity': dish['quantity'] * person_count}
    return recipe


#pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Фахитос'], 5, 'data.txt'))

def sort_text(text_one, text_two, text_three):
    text_dict = {}
    with open(text_one, encoding='UTF-8') as file_one:
        text1 = file_one.readlines()
        text_dict[len(text1)] = [text_one, text1]

    with open(text_two, encoding='UTF-8') as file_two:
        text2 = file_two.readlines()
        text_dict[len(text2)] = [text_two, text2]

    with open(text_three, encoding='UTF-8') as file_three:
        text3 = file_three.readlines()
        text_dict[len(text3)] = [text_three, text3]

    with open('task3.txt', 'a', encoding='UTF-8') as file:
        text_list = list(text_dict.keys())
        text_list.sort()
        for item in text_list:
            file.write(f'{text_dict[item][0]}\n')
            file.write(f'{item}\n')
            file.write(f'{"".join(text_dict[item][1])}\n')


sort_text('1.txt', '2.txt', '3.txt')
