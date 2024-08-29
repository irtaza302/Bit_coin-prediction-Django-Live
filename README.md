# Live Bitcoin Prediction

This project is a Django-based web application that fetches the current Bitcoin price, predicts the next minute's price using a simple linear regression model, and displays the data on a web page. The application updates the prediction and the displayed data every minute.

## Features

- Fetches the current Bitcoin price from the CoinDesk API.
- Uses a simple linear regression model to predict the next minute's Bitcoin price.
- Displays the current and predicted prices on a web page.
- Updates the prediction and displayed data every minute.
- Displays historical Bitcoin prices on a chart.

## Technologies Used

- Django
- Background Task
- Pandas
- Scikit-learn
- NumPy
- Chart.js
- HTML/CSS/JavaScript

## Setup Instructions

### Prerequisites

- Python 3.8+
- Django 3.2+
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/live-bitcoin-prediction.git
    cd live-bitcoin-prediction
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Start the background task scheduler:**

    ```bash
    python manage.py process_tasks
    ```

8. **Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application in action.**

## Project Structure
live-bitcoin-prediction/
├── live_prediction/
│   ├── migrations/
│   ├── templates/
│   │   └── live_prediction/
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tasks.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── bitcoin_prediction/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md

## Key Files

- **`live_prediction/tasks.py`**: Contains the background task that fetches the current Bitcoin price and predicts the next minute's price.
- **`live_prediction/views.py`**: Contains the view that fetches the latest prediction and renders the web page.
- **`live_prediction/templates/live_prediction/index.html`**: The HTML template for the web page.
- **`live_prediction/models.py`**: Defines the `Prediction` model used to store predictions in the database.

## Usage

- The application fetches the current Bitcoin price and predicts the next minute's price every minute.
- The web page displays the current and predicted prices, and updates them every minute.
- The historical Bitcoin prices are displayed on a line chart.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [CoinDesk API](https://www.coindesk.com/coindesk-api) for providing the Bitcoin price data.
- [Chart.js](https://www.chartjs.org/) for the charting library.
- [Django Background Tasks](https://django-background-tasks.readthedocs.io/en/latest/) for the background task scheduler.
