# объявление функции
def get_month(language, number):
    ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        index_ru = number - 1
        return ru[index_ru]
    if language == 'en':
        index_en = number - 1
        return en[index_en]
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))