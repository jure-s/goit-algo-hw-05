import subprocess

def run_task(task_name, script_name):
    print(f"\nЗапуск {task_name}...")
    print("=" * 50)
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Помилка:")
        print(result.stderr)
    print("=" * 50)

def main():
    tasks = {
        "1": ("Тестування хеш-таблиці", "task_1/test_hash_table.py"),
        "2": ("Тестування двійкового пошуку", "task_2/test_binary_search.py"),
        "3": ("Тестування пошуку підрядка", "task_3/test_substring_search.py"),
        "4": ("Аналіз продуктивності пошуку підрядка", "task_3/substring_search.py"),
        "5": ("Запустити всі завдання", None)
    }

    while True:
        print("\nОберіть завдання для запуску:")
        for key, (task_name, _) in tasks.items():
            print(f"{key}. {task_name}")
        print("0. Вихід")

        choice = input("Введіть номер завдання: ")
        if choice == "0":
            print("Вихід...")
            break
        elif choice == "5":
            for task_name, script in tasks.values():
                if script:
                    run_task(task_name, script)
        elif choice in tasks:
            run_task(*tasks[choice])
        else:
            print("Невірний вибір. Будь ласка, оберіть коректний номер.")

if __name__ == "__main__":
    main()