from django.test import TestCase
from django.core.urlresolvers import reverse
from users.models import User
from publishings.models import Publishing
# Create your tests here.

class PublishingsTest(TestCase):
    def setUp(self):
        # one user
        self.user = User.objects.create_user(
            username='photopublishings',
            email='photopublishings@email.com',
            password='demilovato')

        # one publishing
        self.publishing = Publishing.objects.create(
            user=self.user,
            text='text of proof',
            photo='/media/publishings/2017-05-01/avril_smile.png')

    def test_models(self):
        self.assertTrue(self.publishing)

    def test_views(self):
        self.assertTrue(self.client.login(
            username='photopublishings', password='demilovato'))

        res = self.client.get(reverse('publishings:list'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('publishings:create'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('publishings:detail',
            args=(self.publishing.id,)))
        self.assertEqual(res.status_code, 200)
