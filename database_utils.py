import sqlite3
#Create table
def loadConnection(path):
    filename=path+'\\'+'extentions.db'
    connection=sqlite3.connect(filename)
    cursor=connection.cursor()
    return(connection,cursor)
def create_tables(path):
    connection,cursor=loadConnection(path)
    query='create table if not exists extentions_processed (extention text);'
    cursor.execute(query)
def saveExtentions(extentions,path):
    connection,cursor=loadConnection(path)
    cursor.executemany('insert into extentions_processed (extention) values(?)',[(x,) for x in extentions])
    connection.commit()
def fetchExtentions(path):
    connection,cursor=loadConnection(path)
    extentions_processed=list(cursor.fetchall())
    clearExtentions(cursor,connection)
    return extentions_processed
def clearExtentions(cursor,connection):
    cursor.execute('delete from extentions_processed')
    connection.commit()
