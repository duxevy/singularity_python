def calculate_taxes(price: float, tax_rate: float) -> float:
    """
    Функция должна вычислять стоимость товара с учётом налога и возвращать результат (float).

    Требования:
    - Если `price` не положительная, функция должна возбуждать исключительную ситуацию `ValueError` с сообщением "Неверная цена".
    - Если `tax_rate` меньше нуля или больше или равен `100%`, функция должна возбуждать исключительную ситуацию `ValueError`с сообщением "Неверный налоговый процент".

    Пример использования:

    ```
    result = calculate_tax(100, 10)
    assert result == 110.0

    result = calculate_tax(50, 5)
    assert result == 52.5
    ```
    """
    if price <= 0:
        raise ValueError("Неверная цена")
    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")

    tax = price * tax_rate / 100
    total_price = price + tax
    return total_price