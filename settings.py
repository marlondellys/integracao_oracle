class User(object):

    SRV_IP = '192.168.0.8'
    SRV_PORT = '1521'
    DB_SERVICE = 'PRD'
    DSN = SRV_IP + ':' + SRV_PORT + '/' + DB_SERVICE + ':' + SRV_PORT + '/' + DB_SERVICE 
    DB_USER = '' # You user on oracle database.
    DB_PASSWORD = '' # You password on oracle database.