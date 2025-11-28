from rest_framework.test import APITestCase
from . import models


class TestTweetAPI(APITestCase):
    """
    test /tweets API endpoints (GET, POST)
    """

    PAYLOAD_CONTENT = "This is a test tweet."
    URL = "/api/v1/tweets/"

    def setUp(self):
        print("🎈STARTING TestTweetAPI tests...")
        self.user = models.CustomUser.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        models.Tweet.objects.create(
            payload=self.PAYLOAD_CONTENT,
            user_id=self.user.id,
        )
        print("🎈Setup complete.")

    def test_get_tweets(self):
        print("🎈Testing GET /api/v1/tweets/ endpoint...")
        response = self.client.get(self.URL)
        data = response.json()
        print("🎈Response data:", data)

        self.assertEqual(
            response.status_code,
            200,
        )
        print("🎈Status code is 200.")

        self.assertEqual(
            len(response.data),
            1,
        )
        print("🎈Response data length is 1.")

        self.assertEqual(
            response.data[0]["payload"],
            self.PAYLOAD_CONTENT,
        )
        print(f"🎈Payload {response.data[0]['payload']}")

    def test_post_tweet(self):
        new_payload = "This is another test tweet."
        response = self.client.post(
            self.URL,
            data={
                "payload": new_payload,
                "user": self.user.id,
            },
        )

        self.assertEqual(
            response.status_code,
            200,
        )
        self.assertEqual(
            response.data["payload"],
            new_payload,
        )


# /api/v1/tweets/<int:pk>: Test GET, PUT and DELETE methods
class TestTweetDetailAPI(APITestCase):
    """
    test /tweets/<int:pk> API endpoints (GET, PUT, DELETE)
    """

    PAYLOAD_CONTENT = "This is a test tweet for detail view."
    URL_TEMPLATE = "/api/v1/tweets/{}/"

    def setUp(self):
        print("🎈STARTING TestTweetDetailAPI tests...")
        self.user = models.CustomUser.objects.create_user(
            username="detailtestuser",
            password="detailtestpassword",
        )
        self.tweet = models.Tweet.objects.create(
            payload=self.PAYLOAD_CONTENT,
            user_id=self.user.id,
        )
        print("🎈Setup complete.")

    def test_get_tweet_detail(self):
        print("🎈Testing GET /api/v1/tweets/<int:pk>/ endpoint...")
        url = self.URL_TEMPLATE.format(self.tweet.id)
        response = self.client.get(url)
        data = response.json()
        print("🎈Response data:", data)

        self.assertEqual(
            response.status_code,
            200,
        )
        print("🎈Status code is 200.")

        self.assertEqual(
            response.data["payload"],
            self.PAYLOAD_CONTENT,
        )
        print(f"🎈Payload {response.data['payload']}")

    def test_put_tweet_detail(self):
        print("🎈Testing PUT /api/v1/tweets/<int:pk>/ endpoint...")
        url = self.URL_TEMPLATE.format(self.tweet.id)
        updated_payload = "This is an updated test tweet."

        self.client.force_login(self.user)

        response = self.client.put(
            url,
            data={
                "payload": updated_payload,
                "user": self.user.id,
            },
        )

        self.assertEqual(
            response.status_code,
            200,
        )
        print("🎈Status code is 200.")

        self.assertEqual(
            response.data["payload"],
            updated_payload,
        )
        print(f"🎈Updated payload {response.data['payload']}")

    def test_delete_tweet_detail(self):
        print("🎈Testing DELETE /api/v1/tweets/<int:pk>/ endpoint...")
        url = self.URL_TEMPLATE.format(self.tweet.id)

        self.client.force_login(self.user)

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            204,
        )
        print("🎈Status code is 204.")

        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            404,
        )
        print("🎈Verified tweet deletion with 404 on GET request.")
