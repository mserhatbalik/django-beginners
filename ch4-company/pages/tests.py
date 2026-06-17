from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class HomepageTests(SimpleTestCase):
    # Testing URL Locations
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # Testing URL Names
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    # Testing Templates
    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    # Testing Elements
    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Company Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    # Testing URL Locations
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)

    # Testing URL Names
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    # Testing Templates
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    # Testing Elements
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Company About Page</h1>")
