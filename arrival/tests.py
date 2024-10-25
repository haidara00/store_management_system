from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Arrival
from stock.models import Category, Stock


class ArrivalModelTest(TestCase):
    def setUp(self):
        self.testUser = get_user_model().objects.create_superuser(
            username="testuser",
            password="testpass123",
        )
        self.testCategory = Category.objects.create(name="testCatgory")
        
        self.testStock = Stock.objects.create(
            name="Getzner",
            initial_quantity=300,
            price=200.00,
            category=self.testCategory
        )
        
        self.testArrival = Arrival.objects.create(
            stock=self.testStock,
            agent=self.testUser,
            quantity=1000
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
        self.assertEqual(self.testStock.initial_quantity, stock1.initial_quantity)
        self.assertEqual(self.testStock.price, stock1.price)
    
    def test_false_teststock(self):
        stock1 = Stock.objects.get(id=1)
        self.assertNotEqual("blablabla", stock1.name)
        self.assertNotEqual(-4, stock1.initial_quantity)
        self.assertNotEqual(100000, stock1.price)
        
    def test_testArrival(self):
        arrivalObj = Arrival.objects.get(id=1)
        self.assertEqual(arrivalObj.agent, self.testArrival.agent)
        self.assertEqual(arrivalObj.agent.username, self.testArrival.agent.username)
        self.assertEqual(arrivalObj.agent.password, self.testArrival.agent.password)
        self.assertEqual(arrivalObj.quantity, self.testArrival.quantity)
        self.assertEqual(arrivalObj.stock, self.testArrival.stock)
        self.assertEqual(arrivalObj.stock.name, self.testArrival.stock.name)