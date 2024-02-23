# IDP_Filter
## Interdependent Privacy (IDP) protection: Text Filter Proof of Concept

### Introduction

This project is designed to solve the widespread interdependent privacy issues of third-party applications. Up to now, the design and deployment of protection measures to protect interdependent privacy are restricted by many factors: 1. From a legal perspective, GDPR does not put forward specific requirements for the management of interdependent privacy data, so application developers and application platforms lack sufficient excitation. 2. In terms of actual deployment, there is a lack of unified standards for the management of interdependent data. Improper handling will affect the user experience.

### Features

- User registration and authentication(pbkdf2).

- User-defined Self-Regarding Blacklist (SRB), Self-Regarding Whitelist (SRW) and Others-Regarding Blacklist (ORB).
- Predefined categories for Blacklist:
  - Names
  - Numbers
  - Links
  - Countries
  - Diseases
  - Streets
- Report of filtered result (number of IDP-related words) 
- User interface demo
- Accuracy analysis compared with SpaCy NER
- Efficiency analysis among different text filter methods (RE, KMP and FlashText)

### Setup

#### Prerequisites

- Python 3.8
- re
- hashlib  
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
   pip install hashlib
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

4. Define SRB, SRW and ORB, choose predefined categories as Blacklists. Update the Filter Settings whenever u want.

5. Input the text, click filter button, then you can see the filtered result and report about how many words are filtered.

### Known Issues

1. Filenames should not include `.csv` in the category names as the system automatically appends this during the file read process.

### Contributing

Contributions are welcome. Please fork the repository and submit pull requests for any enhancements, fixes, or features you think might be valuable.

### License

This project is licensed under the MIT License.

### Acknowledgements


