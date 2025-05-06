# Flask_02

Practice project in the Advanced Python course for Excelentians.  
This project demonstrates how to use Flask to access a remote API (Nobel Prize API) and retrieve data, structured using best practices.

---

## Features

- Fetch Nobel prize categories
- Fetch Nobel laureates' first and last names
- Find the top appearing prize category
- Retrieve prize categories for a specific year
- Fetch a country's code by its name

---

## API Endpoints

| **Endpoint**                  | **Method** | **Description**                                 |
|-------------------------------|------------|-------------------------------------------------|
| `/prizes/categories`          | GET        | Fetch all Nobel prize categories               |
| `/prizes/names`               | GET        | Fetch first and last names of Nobel laureates  |
| `/prizes/top-category`        | GET        | Fetch the top appearing prize category         |
| `/prizes/categories-by-year`  | GET        | Fetch prize categories by a given year         |
| `/countries/code`             | GET        | Fetch a country's code by its name             |

---

## Requirements

- Python 3.8+
- Flask 2.0+
- `requests` library

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DavidIsraelN/Flask_02.git
    cd Flask_02
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source venv/bin/activate   # On Windows: ./.venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    flask run
    ```

---

## Configuration

If there is some issue make sure the `FLASK_APP` environment variable points to the main file. For example:
```bash
export FLASK_APP=run.py   # On Windows: set FLASK_APP=run.py
````

---

## Usage

After starting the Flask server, use the following URLs to test the API:

### Examples

1. Fetch all prize categories:

   ```
   http://127.0.0.1:5000/prizes/categories
   ```

2. Fetch names of Nobel laureates:

   ```
   http://127.0.0.1:5000/prizes/names
   ```

3. Get prize categories for the year 2020:

   ```
   http://127.0.0.1:5000/prizes/categories-by-year?year=2020
   ```

4. Fetch country code for Israel:

   ```
   http://127.0.0.1:5000/countries/code?country=Israel
   ```

---

## Project Structure

```
Flask_02/
│
├── app/
│   ├── __init__.py
│   ├── repositories/
│   │   └── nobel_repository.py
│   ├── routes/
│   │   ├── prize_routes.py
│   │   └── country_routes.py
│   └── services/
│       ├── prize_service.py
│       └── country_service.py
│
├── requirements.txt
├── run.py
└── README.md
```

---

## Contributions

Contributions are welcome!
Feel free to fork this repository and submit pull requests.
