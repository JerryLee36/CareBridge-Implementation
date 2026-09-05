from app.models.platform import NotificationChannel, NotificationMessage, UserRole


class NotificationService:
    def __init__(self) -> None:
        self._messages: list[NotificationMessage] = []

    def send(self, person_id: str, recipient_role: UserRole, channel: NotificationChannel, title: str, body: str) -> NotificationMessage:
        message = NotificationMessage(
            message_id=f"msg-{len(self._messages) + 1}",
            person_id=person_id,
            recipient_role=recipient_role,
            channel=channel,
            title=title,
            body=body,
        )
        self._messages.append(message)
        return message

    def list_messages(self) -> list[NotificationMessage]:
        return self._messages
