from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """ A test to test a model creation of user """

    def test_create_user_with_email_succesfully(self):
        """ A test function to test a user auth """
        email = "test@india.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """ Test the email for a new user is normalized """
        email = "test@INDIA.COM"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_new_user_email(self):
        """ testing for validation """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """ Test for creating a new super user """

        user = get_user_model().objects.create_superuser('test@india.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
