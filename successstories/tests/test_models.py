import unittest
from your_app.models import Product  # Adjust the import based on your project structure
from your_app.database import db_session  # Assuming you're using SQLAlchemy or similar

class TestProductModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a test product before running the tests."""
        cls.product = Product(name='Test Product', price=19.99, description='A test product.', category='Test Category')
        db_session.add(cls.product)
        db_session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests are done."""
        db_session.delete(cls.product)
        db_session.commit()

    def test_find_product_by_name(self):
        """Test finding a product by its name."""
        # Query the product by its name
        found_product = db_session.query(Product).filter_by(name='Test Product').first()

        # Assertions to check if the found product matches expected values
        self.assertIsNotNone(found_product)  # Ensure the product is found
        self.assertEqual(found_product.name, 'Test Product')
        self.assertEqual(found_product.price, 19.99)
        self.assertEqual(found_product.description, 'A test product.')
        self.assertEqual(found_product.category, 'Test Category')

    def test_find_nonexistent_product(self):
        """Test finding a product by a name that doesn't exist."""
        found_product = db_session.query(Product).filter_by(name='Nonexistent Product').first()
        
        # Ensure no product is found
        self.assertIsNone(found_product)

if __name__ == '__main__':
    unittest.main()
