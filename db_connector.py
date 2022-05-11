from couchdb import Server

authtoken = ''
server = None

def login():
    global server, authtoken
    server = Server()
    authtoken = server.login('admin', 'xxxx')

def logout():
    global authtoken
    server.logout(authtoken)



