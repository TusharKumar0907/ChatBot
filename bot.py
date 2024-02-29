from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from docs import clean_corpus

CORPUS_FILE = "./data"

chatbot = ChatBot("Chatpot")
trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)


def get_responses_until_word(temp, user_input):
    word = user_input
    next = "next"
    while True:
        response = chatbot.get_response(word)
        word = response.text
        if temp in response.text:  
            break
        if next in response.text:
            print("")
        else:
            print(response)


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("")
    if query in exit_conditions:
        break
    else:
        get_responses_until_word("STOP", query.lower())
