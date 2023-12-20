
for i in range(1, 201):
    file_name = f"user{i}.txt"
    file = open(file_name, "w")
    print(f"Файл {file_name} успешно создан")

print("Все файлы успешно созданы")