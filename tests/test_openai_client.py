import unittest
from src.openai_client import OpenAIClient


class TestOpenAIClient(unittest.TestCase):
    def setUp(self):
        # Initialize the OpenAIClient with a dummy ID for testing
        self.client = OpenAIClient("dummy_id")

    def test_create_thread_and_run(self):
        # Test the create_thread_and_run method
        # This is a placeholder test, you'll need to mock API responses
        self.assertIsNotNone(self.client.create_thread_and_run("test"))

    # Add more tests for other methods of OpenAIClient


if __name__ == "__main__":
    unittest.main()
