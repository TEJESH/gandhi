import sys
import time
import os
import random
import datetime
import telepot
import telepot.namedtuple
import re
from sys import path
from configparser import ConfigParser
from telegram import ParseMode, Emoji
from telegram.ext import Updater, CommandHandler
path.append("src/")
from GitApi import GitHub
from telepot.delegate import per_inline_from_id, create_open, pave_event_space
from goodreads import client
from goodreads import group
from flask import Flask, request

try:
    from Queue import Queue
except ImportError:
    from queue import Queue

app = Flask(__name__)

TOKEN = '292106014:AAG9k-cwqLa4V6oZm_1BkfIQIHljnYuqFRY'
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
# add handlers


gc = client.GoodreadsClient('nTRaECtlyOjSmjJnLKRaiw', 'hCXp9GKlAe3sk1QIj0jXLF4UGLt9vfj54hDAfzHY')

SECRET = '/bot' + '292106014:AAG9k-cwqLa4V6oZm_1BkfIQIHljnYuqFRY'

# Bot Configuration
config = ConfigParser()
config.read_file(open('config.ini'))


# Connecting the telegram API
# Updater will take the information and dispatcher connect the message to
# the bot
up = Updater(token='292106014:AAG9k-cwqLa4V6oZm_1BkfIQIHljnYuqFRY')
dispatcher = up.dispatcher


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://read1.herokuapp.com/292106014:AAG9k-cwqLa4V6oZm_1BkfIQIHljnYuqFRY/HOOK')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
    
# Home function
def start(bot, update):
    # Home message
    msg = "Hello {user_name}! I'm {bot_name}. \n"
    msg += "What would you like to do? \n"
    msg += "/read + number - book name, and author \n"
    msg += "/current + number - book name, and author \n"
    msg += "/to_read + number - book name, and author \n"
    msg += "Ex: /listing HeavenH | /info HeavenH \n"
    msg += "Ex: /read python \n"
    msg += "Ex: /current \n"
    msg += "Ex: /to_read "

    # Send the message
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name,
                         bot_name=bot.name))


# Function to list the repositories
def listing(bot, update, args):
    gh = GitHub()
    for user in args:
        bot.send_message(chat_id=update.message.chat_id,
                         text='{0} Listing the user repositories '
                         .format('\U0001F5C4') +
                         '[{0}](https://github.com/{0}) {1}'.format(
                             user, Emoji.WHITE_DOWN_POINTING_BACKHAND_INDEX),
                         parse_mode=ParseMode.MARKDOWN)

        bot.send_message(chat_id=update.message.chat_id,
                         text=gh.get_repos(user))


# Function to display user information
def info(bot, update, args):
    gh = GitHub()
    for user in args:
        bot.send_message(chat_id=update.message.chat_id,
                         text='{2} User Information ' +
                         '[{0}](https://github.com/{0}) {1}'.format(
                             user, Emoji.WHITE_DOWN_POINTING_BACKHAND_INDEX,
                             Emoji.INFORMATION_SOURCE),
                         parse_mode=ParseMode.MARKDOWN)
        bot.send_message(chat_id=update.message.chat_id,
                         text=gh.get_info(user))

def read(bot, update, args):
    for user in args:
         #userr = re.sub(' ', '%27s+', str(user))
         #book = gc.book(user)
         bookn = gc.search_books_links(user)

         bookm = gc.search_books(user)
         
         bookr = re.sub(', u', '\n\n', str(bookn))
         bookm1 = re.sub(',', '\n', str(bookm))

         #REMOVE_LIST = ["[u", "]"]

         #remove = '|'.join(REMOVE_LIST)
         #regex = re.compile(r'('+remove+r')', flags=re.IGNORECASE)
         #out = regex.sub("", bookr)
         #print out
         #bookid = str(gc.book(user))
         #authors = book.authors
         #links = book.link
         #description = book.description
        #msg = random.randint(1,6)
        #bot.sendMessage(chat_id=update.message.chat_id, text=msg)
         #bot.sendMessage(chat_id=update.message.chat_id, text=str(book))
         bot.sendMessage(chat_id=update.message.chat_id, text=bookm1)
         bot.sendMessage(chat_id=update.message.chat_id, text=bookr)
        # bot.sendMessage(chat_id=update.message.chat_id, text=str(bookn['authors']))
         #bot.sendMessage(chat_id=update.message.chat_id, text=str(authors))
         #bot.sendMessage(chat_id=update.message.chat_id, text=str(links))
         #bot.sendMessage(chat_id=update.message.chat_id, text=str(description))
def current(bot, update):
    
        msg = str(datetime.datetime.now())
        bot.sendMessage(chat_id=update.message.chat_id, text=msg)
        
def to_read(bot, update):
    
        
        msg = str("Hello person, welcome back")
        bot.sendMessage(chat_id=update.message.chat_id, text=msg)  
      

# Add handlers to dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('listing', listing, pass_args=True))
dispatcher.add_handler(CommandHandler('info', info, pass_args=True))
dispatcher.add_handler(CommandHandler('read', read, pass_args=True))
dispatcher.add_handler(CommandHandler('current', current, pass_args=False))
dispatcher.add_handler(CommandHandler('to_read', to_read, pass_args=False))




'''@app.route(SECRET, methods=['GET', 'POST'])
def pass_update():
    UPDATE_QUEUE.put(request.data)  # pass update to bot
    return 'OK'  '''


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    '''port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://read1.herokuapp.com/" + TOKEN)
updater.idle()'''

updater.start_webhook(listen='127.0.0.1', port=5000, url_path='292106014:AAG9k-cwqLa4V6oZm_1BkfIQIHljnYuqFRY')
updater.bot.setWebhook(webhook_url='https://read1.herokuapp.com/292106014:AAG9k-cwqLa4V6oZm_1BkfIQIHljnYuqFRY',
                       certificate=open('cert.pem.read1', 'rb'))

up.start_polling(bootstrap_retries=5)
up.idle() 



'''class InlineHandler(telepot.helper.InlineUserHandler, telepot.helper.AnswererMixin):

    def __init__(self, *args, **kwargs):
        super(InlineHandler, self).__init__(*args, **kwargs)
        # Home message
        
    


    def on_inline_query(self, msg):
        def compute_answer():
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)

            print query_string
            bookn = gc.search_books(query_string)
            
            bookr = re.sub(', u', '\n\n', str(bookn))
            print bookr
            articles = [{'type': 'article',
                             'id': 'abc', 'title': query_string, 'message_text': bookr}]

            return articles

        self.answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        from pprint import pprint
        pprint(msg)
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print(self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)




bot1 = telepot.DelegatorBot('292106014:AAEdLmqqhYHhDncqidNtFSNx9Mj7Fil50_8', [
    pave_event_space()(
        per_inline_from_id(), create_open, InlineHandler, timeout=200),
])

bot1.message_loop(run_forever='Listening ...')'''



# Start the program

# Developed by Heaven, Jr750ac, Pedro Souza, Israel Sant'Anna all rights
# reserved



'''def handle(msg):
 content_type, chat_type, chat_id = telepot.glance(msg)
 m = telepot.namedtuple.Message(**msg)

 if msg['text'] == '/current' or msg['text'] == '/read' or msg['text'] == '/to_read' or msg['text'] == '/start':
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/read':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/start':
        bot.sendMessage(chat_id, str("/read\n/current\n/to_read "))
       
    if command == '/to_read':
        #person = input('Name')
        bot.sendMessage(chat_id, str("Hello person, welcome back"))           
    elif command == '/current':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))



       

 else:
    

    if chat_id < 0:
        # group message
        print 'Received %s\n a %s from %s, by %s' % (msg['text'],content_type, m.chat, m.from_)
    else:
        # private message
        print 'Received %s\n a %s from %s' % (msg['text'], content_type, m.chat)  # m.chat == m.from_

    if content_type == 'text':
        reply = ''

        # For long messages, only return the first 10 characters.
        if len(msg['text']) > 100:
            reply = 'First 100 characters:\n'

        # Length-checking and substring-extraction may work differently
        # depending on Python versions and platforms. See above.

        reply += msg['text']
        bot.sendMessage(chat_id, reply)

bot = telepot.Bot('292106014:AAFJj6NEwX50A8lt4bRl2HdZflnZsd1xogE')

bot.message_loop(handle)'''



'''class InlineHandler(telepot.helper.InlineUserHandler, telepot.helper.AnswererMixin):
    def __init__(self, *args, **kwargs):
        super(InlineHandler, self).__init__(*args, **kwargs)

    def on_inline_query(self, msg):
        def compute_answer():
            query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
            print(self.id, ':', 'Inline Query:', query_id, from_id, query_string)

            articles = [{'type': 'article',
                             'id': 'abc', 'title': query_string, 'message_text': query_string}]

            return articles

        self.answerer.answer(msg, compute_answer)

    def on_chosen_inline_result(self, msg):
        from pprint import pprint
        pprint(msg)
        result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
        print(self.id, ':', 'Chosen Inline Result:', result_id, from_id, query_string)


TOKEN = '292106014:AAE1Su97unVUdq85FMQ8IF7Y1Se4AGgPEzg'

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_inline_from_id(), create_open, InlineHandler, timeout=10),
])


bot.message_loop(run_forever='Listening ...')'''



'''print 'I am listening ...'

while 1:
    time.sleep(10)'''


