# project_1:FastAPI Overview

FastAPI is a modern, fast (high-performance), and easy-to-use web framework for building APIs with Python. It’s based on standard Python type hints and provides automatic generation of interactive documentation for your APIs, such as Swagger UI and ReDoc.

This guide will walk you through the basics of FastAPI and how it works.

1. POST /users: Create a new user
Purpose: To create a new user in the database.
Input: The request body contains user details (like name, email, etc.) using the UserModel model.
Processing:
The input is converted to a dictionary.
The insert_datetime field is automatically added with the current timestamp.
The new user record is inserted into the user_collection MongoDB collection.
The API retrieves the newly created user record from the database and returns it in the response.

2. GET /users/{id}: Retrieve a user by ID
Purpose: To retrieve a specific user by its unique MongoDB ID (_id).
Processing:
The ID is validated as a MongoDB ObjectId.
The API searches the user_collection for a document with the provided ID.
If a matching user is found, it’s returned in the response. Otherwise, a 404 error is raised.

3. POST /users/filter: Filter users
Purpose: To filter users based on criteria such as name, email, or insertion date.
Input: The request body contains the filter options using the UserFilterModel.
Processing:
The input is converted into a MongoDB query.
The API searches the user_collection for matching records.
Returns a list of users that match the filter criteria (up to 100 users).

4. DELETE /users/{id}: Delete a user by ID
Purpose: To delete a user from the database using their ID.
Input: The id parameter is passed in the URL path.
Processing:
The MongoDB ObjectId is validated.
The user record is deleted from the user_collection.
If the user is successfully deleted, a confirmation message is returned. Otherwise, a 404 error is raised if the user does not exist.
Example Request: DELETE /users/615f1b912fb48f5c23a37d2a

Create: Use POST /clock-in to create new records.
Retrieve: Use GET /clock-in/{id} to get a record by its ID.
Filter: Use POST /clock-in/filter to filter records based on criteria.
Delete: Use DELETE /clock-in/{id} to delete a record by its ID.
Update: Use PUT /clock-in/{id} to update a record by its ID.
Each operation performs validation, ensures data integrity, and interacts with the MongoDB database to store or retrieve the necessary clock-in data. The API uses Pydantic models to ensure the input and output data is structured and validated correctly.

1. POST /clock-in: Create a new clock-in record
Purpose: To create a new clock-in record in the database.
Input: The request body contains details about the clock-in (email, location, etc.) using the ClockInModel model.
Processing:
Converts the input into a dictionary and adds an additional field insert_datetime with the current timestamp.
Inserts the new clock-in record into the clock_in_collection MongoDB collection.

2. GET /clock-in/{id}: Retrieve a clock-in record by ID
Purpose: To retrieve a specific clock-in record using its unique MongoDB ID (_id).
Input: The id parameter is passed in the URL path.
Processing:
The ID is validated to check if it’s a valid MongoDB ObjectId.
The record is fetched from the clock_in_collection using the provided ID.
If the record is found, it’s returned in the response; otherwise, a 404 error is raised.

3. POST /clock-in/filter: Filter clock-in records
Purpose: To filter clock-in records based on provided criteria (like email, location, and date).
Input: The request body contains filter options using the ClockInFilterModel.
Processing:
A query object is built from the provided filters.
The query is executed against the MongoDB collection, fetching all matching records (up to 100 results).
The filtered records are returned as a list.

4. DELETE /clock-in/{id}: Delete a clock-in record by ID

Purpose: To delete a specific clock-in record using its ID.
Input: The id parameter is passed in the URL path.
Processing:
The ID is validated to ensure it’s a valid MongoDB ObjectId.
The record is deleted from the database if it exists.
If the deletion is successful, a confirmation message is returned. If the record is not found, a 404 error is raised.

5. PUT /clock-in/{id}: Update a clock-in record by ID
Purpose: To update an existing clock-in record (except for the insert_datetime field).
Input: The id parameter is passed in the URL path, and the request body contains updated values using the ClockInModel.
Processing:
The ID is validated to ensure it’s a valid ObjectId.
Only the non-None fields in the request body are used to update the record.
The record is updated in the database.
If the update is successful, a confirmation message is returned. If the record is not found, a 404 error is raised.

Conclusion

FastAPI’s automatic documentation is a powerful tool that not only helps developers interact with your API but also keeps your documentation always up-to-date. With no extra configuration needed, FastAPI automatically generates Swagger UI and ReDoc documentation for every API route, making it easier to visualize, understand, and test your APIs.

For further customization or more advanced use cases, refer to the official FastAPI documentation

uvicorn main:app --reload
http://127.0.0.1:8000- Fastapi/docs
mongodb://localhost:27017

use companyDB
db.createCollection('items')
db.createCollection('user_clock_in_records')
