from functools import reduce

transactions = [
    {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
    {"id": 2, "type": "expense", "amount": 200, "currency": "USD"},
    {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
    {"id": 4, "type": "expense", "amount": 300, "currency": "USD"},
    {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
    {"id": 6, "type": "expense", "amount": 400, "currency": "EUR"},
    {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
]


def filter_transactions(transactions, transaction_type):
    return list(filter(lambda x: x['type'] == transaction_type, transactions))


def map_transactions(transactions, currency):
    return list(map(lambda x: x['amount'] if x['currency'] == currency else 0, transactions))


def reduce_transactions(transactions):
    return reduce(lambda x, y: x + y, transactions, 0)


def process_transactions(transactions, transaction_type, currency):
    filtered = filter_transactions(transactions, transaction_type)
    mapped = map_transactions(filtered, currency)
    total = reduce_transactions(mapped)
    return total


print(filter_transactions(transactions, "income"))


# [{'id': 1, 'type': 'income', 'amount': 1000, 'currency': 'USD'},
#  {'id': 3, 'type': 'income', 'amount': 500, 'currency': 'USD'},
#  {'id': 5, 'type': 'income', 'amount': 700, 'currency': 'USD'},
#  {'id': 7, 'type': 'income', 'amount': 100, 'currency': 'EUR'}]

# def test_transaction_processing():
#     assert map_transactions(filter_transactions(transactions, "income"), "USD") == [1000, 500, 700, 0]
#     assert reduce_transactions([1000, 500, 700, 0]) == 2200
#     assert process_transactions(transactions, "expense", 'EUR') == 400
#     # assert process_transactions(transactions, "expense", 'EUR') == 450
#     assert process_transactions(transactions, "invalid_type", 'USD') == 0
#
#     print("All test passed")


# fun17.py::test_transaction_processing FAILED                             [100%]
# fun17.py:40 (test_transaction_processing)
# 400 != 450
#
# Expected :450
# Actual   :400
# <Click to see difference>
#
# def test_transaction_processing():
#         assert map_transactions(filter_transactions(transactions, "income"), "USD") == [1000, 500, 700, 0]
#         assert reduce_transactions([1000, 500, 700, 0]) == 2200
#         assert process_transactions(transactions, "expense", 'EUR') == 400
# >       assert process_transactions(transactions, "expense", 'EUR') == 450
# E       AssertionError: assert 400 == 450
# E        +  where 400 = process_transactions([{'amount': 1000, 'currency': 'USD', 'id': 1, 'type': 'income'}, {'amount': 200, 'currency': 'USD', 'id': 2, 'type': 'expense'}, {'amount': 500, 'currency': 'USD', 'id': 3, 'type': 'income'}, {'amount': 300, 'currency': 'USD', 'id': 4, 'type': 'expense'}, {'amount': 700, 'currency': 'USD', 'id': 5, 'type': 'income'}, {'amount': 400, 'currency': 'EUR', 'id': 6, 'type': 'expense'}, ...], 'expense', 'EUR')
#
# fun17.py:45: AssertionError

# Launching pytest with arguments C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day2\fun17.py --no-header --no-summary -q in C:\Users\CSComarch\PycharmProjects\warsztat_python_14-10\day2
#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# fun17.py::test_transaction_processing PASSED                             [100%]All test passed
#
#
# ============================== 1 passed in 0.07s ==============================
#
# Process finished with exit code 0

if __name__ == '__main__':
    filter_transactions(transactions, 'incoming')
