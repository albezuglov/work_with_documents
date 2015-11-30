from django.test import TestCase
from .models import Order, OrderItem
# Create your tests here.

class OrderTestCase(TestCase):
    def setUp(self):
        order1 = Order.objects.create(name='order1', type='test')
        OrderItem.objects.create(name='item1 order1', order=order1, price=10, quantity=1)
        OrderItem.objects.create(name='item2 order1', order=order1, price=20, quantity=2)

    def test__total_of_order_must_calculated(self):
        order1 = Order.objects.get(name='order1')
        self.assertEqual(order1.total, 50)

        OrderItem.objects.create(name='item3 order1', order=order1, price=30, quantity=3)
        self.assertEqual(order1.total, 140)

        OrderItem.objects.filter(name='item2 order1').update(quantity=4)
        self.assertEqual(order1.total, 180)

