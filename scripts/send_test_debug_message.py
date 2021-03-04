from messaging.models import Messaging

def run():
    messages = Messaging.objects.all()
    # messages.sendMessage( user = 1, text = 'test message', messageType= Messaging.MESSAGE_TYPE_DEBUG)