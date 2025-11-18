
import snowflake.snowpark as snowpark
from snowflake.core import Root


PRIVATE_KEY_STRING = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC4wUO0ZEXM4zW8
DnJkO/vQ5CGkyzzyIRo162zhWPzGMU6Ej57nA5Ytt/B+JJ3SR0n2Iu9fS3/A40Ok
VQvsUaRD/QfruZOV5gyqPTI6s+PH480Nd3/Qb8ChmdMlg2+RqKcFPtvmUTLUAd28
e54DGWBCuukhxD6NT51E6aXC6Bu2iDc1eTTT3Uya/GU+ypW9oLjR8LkJ5vxHjxgj
+nlv3ECzdL+wojFVKFzV0EmKdZB/WN8BgM6HP5HE4d68MDRw06TYsMjvKURruem0
QgpKpnIWlsCZVLGeGOAY5KImBNVddL44K2KumSkKnDn5EuLq6hzhQnP5fUWxIwCj
FpSZ/lE7AgMBAAECggEAFHTtwrURl3iW9A4jc17C6KPB5+XLB0JMDSlWonMAdg9y
krH2VbzrbX9+5PC3+tcC5PqER6hr6lcfn7v8+HsntZF4RY0EPuY8g8MH40EU2Qar
pzCSmektypbmLrKpcVbbu3R008Es4BWe0CZd3hj6tBjPBHqetHXaw40dWgHqQ6EM
GDy6uxlBLc2lgvloVHwEx8iH+FqHTMe8qWDiHbhOboeX6kvJivHSzY69gmVrsg8w
kCStRX6jzoTKzYJRHsbcPAykyUzgVfKw+JGjLxR6ghQm+P9XY87ioaVlwWBGVvC0
3iXScATL/0IJ0vLpiwLJ5ZDbaK9iMFr0E9S5Xee61QKBgQDwfvv6aUwm7P+t0H9n
h3IjrgPa16ojxcdywWsX9FURMu3KdFJ9rUHE98a25TQELXSIW4UrWCrX6Z5Ba3Yz
yK1YUOAE9xVu++aT6H+p8tqO8r+nMrcCc5caZuzw0auAtQvQuPG0MvtQUko822Wh
++sHQ1dzvwRD5LyGEv4qR+om1wKBgQDEqlwIM/3HOAV0XJqwIRu3fbvf4ESDcGdf
WkkfmIwsEXOFdXktdw/lV/WIO8Zwl24rCDnIrduv9ImvMOakqg4q+9DynAeR0E/W
Kn8XReeGaGqZBC1g4JabQPgDgGk3VWpB6AygrUffLI/4dadPOWM1bP69f0qIIaDw
HoFBtdNwPQKBgQDoWmds2kr+2L912Rkel1gJbNjAmNkC0tUN5B1p+WAuy7u+fIAu
eDQw7wsILY4B80DBdVrGM9rA3C9QGVkMUvhXeVvWsDn/DlUJ1flx4vaSYaoVCgSS
08bLdWG6kXhXU5PkxqqPZSo1wiuDfJ1G0TOTwtY9N/IQ/m++QZ9ajjyF5QKBgCFg
1Jvjzxenz20vZmWsSNr8sQ1PL/Gq+zB4z15YcrnsAFJPXNC1m3IOWrLTiluDqAQP
slb4Awg7Fb8xKoQaBKuQ76atiq9ZzqMHtWhKyf/K6wSra9Q8afNRtIZLng/xJEap
TrNalY8wLgM6XLoagFcJ97ZLy2eNZZY7Zy6y4H71AoGADVLLGi/b41YEluVMkE4J
NCyDrL45c9fHylAbCpM8I5tXXpm+mLkFQkR2RLjh1CiFM25cYWesAirxpM4dNA0V
z+QtexXe8xm8j2PDVwM8UGaGX2mUSIl27kIIdcO5q7wTnTNYp0ALKF4+TISOPWJZ
b2DsWclTzo1OBp4uNoKUs9Q=
-----END PRIVATE KEY-----"""

class User:
    def __get__(self,instance,owner):
        return instance._user
    
    def __set__(self,instance,value):
        instance._user = value

    def __delete__(self,instance):
        del instance._user

class Password:
    def __get__(self,instance,owner):
        return instance._password
    
    def __set__(self,instance,value):
        instance._password = value

    def __delete__(self,instance):
        del instance._password

class Account:
    def __get__(self,instance,owner):
        return instance._account
    
    def __set__(self,instance,value):
        instance._account = value

    def __delete__(self,instance):
        del instance._account

class Account:
    def __get__(self,instance,owner):
        return instance._account
    
    def __set__(self,instance,value):
        instance._account = value

    def __delete__(self,instance):
        del instance._account

class Session:
    def __get__(self,instance,owner):
        return instance._session
    
    def __set__(self,instance,value):
        instance._session = value

    def __delete__(self,instance):
        del instance._session

class SessionAttr:
    def __init__(self,parent):
        self.parent = parent

    user = User()
    password = Password()
    account = Account()
    session = Session()

class Session:
    def __init__(self):
        self.attr = SessionAttr(self)
    
    def set_user(self,value):
        self.attr.user = value
    
    def set_password(self,value):
        self.attr.password = value

    def set_account(self,value):
        self.attr.account = value

    def set_session(self,value):
        self.attr.session = value

    def set_passcode(self,value):
        self.passcode=value

    def get_session(self):
        self.set_user(self.attr.user)
        self.set_password(self.attr.password)
        self.set_account(self.attr.account)
        session = (snowpark.Session.builder.config("account",self.attr.account).config("user",self.attr.user).config("password",self.attr.password).create())
        self.set_session(session)
        return self.attr.session
    
    def get_root_object(self):
        root = Root(self.attr.session)
        return root