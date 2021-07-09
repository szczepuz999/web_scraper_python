# read animals.txt
old_animals = open('animals.txt', 'r', encoding='utf-8')
new_animals = open('animals_new.txt', 'w', encoding='utf-8')


for animal in old_animals:
    animal = animal.rstrip()
    new_animals.write(animal + ' ')


# and write animals_new.txt
old_animals.close()
new_animals.close()