from configparser import SafeConfigParser
import os

config = SafeConfigParser()
config.read('config.ini')

ENV = config.get('rapid', 'env')

if ENV in ["localdb", "localqa", "localstage", "localprod", "docker", "database"]:
    
    DBTYPE = config.get(ENV, 'DBTYPE')
    DBDRIVER = config.get(ENV, 'DBDRIVER')
    DBHOST = config.get(ENV, 'DBHOST')
    DBNAME = config.get(ENV, 'DBNAME')
    DBUSER = config.get(ENV, 'DBUSER')
    DBPASS = config.get(ENV, 'DBPASS')
    DBSTRING = config.get(ENV, 'DBSTRING').replace('->', '=').replace(',,', ';')

if ENV in ["QA", "STAGE", "PROD"]:
    
    DBTYPE = os.environ['DBTYPE']
    DBDRIVER = os.environ['DBDRIVER']
    DBHOST =  os.environ['DBHOST']
    DBNAME = os.environ['DBNAME']
    DBUSER = os.environ['DBUSER']
    DBPASS = os.environ['DBPASS']
    DBSTRING = os.environ['DBSTRING'].replace('->', '=').replace(',,', ';')
    DEBUG = 'False'

connection_string = DBSTRING.format(DBHOST, DBNAME, DBUSER, DBPASS, DBTYPE, DBDRIVER)

print(connection_string)