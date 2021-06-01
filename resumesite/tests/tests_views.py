from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.parametrize('param', ['home'])  # testing if the get response of the site works
def test_render_views(client, param):
    temp_url = reverse(param)  # reverse gets URL by matching the 'name' param provided (specified in views.py)
    resp = client.get(temp_url)  # iniciating a get request
    assert resp.status_code == 200


@pytest.fixture
def user_message():
    return {'message_name': 'something', 'message_email': 'email@email.com', 'message': 'Message for the user'}


@pytest.mark.django_db
def test_send_email(client, user_message):
    message_url = reverse('home')
    resp = client.post(message_url, user_message)
    assert resp.status_code == 200
