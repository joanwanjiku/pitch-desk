import unittest
from app.models import Category

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.category = Category(name='Job')

    # def tearDown(self):
    #     Category.query.delete()

    def test_instance_variables(self):
        self.assertEquals(self.category.name, 'Job')
       

    def test_save_pitch(self):
        self.category.save_category()
        self.assertTrue(len(Category.query.all()) > 0)
