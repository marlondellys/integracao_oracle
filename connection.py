import logging
import cx_Oracle
import pandas as pd
from settings import User

dir = r'C:\Users\marlon.oliveira\Documents\instantclient_21_3'

logging.basicConfig(filename='logs.logs', filemode='a+', level=logging.DEBUG, format='%(asctime)s - %(message)s')
logging.debug('This will get logged')

cx_Oracle.init_oracle_client(lib_dir = dir)

class Connection(object):

    def __init__(self):
        connection = cx_Oracle.connect(
            user = User.DB_USER,
            password = User.DB_PASSWORD,
            dsn = User.DSN,
            encoding = "UTF-8"
        )
        self.cursor = connection.cursor()
        logging.debug('Conexão realizada com sucesso...!')
    
    def read_sql(self, sql_query: str) -> pd.DataFrame:
        datas = self.cursor.execute(sql_query).fetchall()
        self.dataframe = pd.DataFrame(datas)
        logging.debug('Dados Selecionados com sucesso...!')


    def save_as(self, mode: str, path: str, name: str) -> bool:
        path = path + '\\' + name
        match mode:
            case 'json':
                self.dataframe.to_json(path)
                logging.debug('Relatório %s Salvo com sucesso...!' % path)
                return

            case 'excel':
                self.dataframe.to_excel(path, index=0)
                logging.debug('Relatório %s Salvo com sucesso...!' % path)
                return

            case 'csv':
                self.dataframe.to_csv(path, sep=';', index=0)
                logging.debug('Relatório %s Salvo com sucesso...!' % path)
                return

