import pytest
from src.taxes import calculate_taxes

@pytest.mark.parametrize("price, tax_rate, expected", [
    (100, 10, 110.0),
    (50, 5, 52.5)
])
def test_calculate_taxes(price, tax_rate, expected):
    result = calculate_taxes(price, tax_rate)
    assert result == expected

def test_calculate_taxes_errors():
    with pytest.raises(ValueError, match="Неверная цена"):
        calculate_taxes(-1, 10)

def test_calculate_taxes_errors_2():
    with pytest.raises(ValueError, match="Неверный налоговый процент"):
        calculate_taxes(100, 100)