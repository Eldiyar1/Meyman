from .notifications import send_notification


def some_view(request):
    user_id = 2
    message = "Привет, это уведомление!"
    send_notification(user_id=user_id, message=message)