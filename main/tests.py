from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        # Membuat instance Product untuk pengujian
        self.product = Product.objects.create(
            name="Jacket",
            price=150000,
            description="A stylish jacket",
            size="M",
            stock=10
        )

    def test_product_creation(self):
        # Memeriksa apakah produk dibuat dengan benar
        self.assertEqual(self.product.name, "Jacket")
        self.assertEqual(self.product.price, 150000)
        self.assertEqual(self.product.description, "A stylish jacket")
        self.assertEqual(self.product.size, "M")
        self.assertEqual(self.product.stock, 10)

    def test_product_string_representation(self):
        # Memeriksa representasi string dari produk
        self.assertEqual(str(self.product), "Jacket")
