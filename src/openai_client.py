import logging
from openai import OpenAI
import time


class OpenAIClient:
    def __init__(self, assistant_id, api_key):
        self.client = OpenAI(api_key=api_key)
        self.assistant_id = assistant_id

    def submit_message(self, thread, user_message):
        try:
            self.client.beta.threads.messages.create(
                thread_id=thread.id, role="user", content=user_message
            )
            return self.client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=self.assistant_id,
            )
        except Exception as e:
            logging.error(f"Error in submit_message: {e}")
            raise

    def get_response(self, thread):
        try:
            return self.client.beta.threads.messages.list(
                thread_id=thread.id, order="asc"
            )
        except Exception as e:
            logging.error(f"Error in get_response: {e}")
            raise

    def create_thread_and_run(self, user_input):
        try:
            thread = self.client.beta.threads.create()
            run = self.submit_message(thread, user_input)
            return thread, run
        except Exception as e:
            logging.error(f"Error in create_thread_and_run: {e}")
            raise

    def wait_on_run(self, run, thread):
        try:
            while run.status == "queued" or run.status == "in_progress":
                run = self.client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id,
                )
                time.sleep(0.5)
            return run
        except Exception as e:
            logging.error(f"Error in wait_on_run: {e}")
            raise
