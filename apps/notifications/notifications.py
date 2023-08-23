from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


async def send_notification(user_id, message):
    await channel_layer.group_add(f'user_{user_id}', 'notification_group')
    await channel_layer.group_send(f'user_{user_id}', {
        'type': 'notification_message',
        'message': message
    })


async def notification_message(event):
    message = event['message']
