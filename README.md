# Hackernews_Clone
 HackerNews Clone

Welcome to the HackerNews Clone application! This application allows you to browse and interact with news items similar to the popular HackerNews website.

Installation

1. Download the Application:
    - Download the HackerNews Clone zip file from the repository.

2. Extract the Zip File:
    - Extract the contents of the zip file to your desired location on your computer.

3. Install Dependencies:
    - Navigate to the extracted directory in your terminal or command prompt.
    - Make sure you have Python installed on your system.
    - Create a virtual environment using the following command:
        ```
        python -m venv venv
        ```
    - Activate the virtual environment:
        - On Windows:
            ```
            venv\Scripts\activate
            ```
        - On macOS and Linux:
            ```
            source venv/bin/activate
            ```
    - Install the required dependencies using:
        ```
        pip install -r requirements.txt
        ```

4. Set Up the Database:
    - Ensure you have MySQL installed on your system.
    - Create a new MySQL database.
    - Run the `hackernews_table.sql` script in your MySQL client to create the necessary tables.
    - Update the `app.py` file with your MySQL database credentials in the `db_config` dictionary.

5. Run the Application:
    - After setting up the database and updating the `app.py` file, you're ready to run the application.
    - Start the Flask application by running:
        ```
        python app.py
        ```
    - Access the application in your web browser at `http://localhost:5000`.

Usage

- Once the application is running, you can sign up for a new account or log in with existing credentials.
- Browse through the news items, mark them as read, or delete them as desired.
- Enjoy using the HackerNews Clone application!


![dashboard1](https://github.com/jayachandranpm/Hackernews_Clone/assets/82634371/d8c3904a-3903-4e40-b79f-5852f2a6c233)

![dashboard_darkmode](https://github.com/jayachandranpm/Hackernews_Clone/assets/82634371/4f790352-a942-42c5-bcf7-e0c688c30089)
