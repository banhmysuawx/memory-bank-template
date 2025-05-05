from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class JWTAuthenticationTests(APITestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpass123"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.token_obtain_url = reverse('token_obtain_pair')
        self.token_refresh_url = reverse('token_refresh')
        self.token_verify_url = reverse('token_verify')

    def test_should_obtain_token_pair_when_credentials_valid(self):
        """Test that we can obtain a token pair with valid credentials"""
        response = self.client.post(
            self.token_obtain_url,
            {'username': self.username, 'password': self.password},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_should_fail_obtain_token_when_credentials_invalid(self):
        """Test that token obtain fails with invalid credentials"""
        response = self.client.post(
            self.token_obtain_url,
            {'username': self.username, 'password': 'wrongpass'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_should_refresh_token_when_refresh_token_valid(self):
        """Test that we can refresh an access token with a valid refresh token"""
        # First obtain tokens
        refresh = RefreshToken.for_user(self.user)
        
        response = self.client.post(
            self.token_refresh_url,
            {'refresh': str(refresh)},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_should_verify_token_when_token_valid(self):
        """Test that we can verify a valid token"""
        # First obtain tokens
        refresh = RefreshToken.for_user(self.user)
        access_token = refresh.access_token
        
        response = self.client.post(
            self.token_verify_url,
            {'token': str(access_token)},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_fail_verify_token_when_token_invalid(self):
        """Test that token verification fails with invalid token"""
        response = self.client.post(
            self.token_verify_url,
            {'token': 'invalid-token'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED) 