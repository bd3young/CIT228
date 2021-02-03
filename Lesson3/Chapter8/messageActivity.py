#import messages
from messages import sendMessages
#from messages import sendMessages as sm
#import messages as mess
#from messages import *

messages = ['Howdy', 'My Name is Beau', 'My cats name is Buttercup', 'Fun Stuff']
sentMessages = []

sentMessages, messages = sendMessages(messages)

print(sentMessages)
print(messages)