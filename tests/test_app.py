from src.app import adicionar_gasto, total_gastos, gastos

def setup_function():
    gastos.clear()

def test_adicionar_gasto():
    adicionar_gasto("Mercado", 50)
    assert total_gastos() == 50

def test_valor_negativo():
    import pytest
    with pytest.raises(ValueError):
        adicionar_gasto("Erro", -10)

def test_total_varios_gastos():
    adicionar_gasto("A", 10)
    adicionar_gasto("B", 20)
    assert total_gastos() == 30