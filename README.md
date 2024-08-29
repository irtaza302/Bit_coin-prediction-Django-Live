## Key Files

- `live_prediction/tasks.py`: Contains the background task that fetches the current Bitcoin price and predicts the next minute's price.
- `live_prediction/views.py`: Contains the view that fetches the latest prediction and renders the web page.
- `live_prediction/templates/live_prediction/index.html`: The HTML template for the web page.
- `live_prediction/models.py`: Defines the `Prediction` model used to store predictions in the database.

## Usage

- The application fetches the current Bitcoin price and predicts the next minute's price every minute.
- The web page displays the current and predicted prices, and updates them every minute.
- The historical Bitcoin prices are displayed on a line chart.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [CoinDesk API](https://www.coindesk.com/coindesk-api) for providing the Bitcoin price data.
- [Chart.js](https://www.chartjs.org/) for the charting library.
- [Django Background Tasks](https://django-background-tasks.readthedocs.io/en/latest/) for the background task scheduler.
