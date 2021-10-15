from pprint import pprint


def get_cook_book(file_name):
    cook_book = dict()
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            dish_name = line.strip()
            counter = int(file.readline())

            temp_list = []
            cook_book[dish_name] = temp_list
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_list.append(
                    {'Название ингридиента': ingredient_name, 'Количество': quantity, 'Ед. измерения': measure})

            file.readline()

    return cook_book


pprint(get_cook_book('recipes.txt'))


def get_shop_list_by_dishes(dishes, person_count):
    guests_menu = []
    guests_menu = get_cook_book('recipes.txt')[dishes]
    menu = {}
    # print(guests_menu)
    for elements in guests_menu:
        menu.setdefault(elements['Название ингридиента'], elements)
        del elements['Название ингридиента']
        a = int(elements['Количество'])
        quantity = a * person_count
        elements['Количество']=quantity
    return menu


pprint(get_shop_list_by_dishes('Омлет', 4))


