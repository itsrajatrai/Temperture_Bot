import telegram

Token = "5921585208:AAHrDdBlDv_S7Q-aRwv9UMYz1cxubqU4OO8"
updater = telegram.updater("5921585208:AAHrDdBlDv_S7Q-aRwv9UMYz1cxubqU4OO8", use_context=True)
dispatcher = updater.dispatcher

def get_temperature():
    # code to get temperature from an API or website
    return temperature

def send_temperature(bot, job):
    temperature = get_temperature()
    subscribers = get_subscribers() #function to get list of subscribers
    for subscriber in subscribers:
        bot.send_message(chat_id=subscriber, text="Temperature in Delhi is: " + temperature)

job_queue = updater.job_queue
job_queue.run_repeating(send_temperature, interval=3600, first=0)
updater.start_polling()

def subscribe(bot, update):
    subscriber = update.message.chat_id
    add_subscriber(subscriber) # function to add subscriber
    update.message.reply_text("You are now subscribed to temperature updates!")

subscribe_handler = telegram.ext.CommandHandler("subscribe", subscribe)
dispatcher.add_handler(subscribe_handler)

updater.start_polling()
updater.idle()