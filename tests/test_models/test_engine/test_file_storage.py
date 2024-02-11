# #!/usr/bin/python3
# """Defines unittests for models/engine/file_storage.py."""

# import unittest
# from models.base_model import BaseModel
# from models.user import User
# from models.review import Review
# from models.city import City
# from models.state import State
# from models.place import Place
# from models.amenity import Amenity
# from models.engine.file_storage import FileStorage
# import datetime


# class TestFileStorage(unittest.TestCase):

#     def setUp(self):
#         """Set up the environment for each test."""
#         self.storage = FileStorage()
#         self.storage._FileStorage__objects.clear()

#     def test_classes(self):
#         """Test that the classes method returns the correct dictionary."""
#         classes = self.storage.classes()
#         expected_classes = {
#             'BaseModel': BaseModel,
#             'User': User,
#             'Place': Place,
#             'State': State,
#             'City': City,
#             'Amenity': Amenity,
#             'Review': Review
#         }
#         self.assertDictEqual(classes, expected_classes)

#     def test_get_attr(self):
#         """Test that the get_attr method returns the correct dictionary."""
#         attrs = self.storage.get_attr()
#         expected_attrs = {
#             "BaseModel": {"id": str, "created_at": datetime.datetime,
#                           "updated_at": datetime.datetime},
#             "User": {"email": str, "password": str, "first_name": str,
#                      "last_name": str},
#             "Review": {"place_id": str, "user_id": str, "text": str},
#             "City": {"state_id": str, "name": str},
#             "Place": {"city_id": str, "user_id": str, "name": str,
#                       "description": str, "number_rooms": int,
#                       "number_bathrooms": int, "max_guest": int,
#                       "price_by_night": int, "latitude": float,
#                       "longitude": float, "amenity_ids": list},
#             "State": {"name": str},
#             "Amenity": {"name": str}
#                       }
#         self.assertDictEqual(attrs, expected_attrs)

#     def test_all(self):
#         """Test that the all method returns the correct dictionary."""
#         all_objs = self.storage.all()
#         self.assertEqual(all_objs, {})

#     def test_new(self):
#         """Test that the new method adds an object correctly."""
#         user = User()
#         self.storage.new(user)
#         self.assertIn(f"{type(user).__name__}.{user.id}",
#                       self.storage.all().keys())

#     def test_save(self):
#         """Test that the save method writes to the file correctly."""
#         user = User()
#         self.storage.new(user)
#         self.storage.save()

#     def test_reload(self):
#         """Test that the reload method reads from the file correctly."""
#         user = User()
#         self.storage.new(user)
#         self.storage.save()
#         self.storage.reload()

#     def tearDown(self):
#         """Clean up after each test."""


# if __name__ == '__main__':
#     unittest.main()
