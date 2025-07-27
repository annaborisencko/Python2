from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
import re
# Приводим первые три поля к виду Фамилия, Имя, Отчество
for item in contacts_list[1:]:
  fio = " ".join(item[:2])
  # print(fio)
  pattern = r"(\w+)\s+(\w+)\s*(\w*)"
  result = re.match(pattern, fio)
  item[0] = result.group(1)
  item[1] = result.group(2)
  item[2] = result.group(3)

# Объединяем информацию о дублях и исключаем дубли из общего списка
contacts_list_copy = []
double_index = []
for index, contact in enumerate(contacts_list):
  fi = " ".join(contact[:2])
  for i in range(index+1, len(contacts_list)):
    fi_i = " ".join(contacts_list[i][:2])
    if fi == fi_i and index != i:
      right_contact = contacts_list[index]
      double_contact = contacts_list[i]
      double_index.append(i)
      for f_index, field in enumerate(right_contact):
        # print(f'Индекс поля {f_index}, значение {field}')
        if field in ("", None):
          right_contact[f_index] = double_contact[f_index]
  if index not in double_index:
    contacts_list_copy.append(contact)

# Приводим телефоны в адресной книге к формату +7(999)999-99-99
phone_pattern = r"(\+7|8)?\s*\(?(\d{3})\)?-?\s*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(?(доб.\s*\d+)?\)?"
re_phone = r"+7(\2)\3-\4-\5 \6"
for contact in contacts_list_copy:
  # phone = re.findall(phone_pattern,contact[-2])
  phone = re.sub(phone_pattern, re_phone, contact[-2])
  contact[-2] = phone

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list_copy)