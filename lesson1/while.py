# Пройдите в цикле по списку пока не встретите имя
# "Валера". Когда найдете напишите "Валера нашелся".
# Подсказка: используйте метод pop()
# Перепишите предыдущий пример в виде функции
# find_person(name), которая ищет имя в списке.
my_list = ["Vasya", "Masha", "Petya", "Valera", "Sasha"]
while my_list:
    name = my_list.pop()
    if name == 'Valera':
        print(name + " nastalo tvoe vremya")
        break

print(my_list)

def find_person(name):
    if name in my_list:
        print(name + " nastalo tvoe vremya")

find_person('Masha')

# Написать функцию ask_user() чтобы помощью input()
# спрашивать пользователя “Как дела?”,
# пока он не ответит “Хорошо”
def ask_user():
    answer = ''
    while answer != 'horosho':
        answer = input("Kak dela? ")
ask_user()

# При помощи функции get_answer() отвечать на вопросы
# пользователя в ask_user(), пока он не скажет “Пока!”
