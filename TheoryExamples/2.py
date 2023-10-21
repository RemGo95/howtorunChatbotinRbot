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