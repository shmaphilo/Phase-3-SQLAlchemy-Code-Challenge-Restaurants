from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Define the Restaurant, Customer, and Review classes
class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define relationships
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define relationships
    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Define relationships
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.first_name} {self.customer.last_name}: {self.star_rating} stars"

# Create tables in the database
Base.metadata.create_all(engine)

# Sample data
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)
customer1 = Customer(first_name='Philip', last_name='Ogaye')
customer2 = Customer(first_name='jane', last_name='Smith')
review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant1, customer=customer2)
review3 = Review(star_rating=3, restaurant=restaurant2, customer=customer1)

# Add data to the session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
session.commit()

# Test the methods
customer = session.query(Customer).first()
restaurant = session.query(Restaurant).first()

print("Customer's Reviews:")
for review in customer.reviews:
    print(f"Rating: {review.star_rating}, Restaurant: {review.restaurant.name}")

print("\nRestaurant's Reviews:")
for review in restaurant.reviews:
    print(f"Rating: {review.star_rating}, Customer: {review.customer.first_name} {review.customer.last_name}")

