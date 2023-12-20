for i in range(1, 31):
    file_name = f"file{i}.txt"
    file = open(file_name, "w")
    print(f"Файл {file_name} успешно создан")

print("Все файлы успешно созданы")