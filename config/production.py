from config.default import *

# 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{passwd}@{host}/{db}'.format(BASE_DIR,
    user = 'root',
    passwd = '1234',
    host = '127.0.0.1',
    db = 'aicms',
)
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy의 이벤트를 처리하는 옵션
SECRET_KEY = b'Zb3\x81\xdb\xf1\xd9\xd7-Knb\x8eB\xa5\x18'