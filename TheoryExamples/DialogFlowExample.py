import os
import dialogflow_v2 as dialogflow
import google.api_core.exceptions
import json
import wave
from google.oauth2 import service_account
import pyttsx3

class Chatbot:

    def __init__(self, project_id, credentials_file):
        self.project_id = project_id
        self.credentials_file = credentials_file
        self.session_client = self._create_session_client()

    def _create_session_client(self):
        creds = service_account.Credentials.from_service_account_file(self.credentials_file)
        return dialogflow.SessionsClient(credentials=creds)

    def detect_intent(self, text, session_id):
        session = self.session_client.session_path(self.project_id, session_id)
        text_input = dialogflow.TextInput(text=text, language_code="en-US")
        query_input = dialogflow.QueryInput(text=text_input)

        try:
            response = self.session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )
            return response.query_result.fulfillment_text
        except google.api_core.exceptions.InvalidArgument:
            return "Sorry, I didn't understand that."

    def text_to_speech(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def handle_user_query(self, user_query):
        response = self.detect_intent(user_query, "unique_session_id")
        self.text_to_speech(response)
        return response

if __name__ == "__main__":
    # Replace with your own Dialogflow Project ID and credentials file
    project_id = "your_project_id"
    credentials_file = "path/to/your/credentials.json"

    chatbot = Chatbot(project_id, credentials_file)

    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            break

        response = chatbot.handle_user_query(user_query)
        print(f"Bot: {response}")