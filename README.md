# IDP_Filter
## IDP Text Filter Program

### Introduction

This project is designed to solve the widespread interdependence privacy issues of third-party applications. Up to now, the design and deployment of protection measures to protect interdependent privacy are restricted by many factors: 1. From a legal perspective, GDPR does not put forward specific requirements for the management of interdependent privacy data, so application developers and application platforms lack sufficient excitation. 2. In terms of actual deployment, there is a lack of unified standards for the management of interdependent data. Improper handling will affect the user experience.

### Features

- User registration and authentication.
- Customizable filters for:
  - Names
  - Numbers
  - Links
  - Countries
  - Medicines
  - Streets
- User-defined sensitive and non-sensitive words.
- Text input to see the filter in action.

### Setup

#### Prerequisites

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite

#### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the directory:

   ```bash
   cd path-to-directory
   ```

3. Install the required libraries:

   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

4. Initialize the SQLite database:

   ```python
   from app import db
   db.create_all()
   ```

### Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open a web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

3. Register a new user or login with existing credentials.

4. Once logged in, you'll be directed to the dashboard where:
   - You can define sensitive and non-sensitive words.
   - Enable/disable specific filters.
   - Input text to see the filter in action.

5. To view the filtered text, scroll down to the "Filtered Text" section.

### Known Issues

1. Filenames should not include `.csv` in the category names as the system automatically appends this during the file read process.

### Contributing

Contributions are welcome. Please fork the repository and submit pull requests for any enhancements, fixes, or features you think might be valuable.

### License

This project is licensed under the MIT License.

### Acknowledgements

Thanks to the OpenAI community for guidance and support during the development of this program.
