"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001), f"we dont have 1001 books"

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1000)

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 10)
        assert product in cart.products
        assert cart.products[product] == 10

    def test_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 3)
        assert product in cart.products
        assert cart.products[product] == 7

    def test_buy_products(self, cart, product):
        cart.add_product(product, 10)
        cart.buy()
        assert product.quantity == 990
        cart.add_product(product, 1000)
        with pytest.raises(ValueError):
            cart.buy()
