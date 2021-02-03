def sendMessages(messageList):
    for message in messageList:
        print(message)
        
        sentMessages.append(message)
    
    return sentMessages, messageList

messages = ['hello', 'hi', 'whats up', 'i like potatoes', 'yes', 'no']
sentMessages = []    
    
sentMessages, messages = sendMessages(messages)


print(messages)
print(sentMessages)
