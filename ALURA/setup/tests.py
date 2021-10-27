from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/eduardo/Downloads')



    def tearDown(self):
        self.browser.quit()
