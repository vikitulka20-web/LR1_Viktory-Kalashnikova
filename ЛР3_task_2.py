# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=","):
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    common_participants = [participant for participant in participants1 if participant in participants2]

    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, "|")
print(f"Общие участники: {common}")
print(f"Количество общих участников: {len(common)}")

print("\nПример с разделителем по умолчанию:")
participants1_default = "Иванов,Петров,Сидоров"
participants2_default = "Петров,Сидоров,Смирнов"
common_default = find_common_participants(participants1_default, participants2_default)
print(f"Общие участники: {common_default}")

print("\nПример без общих участников:")
participants_no_common1 = "Иванов,Петров,Сидоров"
participants_no_common2 = "Кузнецов,Смирнов,Попов"
common_no = find_common_participants(participants_no_common1, participants_no_common2)
print(f"Общие участники: {common_no}")