# Ввести предложение состоящее из двуз слов. Поменять местами слова, добавить 
# восклицательный знак в начало и конец, слова разделить 3 символами (пробел, восклицательный знак
# и ещё пробел), вывести итоговое предложение на экран. Задание необходимо выполнить 3-мя способами форматирования

# Dibrie Dni.
Slovo = "Dibrie Dni."
print ("!Dni ! Dibrie.!")

# конкатенация
first_slovo_1 = "Dibrie"
second_slovo_2 = "Dni"
print (first_slovo_1 + second_slovo_2)

# % - форматирование
s1_first_slovo_1 = "Dibrie"
s1_second_slovo_2 = "Dni"
print ("%s %d" % (s1_first_slovo_1, s1_second_slovo_2))

# template - строки 
from string import Template 
s2_first_slovo_1 = "Dibrie"
s2_second_slovo_2 = "Dni"
print ("{} {}".format(s2_first_slovo_1, s2_second_slovo_2))

# погружение в f - cтроки
s3_first_slovo_1 = "Dibrie"
s3_second_slovo_2 = "Dni"
print (f"{s3_first_slovo_1} {s3_second_slovo_2 }")
