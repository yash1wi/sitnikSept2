for i in range(1, 180):
    file_name = f"photo{i}.txt"
    file = open(file_name, "w")
    print(f"Файл {file_name} успешно создан")

print("Все файлы успешно созданы")