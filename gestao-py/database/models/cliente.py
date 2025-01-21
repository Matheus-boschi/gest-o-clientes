from peewee import CharField, Model, DateTimeField
from database.database import db
import datetime

class Cliente(Model):
    nome = CharField()
    email = CharField()
    endereco = CharField()
    cpf =CharField()
    data_created  = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db