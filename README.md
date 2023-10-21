# howtorunChatbotinRbot
Learn how to run chat bot in mobile robot

First of all we have to remmember that project mosty depends on hardware background of robot and in the final parts of work will be edited. 

In this repo I want to try using simple chatbot in mobile robot with Raberry Pi. 

Below I have writed list that shows how to walkthrough of that project. If you have more expirience in projects like that you can skip first 10 steps.


1. First I want to remind to myself and show to show you simple neural network for a chatbot in Python, it can be accomplished using libraries like TensorFlow. Below is code with chatbot, neural network will use TensorFlow. This network will be a sequence-to-sequence model that takes input text and generates responses. As you can see code is very very simplified, it's just for demonstretion. Additionally, you'd need to integrate the chatbot with a text processing pipeline, handle user interactions, and improve the response generation logic.

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential

# Define a simple vocabulary for illustration purposes
vocab = ['hello', 'how', 'are', 'you', 'good', 'bye']

# Create a dictionary to map words to integers and vice versa
word2int = {word: i for i, word in enumerate(vocab)}
int2word = {i: word for i, word in enumerate(vocab)}

# Sample input-output pairs for training
data = [("hello how are you", "good"),
        ("how are you", "good"),
        ("hello", "goodbye")]

# Convert the input and output sentences to integer sequences
X = [[word2int[word] for word in sentence.split()] for sentence, _ in data]
Y = [[word2int[word] for word in sentence.split()] for _, sentence in data]

# Pad sequences to a fixed length
X = tf.keras.preprocessing.sequence.pad_sequences(X)
Y = tf.keras.preprocessing.sequence.pad_sequences(Y)

# Build the chatbot model
model = Sequential()
model.add(Embedding(len(vocab), 128))
model.add(LSTM(128))
model.add(Dense(len(vocab), activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model (you will need more data for a real chatbot)
model.fit(X, Y, epochs=1000)

# Generate responses using the trained model
input_sentence = "hello how are"
input_sequence = [word2int[word] for word in input_sentence.split()]
predicted_sequence = model.predict_classes(tf.keras.preprocessing.sequence.pad_sequences([input_sequence]))
output_sentence = ' '.join([int2word[i] for i in predicted_sequence])
print("Chatbot Response:", output_sentence)

2. Expanding chatbot training data is the most important thing that you can to improve performance and flexiblity of your bot. Of course we can you use already trained models, trained on big data but I think its good to know how to make it on your owm, even if its weaker.

Below you can find code that combines words, easiest way to make more train data for our simple chatbot. 

Topic will be obviously connected with life of our diy robot :)

import random

# Topics and keywords for generating sentences
topics = ["power", "program", "log","mobile robots", "motors", "batteries", "sensors", "navigation", "AI", "obstacle avoidance", "autonomous"]

verbs = ["move", "navigate", "power", "charge","stop", "start", "on", "off", "detect", "avoid", "control", "analyze", "communicate", "explore", "ride", "come", "get", "set", "calculate"]

nouns = ["robot", "motor", "battery", "sensor", "environment", "obstacle", "path", "data", "algorithm", "technology"]

adjectives = ["autonomous", "efficient", "smart", "wireless", "rechargeable", "sophisticated", "adaptive", "precise", "advanced", "mobile"]

# Generate sentences
num_sentences = 1000  # Adjust the number of sentences as needed
generated_sentences = []

for _ in range(num_sentences):
    sentence = f"A {random.choice(adjectives)} {random.choice(nouns)} can {random.choice(verbs)} in {random.choice(topics)}."
    generated_sentences.append(sentence)

# Save the generated sentences to a file
with open('robot_sentences.txt', 'w') as file:
    file.write('\n'.join(generated_sentences))

3. Third code will be connected with adding text-to-speech engine (TTS). Below is example of imported and used gTTS.

from gtts import gTTS
from io import BytesIO
import pygame

class TextToSpeech:
    def __init__(self):
        pygame.mixer.init()

    def speak(self, text):
        tts = gTTS(text)
        fp = BytesIO()
        tts.save(fp)
        fp.seek(0)
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

And integration with chatbot:

from voice_robot import VoiceControlledRobot
from chatbot import initialize_chatbot_model, generate_chatbot_response
from text_to_speech import TextToSpeech  # Import the TextToSpeech class

if __name__ == "__main__":
    # Initialize the chatbot model
    model = initialize_chatbot_model()

    # Create instances of the VoiceControlledRobot and TextToSpeech classes
    robot = VoiceControlledRobot()
    tts = TextToSpeech()

    try:
        while True:
            # Listen for voice commands and control the robot
            robot.listen_for_commands()

            # Accept user text input and generate chatbot responses
            user_input = input("User: ")
            chatbot_response = generate_chatbot_response(model, user_input)
            print("Chatbot: " + chatbot_response)

            # Make the chatbot speak its response
            tts.speak(chatbot_response)

    except KeyboardInterrupt:
        robot.cleanup()  # Clean up the robot's GPIO pins on exit

4. Next step will be naturally connected with implementing micro and voice recognition. There is sample class that show how to achive that:

import speech_recognition as sr

class MicrophoneSettings:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def set_microphone_settings(self, energy_threshold=4000, dynamic_energy_threshold=True):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            if dynamic_energy_threshold:
                self.recognizer.dynamic_energy_threshold = True
            else:
                self.recognizer.energy_threshold = energy_threshold

    def get_audio(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        return audio

5. Finally - we can do something more practice. This code will demonstrate how to connect previous classes in program for mobile robot. It's still example so our bot will interact with only few commands (at this step we dont have connected actuators or any software for them).

from voice_robot import VoiceControlledRobot
from chatbot import initialize_chatbot_model, generate_chatbot_response
from text_to_speech import TextToSpeech
from microphone_settings import MicrophoneSettings

if __name__ == "__main__":
    # Initialize the chatbot model
    model = initialize_chatbot_model()

    # Create instances of the VoiceControlledRobot, TextToSpeech, and MicrophoneSettings classes
    robot = VoiceControlledRobot()
    tts = TextToSpeech()
    microphone_settings = MicrophoneSettings()

    try:
        while True:
            # Set microphone settings for better voice recognition
            microphone_settings.set_microphone_settings(energy_threshold=4000, dynamic_energy_threshold=True)

            # Listen for voice commands
            print("Listening for voice commands...")
            audio = microphone_settings.get_audio()

            try:
                command = microphone_settings.recognizer.recognize_google(audio).lower()
                print("You said: " + command)

                # Control the robot based on voice commands
                if "forward" in command:
                    robot.move_robot("forward")
                elif "backward" in command:
                    robot.move_robot("backward")
                elif "left" in command:
                    robot.move_robot("left")
                elif "right" in command:
                    robot.move_robot("right")
                elif "stop" in command:
                    robot.move_robot("stop")
                else:
                    print("Command not recognized")

                # Generate chatbot responses
                user_input = command  # Use the recognized voice command as user input
                chatbot_response = generate_chatbot_response(model, user_input)
                print("Chatbot: " + chatbot_response)

                # Make the chatbot speak its response
                tts.speak(chatbot_response)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition; {e}")

    except KeyboardInterrupt:
        robot.cleanup()  # Clean up the robot's GPIO pins on exit


This main loop combines all the previously discussed classes and demonstrates how to set microphone settings for better voice recognition, control the robot based on voice commands, and make the chatbot speak its responses. Adjust the settings and parameters as needed for your specific setup and requirements.

Before running this code, ensure that you have the necessary hardware (microphone and speaker) connected to your Raspberry Pi and have configured your audio settings correctly.

6. Chatbot connected with internet. This chatbot uses the Dialogflow API for natural language understanding and generation. You'll need to install the `dialogflow` Python package and set up a Dialogflow agent to use this class. You can install it by copy command below: 
- pip install dialogflow google-auth wave pyttsx3

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











