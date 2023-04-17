Projeto de mensageiria em _Python_ aplicando os **princípios do SOLID:**

```python
# Módulo principal

from abc import ABC, abstractmethod

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

from typing import Union

def send_notification(messenger: Messenger, recipient: Union[str, int], message: str) -> None:
    if isinstance(recipient, str):
        messenger.send_message(f"Enviando mensagem para email {recipient}: {message}")
    elif isinstance(recipient, int):
        messenger.send_message(f"Enviando mensagem para número {recipient}: {message}")


# Teste

email_messenger = EmailMessenger("fulano@exemplo.com")
sms_messenger = SMSMessenger("+5511999999999")

send_notification(email_messenger, "ciclano@exemplo.com", "Olá, este é um email de teste!")
send_notification(sms_messenger, 11999999999, "Olá, esta é uma mensagem de texto de teste!")
```

Neste exemplo, utilizamos o Princípio da Responsabilidade Única (SRP):
- Criando uma classe abstrata `Messenger` que define um único método `send_message`;
- Em seguida, criamos duas classes concretas `EmailMessenger` e `SMSMessenger`, cada uma responsável por implementar a lógica para enviar mensagens por email e SMS, respectivamente.

Além disso, utilizamos o Princípio da Inversão de Dependência (DIP):
- Permitindo que o módulo principal dependa apenas da abstração `Messenger`, sem se preocupar com as classes concretas específicas.

Por fim, utilizamos o Polimorfismo para:
- Permitir que a função `send_notification` possa ser usada com qualquer objeto que implemente a interface `Messenger`, tornando o código mais flexível e extensível.
