from django.test import TestCase
from django.utils import timezone

from .models import Supplier, Debt
from . import models


class SupplierModelTest(TestCase):
    def setUp(self):
        self.testSupplier = Supplier.objects.create(
            first_name="testSupplier",
            last_name="Haidara",
            email="test@email.com",
           
            is_male=True   
        )
        
    def test_test_supplier(self):
        obj = Supplier.objects.get(id=1)
        self.assertEqual(obj.first_name, self.testSupplier.first_name)
        self.assertEqual(obj.last_name, self.testSupplier.last_name)
        self.assertEqual(obj.email, self.testSupplier.email)
    def test_false_test_supplier(self):
        obj = Supplier.objects.get(id=1)
        self.assertNotEqual(obj.first_name, "Ismail")
        self.assertNotEqual(obj.last_name, "Traoré")
        self.assertNotEqual(obj.email, "maamammnakan@gmail.com")

class DebtModelTest(TestCase):
    def setUp(self):
        self.testSupplier = Supplier.objects.create(
            first_name="testSupplier",
            last_name="Haidara",
            email="test@email.com",
            is_male=True   
        )
        self.testDept = Debt.objects.create(
            supplier = self.testSupplier,
            amount = 2000.00,
            borrowed_at=timezone.now()
        )
            
    def test_test_debt(self):
        obj = Debt.objects.get(id=1)
        self.assertEqual(obj.supplier.first_name, self.testSupplier.first_name)
        self.assertEqual(obj.supplier.first_name, self.testSupplier.first_name)
        self.assertEqual(obj.supplier.first_name, self.testSupplier.first_name)

class Reinbourse(TestCase):
    def setUp(self):
        self.testSupplier = Supplier.objects.create(
            first_name="testSupplier",
            last_name="Haidara",
            email="test@email.com",
            is_male=True    
        )
        self.testReinbourse = models.Reinbourse.objects.create(
            supplier=self.testSupplier,
            amount=20000.00,
            paid_at=timezone.now()
        )
        
    def test_test_supplier(self):
        obj = Supplier.objects.get(id=1)
        self.assertEqual(obj.first_name, self.testSupplier.first_name)
        self.assertEqual(obj.last_name, self.testSupplier.last_name)
        self.assertEqual(obj.email, self.testSupplier.email)
    
    def test_false_test_supplier(self):
        obj = Supplier.objects.get(id=1)
        self.assertNotEqual(obj.first_name, "Ismail")
        self.assertNotEqual(obj.last_name, "Traoré")
        self.assertNotEqual(obj.email, "maamammnakan@gmail.com")
