# AI Coach App

The AI Coach App is a web application designed to provide personalized fitness and nutrition advice. It leverages AI to generate tailored recommendations based on user profiles, goals, and other inputs.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Personal Data Management**: Users can input and update their personal information.
- **Goal Setting**: Users can set and manage their fitness goals.
- **Macro Calculation**: The app calculates recommended daily intake of protein, calories, fat, and carbohydrates based on user profiles and goals.
- **Notes Management**: Users can add, view, and delete notes.
- **AI Interaction**: Users can ask the AI questions and receive personalized responses.

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/AI-Coach-App.git
   cd AI-Coach-App
   ```

2. **Create and activate a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a [.env](http://_vscodecontentref_/0) file in the root directory and add the necessary environment variables:
   ```
   APPLICATION_TOKEN_2=your_application_token
   ```

## Usage

1. **Run the application**:

   ```sh
   streamlit run main.py
   ```

2. **Access the application**:
   Open your web browser and go to `http://localhost:8501`.

3. **Interact with the application**:
   - Fill out the personal data form.
   - Set your fitness goals.
   - Add notes and ask the AI questions to receive personalized advice.

## Project Structure

AI-Coach-App/
├── init.py
├── pycache/
├── .env
├── .gitignore
├── ai.py
├── db.py
├── flows/
│ ├── AskAI.json
│ ├── Macro.json
├── form_submit.py
├── LICENSE
├── main.py
├── profiles.py
├── prompts/
│ ├── conditional_router.txt
│ ├── general_agent.txt
│ ├── macro.txt
│ ├── tool_calling_agent.txt
├── README.md
├── requirements.txt

- **ai.py**: Contains functions for interacting with the AI, including `ask_ai` and `get_macros`.
- **db.py**: Handles database interactions.
- **form_submit.py**: Manages form submissions for updating personal information and notes.
- **main.py**: The main entry point for the Streamlit application.
- **profiles.py**: Functions for creating and retrieving user profiles and notes.
- **flows/**: Contains JSON files defining the AI interaction flows.
- **prompts/**: Contains text files with prompt templates for the AI.
- **requirements.txt**: Lists the Python dependencies for the project.
- **.env**: Environment variables for the application.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **LICENSE**: The license for the project.

## API Endpoints

- **GET /profiles**: Retrieve all user profiles.
- **POST /profiles**: Create a new user profile.
- **PUT /profiles/{id}**: Update an existing user profile.
- **DELETE /profiles/{id}**: Delete a user profile.
- **GET /notes**: Retrieve all notes.
- **POST /notes**: Create a new note.
- **DELETE /notes/{id}**: Delete a note.

## Technologies Used

- **Python**: The main programming language used.
- **Streamlit**: The framework used for building the web application.
- **AstraDB**: The database used for storing user data and notes in vector form.
- **Groq API**: Used for generating AI responses.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/1) file for details.
