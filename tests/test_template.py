from .context import app
from unittest import TestCase



class test_post_user(TestCase):
    def setUp(self):
        immogarantie_flask_app = app.create_app()
        self.test_api = immogarantie_flask_app.test_client()

    def test_thing(self):
        response = self.test_api.get('/')
        assert "shit" == "fuck"
