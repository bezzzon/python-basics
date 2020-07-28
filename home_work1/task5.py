"""
- Запросите у пользователя значения выручки и издержек фирмы.
- Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
- Выведите соответствующее сообщение.
- Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
- Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

debit = float(input("Please input company's debit balance: "))
credit = float(input("Please input company's credit balance: "))

if debit > credit:
    print('Company works with profit')
    profitability = (debit - credit) / debit
    employees = int(input("Please input number of the company's employees: "))
    print(f'Profitability is: {profitability * 100}%\nThe profit per one employee: {(debit - credit) / employees}')
elif debit < credit:
    print('Company works with loss')
else:
    print('Company works without either profit or loss')
