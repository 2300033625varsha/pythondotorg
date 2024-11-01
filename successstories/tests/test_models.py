import unittest
from your_app.models import Product  # Adjust the import based on your project structure
from your_app.database import db_session  # Assuming you're using SQLAlchemy or similar

class TestProductModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a test product before running the tests."""
        cls.product = Product(name='Original Product', price=29.99, description='An original product.', category='Test Category')
        db_session.add(cls.product)
        db_session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests are done."""
        db_session.delete(cls.product)
        db_session.commit()

    def test_update_product(self):
        """Test the UPDATE operation for a product."""
        # Update the product's details
        self.product.name = 'Updated Product'
        self.product.price = 39.99
        self.product.description = 'An updated product.'
        self.product.category = 'Updated Category'
        db_session.commit()

        # Fetch the updated product from the database
        updated_product = db_session.query(Product).filter_by(id=self.product.id).first()

        # Assertions to check if the updated product matches expected values
        self.assertIsNotNone(updated_product)  # Ensure the product is found
        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.price, 39.99)
        self.assertEqual(updated_product.description, 'An updated product.')
        self.assertEqual(updated_product.category, 'Updated Category')

if __name__ == '__main__':
    unittest.main()

