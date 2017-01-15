import telepot, time, os
from telepot.delegate import per_chat_id, create_open, pave_event_space
from message_consumer.message_consumer import MessageConsumer

TOKEN = os.getenv('TELEGRAM_API_TOKEN', '')

bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageConsumer, timeout=60
    ),
])

bot.message_loop(run_forever='Listening ...')
