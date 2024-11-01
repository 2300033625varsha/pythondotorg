import unittest
from your_app.models import Product  # Adjust the import based on your project structure
from your_app.database import db_session  # Assuming you're using SQLAlchemy or similar

class TestProductModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test products before running the tests."""
        cls.product1 = Product(name='Product A', price=10.99, description='First test product.', category='Category 1')
        cls.product2 = Product(name='Product B', price=20.99, description='Second test product.', category='Category 2')
        cls.product3 = Product(name='Product C', price=15.99, description='Third test product.', category='Category 1')
        
        db_session.add(cls.product1)
        db_session.add(cls.product2)
        db_session.add(cls.product3)
        db_session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests are done."""
        db_session.delete(cls.product1)
        db_session.delete(cls.product2)
        db_session.delete(cls.product3)
        db_session.commit()

    def test_find_products_by_category(self):
        """Test finding products by their category."""
        # Query products by category
        found_products = db_session.query(Product).filter_by(category='Category 1').all()

        # Assertions to check if the correct products are retrieved
        self.assertEqual(len(found_products), 2)  # Ensure we have two products in Category 1
        self.assertIn(self.product1, found_products)  # Check that product1 is in the list
        self.assertIn(self.product3, found_products)  # Check that product3 is in the list

    def test_find_no_products_in_category(self):
        """Test finding products in a category with no products."""
        found_products = db_session.query(Product).filter_by(category='Nonexistent Category').all()

        # Ensure no products are found
        self.assertEqual(len(found_products), 0)

if __name__ == '__main__':
    unittest.main()
