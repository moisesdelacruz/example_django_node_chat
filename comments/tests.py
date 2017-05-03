from django.test import TestCase
from comments.models import Comment
from users.models import User
from publishings.models import Publishing

# Create your tests here.

class CommentTest(TestCase):
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
        self.assertTrue(self.user)
        self.assertTrue(self.publishing)

        self.assertTrue(Comment.objects.create(
            publishing=self.publishing, user=self.user, text='Hello Test'))
