from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

chatbot = ChatBot(
    "Jarvis",
    logic_adapters=[{
        'import_path': 'chatterbot.logic.BestMatch'
    },
    {
        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
        'threshold': 2,
        'default_response': 'I am sorry, but i do not understand'
        },
        {
        'import_path': 'chatterbot.logic.SpecificResponseAdapter',
        'input_text': 'Help me!',
        'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
        }],
    storage_adapter='chatterbot.storage.SQLStorageAdapter')

chatbot.set_trainer(ListTrainer)

# Pre Trainer
'''
chatbot.train(
    "chatterbot.corpus.english"
)
'''

# Self Trainer
'''
chatbot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])
'''

# Open Multiple files for training
'''
for files in os.listdir('C://Users//new owner//Desktop//Machine Learning//chatterbot-corpus-master//chatterbot_corpus//data//english'):
    data = open('C://Users//new owner//Desktop//Machine Learning//chatterbot-corpus-master//chatterbot_corpus//data//english//' + files, 'r').readlines()
    chatbot.train(data)
'''

# Open single file for training
data2 = open('C://Users//new owner//Desktop//Machine Learning//chatterbot-corpus-master//chatterbot_corpus//data//english//ai.yml', 'r').readlines()
chatbot.train(data2)

# Main loop
while True:
    try:
        message = input("You: ")
        if message != 'bye':
            reply = chatbot.get_response(message)
            print(reply)
        elif message == 'bye':
            print('Bye')
            break
    except(KeyboardInterrupt, EOFError, SystemExit):
        break