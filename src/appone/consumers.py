from channels.consumer import AsyncConsumer

class MyConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        # Called when a new websocket connection is established
        print("connected", event)
        user = self.scope['user']
        self.update_user_status(user, 'online')

    async def websocket_receive(self, event):
        # Called when a message is received from the websocket
        # Method NOT used
        print("received", event)

    async def websocket_disconnect(self, event):
        # Called when a websocket is disconnected
        print("disconnected", event)
        user = self.scope['user']
        self.update_user_status(user, 'offline')
    
# @database_sync_to_async
# def update_user_incr(self, user):
#     UserProfile.objects.filter(pk=user.pk).update(online=F('online') + 1)

# @database_sync_to_async
# def update_user_decr(self, user):
#     UserProfile.objects.filter(pk=user.pk).update(online=F('online') - 1)