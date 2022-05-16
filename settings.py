class User(object):

    SRV_IP = '' # Server IP on database.
    SRV_PORT = '' # Port Server.
    DB_SERVICE = '' # Service Name on Server.
    DSN = SRV_IP + ':' + SRV_PORT + '/' + DB_SERVICE + ':' + SRV_PORT + '/' + DB_SERVICE 
    DB_USER = '' # You user on oracle database.
    DB_PASSWORD = '' # You password on oracle database.
