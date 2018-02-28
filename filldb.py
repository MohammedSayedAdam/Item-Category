from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Catagory, Base, CatagoryItem, User
 
engine = create_engine('sqlite:///catagory.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()

User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


cat1 = Catagory(user_id=1, name = "Soccer")

session.add(cat1)
session.commit()

catItem1 = CatagoryItem(user_id=1, name = "Two shinguard",
                        description = "any thing =D",
                        catagory = cat1)

session.add(catItem1)
session.commit()


catItem2 = CatagoryItem(user_id=1, name = "Shinguard",
                        description = "any thing =D",
                        catagory = cat1)

session.add(catItem2)
session.commit()

catItem3 = CatagoryItem(user_id=1, name = "Jeisey",
                        description = "any thing =D",
                        catagory = cat1)

session.add(catItem3)
session.commit()


cat2 = Catagory(user_id=1, name = "Snow boarding")

session.add(cat2)
session.commit()


catItem1 = CatagoryItem(user_id=1, name = "Googles",
                        description = "With your choice",
                        catagory = cat2)

session.add(catItem1)
session.commit()

cat3 = Catagory(user_id=1, name = "Baseball")

session.add(cat3)
session.commit()


catItem1 = CatagoryItem(user_id=1, name = "Bat",
                        description = "batman is bla bla bla",
                        catagory = cat3)

session.add(catItem1)
session.commit()

cat4 = Catagory(user_id=1, name = "Hockey")

session.add(cat4)
session.commit()


catItem1 = CatagoryItem(user_id=1, name = "Stick",
                        description = " bla bla bla",
                        catagory = cat4)

session.add(catItem1)
session.commit()


print "added catagory items!"
