import unittest
from app.models import Pitch, Category

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.category = Category(name='Job')
        self.pitch = Pitch(title = 'Get your first job', content= "I am the best you will ever find",category=self.category)

    def tearDown(self):
        # Category.query.delete()
        Pitch.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.pitch,Pitch))

    def test_instance_variables(self):
        self.assertEquals(self.pitch.title, 'Get your first job')
        self.assertEquals(self.pitch.content, 'I am the best you will ever find')
        self.assertEquals(self.pitch.category, self.category)

    def test_save_pitch(self):
        self.pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)
    
    # def test_get_pitch_by_id(self):
    #     self.pitch.save_pitch()
    #     pitch = Pitch.get_by_id()