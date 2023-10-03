import sqlalchemy.orm
from sqlalchemy import create_engine, dialects
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base


# создаём движок для подключения по ссылке
engine = create_engine('postgresql://rakjuhbb:e4hcZp5xW9H8HpJsNmCg2fZwnWRoG6TN@tai.db.elephantsql.com/rakjuhbb')
# создаём сессию, которая позволит нам отправлять запросы в БД
db_session = scoped_session(sessionmaker(bind=engine))

# все модели будут наследоваться от Base и иметь возможность взаимодействовать с sqlalchemy
Base = sqlalchemy.orm.declarative_base()
# сделали так, чтобы можно было делать запросы из модели, используя не db_session, а из самой модели
Base.query = db_session.query_property()