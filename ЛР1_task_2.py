# TODO Найдите количество книг, которое можно разместить на дискете
V_disk = 1.44
symbol = 25
line = 50
page = 100

all_symbols = symbol * line * page
weight = all_symbols * 4 / 1024 / 1024
count_books = round(V_disk // weight)

print("Количество книг, помещающихся на дискету:", count_books)
