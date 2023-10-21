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