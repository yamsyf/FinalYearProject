from re import M
from mongoengine import connect
import mongoengine
from mongoengine.document import Document

connect('test')
 
class Doc(mongoengine.Document):
    pid = mongoengine.IntField(default=0)
    
    qid = mongoengine.IntField(default=0)
    passage = mongoengine.StringField(max_length=16)
    new = mongoengine.IntField(default=0)
    relevancy = mongoengine.IntField(default=0)
    queries = mongoengine.StringField(max_length=16)
    s  = mongoengine.IntField(default=0)

class Doc2(mongoengine.Document):
    M_of_C2__12C2__8states=mongoengine.IntField(default=0)
    I = mongoengine.IntField(default=0)
    v =mongoengine.FloatField(default = 0)
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

class Doc3(mongoengine.Document):
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

class Doc4(mongoengine.Document):
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
    
    
    