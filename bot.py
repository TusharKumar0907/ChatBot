from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from docs import clean_corpus
from tabula.io import read_pdf
CORPUS_FILE = "./data"
PDFPATH = './brochure.pdf'

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
        if query.lower() == "important contacts of university":
            dfs = read_pdf(PDFPATH, pages='10', encoding='cp1252')
            print(dfs[0])
        if query.lower() == "hostel charges":
            dfs = read_pdf(PDFPATH, pages='29', encoding='cp1252')
            print(dfs[0])
        if query.lower() == "documents required for admission":
            dfs = read_pdf(PDFPATH, pages='36', encoding='cp1252')
            print(dfs[0])
        if query.lower() == "minor degree":
            dfs = read_pdf(PDFPATH, pages='57', encoding='cp1252')
            print(dfs[0])        
        else:
            get_responses_until_word("STOP", query.lower())
