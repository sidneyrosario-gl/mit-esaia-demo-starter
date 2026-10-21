import unittest
from types import SimpleNamespace
from unittest.mock import patch
from app.service import documents, search, request_change
from app.model import OpenAIModel

class VisibleTests(unittest.TestCase):
    def test_public_policy_search(self):
        self.assertIn("travel", [d["id"] for d in search("alice", "meal limit")])
    def test_empty_context_does_not_call_openai(self):
        with patch("app.model.OpenAI") as client:
            self.assertIn("authorized source", OpenAIModel().answer("secret", []))
            client.assert_not_called()

    def test_policy_documents_have_metadata_and_markdown_bodies(self):
        policies = documents()
        self.assertEqual({doc["id"] for doc in policies}, {
            "travel", "access", "incident", "acquisition", "prompt-test",
        })
        for doc in policies:
            self.assertTrue(doc["title"])
            self.assertTrue(doc["owner"])
            self.assertIsInstance(doc["allowed_groups"], list)
            self.assertTrue(doc["allowed_groups"])
            self.assertTrue(doc["text"].startswith("# "))

    def test_answer_uses_openai_responses_api(self):
        import json
        with patch("app.model.load_dotenv") as dotenv, patch.dict(
            "os.environ", {"OPENAI_API_KEY": "test-key", "OPENAI_MODEL": "gpt-4.1-mini"},
        ), patch("app.model.OpenAI") as client:
            api = client.return_value.__enter__.return_value
            api.responses.create.return_value = SimpleNamespace(output_text="The limit is $65 [travel].")
            sources = [doc for doc in documents() if doc["id"] == "travel"]
            answer = OpenAIModel().answer("What is the meal limit?", sources)
            self.assertEqual(answer, "The limit is $65 [travel].")
            dotenv.assert_called_once()
            self.assertEqual(dotenv.call_args.args[0].name, ".env")
            self.assertEqual(client.call_args.kwargs["api_key"], "test-key")
            payload = api.responses.create.call_args.kwargs
            self.assertEqual(payload["model"], "gpt-4.1-mini")
            self.assertFalse(payload["store"])
            self.assertEqual(json.loads(payload["input"]), {
                "question": "What is the meal limit?", "documents": sources,
            })

    def test_missing_key_reports_setup_error(self):
        with patch("app.model.load_dotenv"), patch.dict("os.environ", {}, clear=True), patch("app.model.OpenAI") as client:
            with self.assertRaisesRegex(ValueError, "OPENAI_API_KEY"):
                OpenAIModel().answer("meal limit", documents())
            client.assert_not_called()
    def test_change_request_shape(self):
        result = request_change("alice", "travel", "owner", "Finance")
        self.assertEqual(result["status"], "accepted")

if __name__ == "__main__": unittest.main()
