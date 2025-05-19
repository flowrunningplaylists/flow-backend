from database import engine, Base, Session
import crud

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine) # only creates the tables that are not already present

db = Session()

### fake test 1 - user create, read, update ###

# print("Creating user...")
# user = crud.create_user(db, email="alice@example.com", password_hash="123")
# print("Created:", user.id, user.name, user.email)

# print("Reading user...")
# fetched_user = crud.get_user_by_email(db, email="alice@example.com")
# print("Fetched:", fetched_user.id, fetched_user.name, fetched_user.email)

# print("updating user; SQLAlchemy should raise an exception because the name is too long...")
# try:
#     crud.update_user(
#         db, 
#         fetched_user.id, 
#         # name="Adeline")
#         name="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam massa ante, tempor eu risus in, tempus rutrum sem. In hac habitasse platea dictumst. Aenean pulvinar nisl sed efficitur semper. Mauris rutrum mi eros, nec lobortis mi mattis eget. Nullam pharetra augue a nisl sagittis faucibus. Vivamus placerat, est et pretium.")
# except Exception as e:
#     print("Error:", e)

### fake test 2 - user delete ###
# print("Creating user...")
# user = crud.create_user(db, email="julia@example.com", password_hash="abc")
# print("Created:", user.id, user.name, user.email)

# print("Reading user...")
# fetched_user = crud.get_user_by_email(db, email="julia@example.com")
# print("Fetched:", fetched_user.id, fetched_user.name, fetched_user.email)

# print("Deleting user...")
# deleted_user = crud.delete_user(db, fetched_user.id)
# print("Deleted:", deleted_user.id, deleted_user.name, deleted_user.email)

# print("Reading user...")
# fetched_user = crud.get_user(db, user_id=deleted_user.id)
# print("Fetched:", fetched_user)  # Should be None

### fake test 3 - activity create ###
# try:
#     print("Creating activity...")
#     new_activity = crud.create_activity(
#         db,
#         user_id=999, # this should raise an exception because the user does not exist
#         distance=1000.0,
#         moving_time=3600.0,
#         name="Morning Run",
#     )
#     print("Created:", new_activity.id, new_activity.name, new_activity.distance, new_activity.moving_time)
# except Exception as e:
#     print("Error:", e)

try:
    print("Creating activity...")
    new_activity = crud.create_activity(
        db,
        user_id=1, 
        distance=3000.0,
        moving_time=3600.0,
        name="Afternoon Run",
    )
    print("Created:", new_activity.id, new_activity.name, new_activity.distance, new_activity.moving_time)
except Exception as e:
    print("Error:", e)

### fake test 4 - activity read ###
# print("Reading activity...")
fetched_activity = crud.get_activity(db, activity_id=2)
print("Fetched:", fetched_activity.id, fetched_activity.name, fetched_activity.distance, fetched_activity.moving_time)

# print("Reading all activities...")
all_activities = crud.get_activities(db)
print("All activities:")
for activity in all_activities:
    print(activity.id, activity.name, activity.distance, activity.moving_time)

# print("Reading all activities for a user...")
users_activities = crud.get_activities_by_user(db, user_id=1)
print("All activities for user 1:")
for activity in users_activities:
    print(activity.id, activity.name, activity.distance, activity.moving_time)


db.close()
