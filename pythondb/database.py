from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    cities = relationship("City", back_populates="country")

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship("Country", back_populates="cities")
    hotels = relationship("Hotel", back_populates="city")

class Hotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    address = Column(String(255))
    phone = Column(String(20))
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("City", back_populates="hotels")
    tours = relationship("Tour", back_populates="hotel")

class Tour(Base):
    __tablename__ = 'tours'
    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    hotel = relationship("Hotel", back_populates="tours")
    tourists = relationship("Tourist", secondary='tour_tourists', back_populates="tours")

class Tourist(Base):
    __tablename__ = 'tourists'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    tours = relationship("Tour", secondary='tour_tourists', back_populates="tourists")

class TourTourist(Base):
    __tablename__ = 'tour_tourists'
    tour_id = Column(Integer, ForeignKey('tours.id'), primary_key=True)
    tourist_id = Column(Integer, ForeignKey('tourists.id'), primary_key=True)

# Инициализация БД
engine = create_engine('sqlite:///tourism.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()