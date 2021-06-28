from decimal import Decimal
from django.conf import settings
from product.models import Product


class Cart(object):
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем ПУСТУЮ корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # Добавление товара в корзину пользователя или обновление количеста товара
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # Сохранение данных в сессию
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # Перебираем товары в корзине и получаем товары из базы данных.
    def __iter__(self):
        product_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


