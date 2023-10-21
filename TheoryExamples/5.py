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