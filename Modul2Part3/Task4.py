def calculate_salary(sales):
    base_salary = 200
    if sales <= 500:
        commission_rate = 0.03
    elif 500 < sales <= 1000:
        commission_rate = 0.05
    else:
        commission_rate = 0.08
    commission = sales * commission_rate
    total_salary = base_salary + commission
    return total_salary
manager_salaries = []
for i in range(3):
    sales = float(input(f"введите объем продаж для менеджера {i + 1}: "))
    salary = calculate_salary(sales)
    manager_salaries.append({"manager_id": i + 1, "sales": sales, "salary": salary})
best_manager = max(manager_salaries, key=lambda x: x["salary"])
best_manager["salary"] += 200

print("\n ---итоги---")
for manager in manager_salaries:
     print(f"Менеджер {manager['manager_id']}: продажи = {manager['sales']:.2f}, зарпла = {manager['salary']:.2f}")
print(f"лучший менеджер: Менеджер {best_manager['manager_id']} c зарплатой {best_manager['salary']:.2f} (включая премию)")