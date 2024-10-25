from django.test import TestCase

from .models import Stock, Category


class StockTestModelTest(TestCase):
    def setUp(self):
        self.testCategory = Category.objects.create(name="testCategory")
        
        self.testStock = Stock.objects.create(
            name="test stock",
            initial_quantity=5,
            price=200.00,
            category=self.testCategory
            
        )
    
    def test_stock_contain(self):
        self.assertEqual(self.testStock.name, "test stock")
        self.assertEqual(self.testStock.initial_quantity, 5)
        self.assertEqual(self.testStock.price, 200.00)
    
    def test_stock_not_contain(self):
        self.assertNotEqual(self.testStock.name, "test sldkj stock")
        self.assertNotEqual(self.testStock.quantity, 50)
        self.assertNotEqual(self.testStock.price, 20.00)
