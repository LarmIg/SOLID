from abc import ABC, abstractmethod
from typing import Union

class Messenger(ABC):
    @abstractmethod
    def send_message(self, message: str) -> bool:
        pass

class EmailMessenger(Messenger):
    def __init__(self, email_address: str):
        self.email_address = email_address
        
    def send_message(self, message: str) -> bool:
        # Implementação para envio de email aqui
        pass

class SMSMessenger(Messenger):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        
    def send_message(self, message: str) -> bool:
        # Implementação para envio de SMS aqui
        pass


# Exemplo de uso
def send_notification(messenger: Messenger, recipient: Union[str, int], message: str) -> None:
    if isinstance(recipient, str):
        messenger.send_message(f"Enviando mensagem para email {recipient}: {message}")
    elif isinstance(recipient, int):
        messenger.send_message(f"Enviando mensagem para número {recipient}: {message}")


# Teste

email_messenger = EmailMessenger("fulano@exemplo.com")
sms_messenger = SMSMessenger("+551191234678")

send_notification(email_messenger, "ciclano@exemplo.com", "Olá, este é um email de teste!")
send_notification(sms_messenger, 1191234678, "Olá, esta é uma mensagem de texto de teste!")
