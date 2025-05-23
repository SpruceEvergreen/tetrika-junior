from itertools import groupby
import wikipediaapi
import csv

def get_categorymembers(categorymembers):
    for category in categorymembers.values():
        yield category.title

wikipedia = wikipediaapi.Wikipedia(user_agent='user-agent', language='ru')

page_cat = wikipedia.page("Категория:Животные по алфавиту")

categories = get_categorymembers(page_cat.categorymembers)

next(categories)
categories = sorted(categories)

groups = groupby(categories, lambda k: k[0])

animals = []
for k, v in groups:
    temp = [f"{k}", len(list(v))]
    animals.append(temp)

with open('beasts.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(animals)



# Для решения задания используется wikipediaapi, которой покрыт
# тестами разработчика (https://github.com/martin-majlis/Wikipedia-API/tree/master/tests).
