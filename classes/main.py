from services.data_service import DataService


# --------------------------------------------------------------
# Create an instance of the class
# --------------------------------------------------------------

data_service = DataService()  # Instance of the DataService class


# --------------------------------------------------------------
# Call the methods of the instance to run the pipeline
# --------------------------------------------------------------

data_service.run()  # Run the data processing pipeline


# --------------------------------------------------------------
# Access the attributes of the instance
# --------------------------------------------------------------

data_service.data  # Access the DataFrame with processed data

import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")

print(PASSWORD)
