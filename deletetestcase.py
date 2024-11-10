import unittest
from app import app, db, Person

class DeleteDataTestCase(unittest.TestCase):

    def setUp(self):
        # Set up the Flask test client and application context
        self.app = app.test_client()
        self.app.testing = True

        # Create application context before interacting with the database
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Remove the session and drop all tables after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def testDeleteData(self):
        # Add a test person to the database
        person = Person(
            name="Luke Skywalker", 
            height="172", 
            mass="77", 
            hairColor="blond", 
            skinColor="fair", 
            eyeColor="blue", 
            birthYear="19BBY", 
            gender="male"
        )

        # Add to the session and commit
        with app.app_context():
            db.session.add(person)
            db.session.commit()

        # Re-attach the person object to the session before deleting it
        with app.app_context():
            person = db.session.merge(person)  # This attaches the person to the current session

        # Send the DELETE request to delete the person
        response = self.app.delete(f'/deleteData/{person.id}')

        # Check if the response is correct (status code and message)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Person deleted successfully!", response.json['message'])

        # Verify the person is deleted from the database
        with app.app_context():
            deleted_person = Person.query.get(person.id)
            self.assertIsNone(deleted_person)  # The person should be None after deletion

    def testDeleteDataPersonNotFound(self):
        # Try to delete a person that doesn't exist (using a non-existent id)
        response = self.app.delete('/deleteData/999')
        
        # Check if the response indicates the person was not found
        self.assertEqual(response.status_code, 404)
        self.assertIn("Person not found!", response.json['message'])

if __name__ == '__main__':
    unittest.main()
