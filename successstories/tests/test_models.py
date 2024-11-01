import unittest
from your_app.models import Product  # Adjust the import based on your project structure
from your_app.database import db_session  # Assuming you're using SQLAlchemy or similar

class TestProductModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test products before running the tests."""
        cls.product1 = Product(name='Product 1', price=10.99, description='First test product.', category='Category 1')
        cls.product2 = Product(name='Product 2', price=20.99, description='Second test product.', category='Category 2')
        db_session.add(cls.product1)
        db_session.add(cls.product2)
        db_session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests are done."""
        db_session.delete(cls.product1)
        db_session.delete(cls.product2)
        db_session.commit()

    def test_list_all_products(self):
        """Test listing all products."""
        # Retrieve all products from the database
        products = db_session.query(Product).all()

        # Assertions to check if the correct products are retrieved
        self.assertEqual(len(products), 2)  # Ensure we have two products
        self.assertIn(self.product1, products)  # Check that product1 is in the list
        self.assertIn(self.product2, products)  # Check that product2 is in the list

    def test_empty_product_list(self):
        """Test listing products when no products exist."""
        # Clean up all products
        db_session.query(Product).delete()
        db_session.commit()

        # Retrieve all products from the database
        products = db_session.query(Product).all()

        # Ensure the product list is empty
        self.assertEqual(len(products), 0)

if __name__ == '__main__':
    unittest.main()
