from pprint import pprint

def get_cook_book(file_name):
    cook_book=dict()
    with open(file_name) as file:
        for line in file:
            dish_name=line.strip()
            counter=int(file.readline())

            temp_list=[]
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().strip().split('|', ' ')
                temp_list.append(
                    {'Название ингридиента':ingredient_name, 'Количество': quantity, 'Ед. измерения': measure}
                )
                cook_book[dish_name]=temp_list


                file.readline()
                
    return cook_book
            
pprint(get_cook_book('recipes.txt'))

