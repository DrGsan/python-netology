import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

contacts_list = []
new_list = []

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    for row in rows:
        contacts_list.append(','.join(row))

# TODO 1: выполните пункты 1-3 ДЗ
patterns = [
    ['^(\w+)( |,)(\w+)( |,)(\w+|),(,+|)(,,,|[А-Яа-я]+)', r'\1,\3,\5,\7'],
    ['(\+7|8)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})', r'+7(\3)\4-\5-\6'],
    ['\(?доб\.\s(\d{4})\)*', r'доб.\1']
]

for contact in contacts_list:
    for pattern in patterns:
        find = re.findall(pattern[0], contact)
        contact = re.sub(pattern[0], pattern[1], contact)
    print(contact)
    new_list.append(contact.split(','))

fname_sname = []
for contact in new_list:
    fname_sname.append(contact[0] + contact[1])

del_cont = []
for i in range(1, len(new_list) - 1):
    for m in range(i + 1, len(new_list)):
        if new_list[i][0] == new_list[m][0]:
            for k in range(7):
                if new_list[i][k] == '':
                    new_list[i][k] = new_list[m][k]
            del_cont.append(new_list[m])

for d in del_cont:
    new_list.remove(d)
# pprint(correct_list)  # test


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)