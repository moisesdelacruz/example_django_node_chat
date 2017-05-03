from django.test import TestCase
from django.core.urlresolvers import reverse
# models
from users.models import User

from datetime import datetime

# Create your tests here.

class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='selenagomez',
            first_name='Selena',
            last_name='Gomez',
            email='selenagomez@test.com',
            birthday=datetime.strptime('1992-07-20', '%Y-%m-%d'),
            photo='/media/selenagomez/selena.jpg',
            password='demilovato'
        )

    def test_model(self):
        self.assertTrue(self.user)
        self.assertEqual(
            self.user.get_full_name(),
            ' '.join([self.user.first_name, self.user.last_name]))

        self.assertEqual(self.user.get_short_name(), self.user.first_name)

    def test_views(self):
        self.client.login(username='selenagomez', password='demilovato')

        res = self.client.get(reverse('users:detail', args=(self.user.username,)))
        self.assertEqual(res.status_code, 200)
