#!/usr/bin/python3
"""Test for DBStorage module."""
import unittest
from models import storage
from models.base_model import BaseModel
from models.state import State
import os
from sqlalchemy.exc import OperationalError, IntegrityError


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not db storage")
class TestDBStorage(unittest.TestCase):
    """DBStorage tests."""

    def setUp(self):
        """SetUp method."""
        # Assuming using an in-memory SQLite database for testing
        self.test_state = State(name="TestState")

    def tearDown(self):
        """TearDown method."""
        # Clean up any created objects to avoid storage clutter
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

        # Close the current session and roll back to clean the DB
        storage.close()
        storage.reload()

    def test_create_and_save(self):
        """Test if storage can create and save an object."""
        initial_count = len(storage.all(State))
        self.test_state.save()
        new_count = len(storage.all(State))
        self.assertTrue(new_count > initial_count)

    def test_all(self):
        """Test the all method."""
        obj_count = len(storage.all())
        self.test_state.save()
        new_obj_count = len(storage.all())
        self.assertTrue(new_obj_count > obj_count)

    def test_delete(self):
        """Test the delete method."""
        self.test_state.save()
        state_id = self.test_state.id
        storage.delete(self.test_state)
        self.assertNotIn(state_id, storage.all(State))

    def test_reload(self):
        """Test reloading objects from the database."""
        self.test_state.save()
        storage.reload()
        self.assertIn("State." + self.test_state.id, storage.all(State))

    def test_invalid_save(self):
        """Test save with an integrity error."""
        corrupt_state = State(id=12345)
        with self.assertRaises(IntegrityError):
            corrupt_state.save()

    def test_dangling_commit(self):
        """Test for hanging commits. If there's an error during a commit, the session should not be left hanging."""
        corrupt_state = State(id="invalid_id")
        try:
            storage.new(corrupt_state)
            storage.save()
        except OperationalError:
            self.assertFalse(storage._DBStorage__session.is_active)

    def test_storage_no_session(self):
        """Test that there's no session if the DB hasn't been loaded."""
        storage._DBStorage__session = None
        with self.assertRaises(AttributeError):
            storage.all()

    def test_committing_deleted(self):
        """Test attempting to commit a deleted object."""
        self.test_state.save()
        storage.delete(self.test_state)
        with self.assertRaises(OperationalError):
            storage.save()

# ... additional edge cases ...


if __name__ == "__main__":
    unittest.main()
