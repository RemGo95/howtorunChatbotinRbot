# howtorunChatbotinRbot
Learn how to run chat bot in mobile robot

First of all we have to remmember that project mosty depends on hardware background of robot and in the final parts of work will be edited. 

In this repo I want to try using simple chatbot in mobile robot with Raberry Pi. 

Below I have writed list that shows how to walkthrough of that project. If you have more expirience in projects like that you can skip first 10 steps.

1. First I want to remind to myself and show to show you simple neural network for a chatbot in Python, it can be accomplished using libraries like TensorFlow. Below is code with chatbot, neural network will use TensorFlow. This network will be a sequence-to-sequence model that takes input text and generates responses. As you can see code is very very simplified, it's just for demonstretion. Additionally, you'd need to integrate the chatbot with a text processing pipeline, handle user interactions, and improve the response generation logic.

2. Expanding chatbot training data is the most important thing that you can to improve performance and flexiblity of your bot. Of course we can you use already trained models, trained on big data but I think its good to know how to make it on your owm, even if its weaker.

Below you can find code that combines words, easiest way to make more train data for our simple chatbot. 

Topic will be obviously connected with life of our diy robot :)


3. Third code will be connected with adding text-to-speech engine (TTS). Below is example of imported and used gTTS.

And integration with chatbot in 3integration.py file.

4. Next step will be naturally connected with implementing micro and voice recognition. There is sample class that show how to achive that.

5. Finally - we can do something more practice. This code will demonstrate how to connect previous classes in program for mobile robot. It's still example so our bot will interact with only few commands (at this step we dont have connected actuators or any software for them).

This main loop combines all the previously discussed classes and demonstrates how to set microphone settings for better voice recognition, control the robot based on voice commands, and make the chatbot speak its responses. Adjust the settings and parameters as needed for your specific setup and requirements.

Before running this code, ensure that you have the necessary hardware (microphone and speaker) connected to your Raspberry Pi and have configured your audio settings correctly.

6. Chatbot connected with internet. This chatbot uses the Dialogflow API for natural language understanding and generation. You'll need to install the `dialogflow` Python package and set up a Dialogflow agent to use this class. You can install it by copy command below: 
- pip install dialogflow google-auth wave pyttsx3











