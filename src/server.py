from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver


# telnet 127.0.0.1 1234
class ServerProtocol(LineOnlyReceiver):
    factory: 'Server'
    login: str = None

    def connectionMade(self):
        self.factory.clients.append(self)

    def connectionLost(self, reason=connectionDone):
        self.factory.clients.remove(self)

    def lineReceived(self, line: bytes):
        content = line.decode()

        if self.login is not None:
            content = f"Message form {self.login}: {content}".encode()
            
            self.factory.m_history.append(content) # Сохранение истории сообщений 
            # История сообщений не должна превышать 10 сообщений
            if len(self.factory.m_history) > 10:
                self.factory.m_history.pop(0)

            for user in self.factory.clients:
                if user is not self:
                    user.sendLine(content)
        else:
                # login:admin -> admin
                if content.startswith("login:"):
                    login = content.replace("login:", "")
                    # Проверка на повторение имён пользователей:
                    flag = False # Flag - переменная булевого типа для дальнейшей проверки Повторяющихся имён
                    for client in self.factory.clients:
                        if client.login == login:
                           self.sendLine("This login already used!".encode())
                           flag = True
                           break
                        if not flag:
                            self.login = login
                            self.sendLine("Welcome!".encode())
                            self.factory.send_m_history(self) # Отправка истории сообщений новому пользователю
                else:
                    self.sendLine("Invalid login".encode())

class Server(ServerFactory):
    protocol = ServerProtocol
    clients: list
    m_history = [] # История сообщений message_history

    def startFactory(self):
        self.clients = []
        print("Server started")

    def stopFactory(self):
        print("Server closed")

    def send_m_history(self, protocol):
        for content in self.m_history:
            protocol.sendLine(content)


reactor.listenTCP(1234, Server())
reactor.run()