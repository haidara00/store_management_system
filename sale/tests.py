from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Sale
from stock.models import Stock, Category

class SaleModelTest(TestCase):
    
    def setUp(self):
        self.testUser = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.testCategory = Category.objects.create(
            name="testCategory"
        )
        
        self.testStock = Stock.objects.create(
            name="Getzner",
            initial_quantity=300,
            price=200.00,
            category=self.testCategory
        )
        self.testSale = Sale.objects.create(
            agent=self.testUser,
            stock=self.testStock,
            quantity=5,
            
        )
    def test_testuser(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(self.testUser.username, user.username)
    
    def test_false_testuser(self):
        self.assertNotEqual(self.testUser.username, "Ismail")
        self.assertNotEqual(self.testUser.password, "Ismail")
    
    def test_teststock(self):
        stock1 = Stock.objects.get(id=1)
        self.assertEqual(self.testStock.name, stock1.name)
        self.assertEqual(self.testStock.quantity, stock1.quantity)
        self.assertEqual(self.testStock.price, stock1.price)
    
    def test_false_teststock(self):
        stock1 = Stock.objects.get(id=1)
        self.assertNotEqual("blablabla", stock1.name)
        self.assertNotEqual(-4, stock1.quantity)
        self.assertNotEqual(100000, stock1.price)
        
    def test_testSale(self):
        sale1 = Sale.objects.get(id=1)
        self.assertEqual(self.testSale.agent, sale1.agent)
        self.assertEqual(self.testSale.agent.username, sale1.agent.username)
        self.assertEqual(self.testSale.quantity, sale1.quantity)
        self.assertEqual(self.testSale.stock, sale1.stock)
        self.assertEqual(self.testSale.stock.name, sale1.stock.name)