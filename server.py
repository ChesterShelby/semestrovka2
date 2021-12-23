import socket
from threading import Thread

BUFFER = 1024


class Client:
    def __init__(self):
        self.__address = None
        self.__connection = None
        self.__name = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x):
        self.__name = x

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, x):
        self.__address = x

    @property
    def connection(self):
        """
        Returns:
            socket.socket: connection
        """
        return self.__connection

    @connection.setter
    def connection(self, x):
        self.__connection = x


class Server:
    def __init__(self, ip, port):
        self.clients = set()
        self.sock = socket.socket()
        self.sock.bind((ip, port))

        self.listen()

    def listen(self):
        print('Start')
        self.sock.listen(2)
        while True:
            connection, address = self.sock.accept()

            client = Client()
            client.address = address
            client.connection = connection

            self.clients.add(client)

            print(f'Connected {address}')
            Thread(target=self.client_loop, args=(client,)).start()

    def recv_and_share(self, client, new_client=False):
        try:
            if response := client.connection.recv(BUFFER):
                response = response.decode('UTF-8')
                if new_client:
                    client.name = response
                    print(f'new client {client.address} with name: {response}')
                    self.send_all(client, 'Привет всем, я новенький!')
                else:
                    print(f'from client {client.address} recieved: {response}')
                    self.send_all(client, response)
            else:
                raise Exception('Client disconnected')
        except Exception:
            self.close_client(client)
            return False
        else:
            return True

    def client_loop(self, client):
        """

        Args:
            client (Client):

        Returns:

        """
        self.recv_and_share(client, new_client=True)
        while self.recv_and_share(client):
            pass

    def send_all(self, from_client, text):
        for client in self.clients:
            if client != from_client:
                client.connection.send(f"[{from_client.name}]: {text}".encode('UTF-8'))

    def close_client(self, client):
        self.clients.remove(client)
        client.connection.close()


server = Server('localhost', 8081)
