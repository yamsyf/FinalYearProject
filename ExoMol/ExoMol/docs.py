from re import M
from mongoengine import connect
import mongoengine
from mongoengine.document import Document

connect('test')

class Doc4(mongoengine.Document):
    meta = {'collection':'doc4'}
    M=mongoengine.IntField(default=0)
    I = mongoengine.IntField(default=0)
    v = mongoengine.FloatField(default = 0)
    S = mongoengine.FloatField(default = 0)
    A = mongoengine.FloatField(default = 0)
    E_f = mongoengine.FloatField(default = 0)
    V_i = mongoengine.StringField(max_length=16)
    V_f = mongoengine.StringField(max_length=16)
    Q_i = mongoengine.StringField(max_length=16)
    Q_f =mongoengine.StringField(max_length=16)
    Ierr = mongoengine.FloatField(default = 0)
    g_i = mongoengine.IntField(default=0)
    g_f = mongoengine.IntField(default=0)
    q = mongoengine.IntField(default=0)
    
    
    
    