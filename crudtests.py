import unittest
from app import app, db, Person

class EditDataTestCase(unittest.TestCase):
    
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

    def testGetData(self):
        # Add test data to the database
        person = Person(name="Leia", height="150", mass="49", hairColor="brown", skinColor="fair", eyeColor="brown", birthYear="19BBY", gender="female")

        # Add to the session and commit before running the test
        with app.app_context():
            db.session.add(person)
            db.session.commit()

            # Refresh the person instance to get the latest state from the database
            db.session.refresh(person)

            # Now that the session is refreshed, we can test the '/getData/<id>' route
            response = self.app.get(f'/getData/{person.id}')

        # Check if the response is correct
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "Leia")
        self.assertEqual(response.json['height'], "150")

    def testEditData(self):
        # Create a test person in the database
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

            # Refresh the person instance to ensure it's properly loaded with the session
            person = Person.query.get(person.id)  # Reload the person from the DB

        # Prepare the updated data to be sent in the PUT request
        updated_data = {
            "height": "175", 
            "mass": "80"
        }

        # Send the PUT request to edit the person data
        response = self.app.put(f'/editData/{person.id}', json=updated_data)

        # Check if the response is correct
        self.assertEqual(response.status_code, 200)
        self.assertIn("Person data updated successfully!", response.json['message'])

        # Verify the changes were applied in the database
        with app.app_context():
            updated_person = Person.query.get(person.id)
            self.assertEqual(updated_person.height, "175")
            self.assertEqual(updated_person.mass, "80")
            self.assertEqual(updated_person.name, "Luke Skywalker")  # Name should remain unchanged

    def testEditDataPersonNotFound(self):
        # Try to edit a person that doesn't exist (using a non-existent id)
        response = self.app.put('/editData/999', json={"height": "180"})
        
        # Check if the response indicates the person was not found
        self.assertEqual(response.status_code, 404)
        self.assertIn("Person not found!", response.json['message'])

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
            deletedPerson = Person.query.get(person.id)
            self.assertIsNone(deletedPerson)  # The person should be None after deletion

    def test_delete_data_person_not_found(self):
        # Try to delete a person that doesn't exist (using a non-existent id)
        response = self.app.delete('/deleteData/999')
        
        # Check if the response indicates the person was not found
        self.assertEqual(response.status_code, 404)
        self.assertIn("Person not found!", response.json['message'])
           



if __name__ == '__main__':
    unittest.main()