from blinker import Namespace


INCOMING_MESSAGE_SIGNAL = 'incoming-message'
PROCESSED_MESSAGE_SIGNAL = 'processed-message'

bot_signals = Namespace()
incoming_message_signal = bot_signals.signal(INCOMING_MESSAGE_SIGNAL)
processed_message_signal = bot_signals.signal(PROCESSED_MESSAGE_SIGNAL)
