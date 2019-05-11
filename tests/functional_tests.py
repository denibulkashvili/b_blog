"""Functional tests using Selenium"""
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class BlogTest(LiveServerTestCase):
    """Main test class"""

    @classmethod
    def setUpClass(cls):
        """Instantiates WebDriver and populates the database on every test run"""
        super().setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        """Quits Selenium at the end of every test"""
        cls.selenium.quit()
        super().tearDownClass()

    def test_b_blog_in_title(self):
        """Tests whether b_blog is in title"""
        self.selenium.get("http://localhost:8000")
        title = self.selenium.find_element_by_tag_name("h1")
        self.assertEqual("b_blog", title.text)
