from connection import Connection

if __name__ == '__main__':
    flow = Connection()
    flow.read_sql('SELECT * FROM NF_SUP WHERE ROWNUM <= 100')
    flow.save_as('excel', '.', 'notas.xlsx')
