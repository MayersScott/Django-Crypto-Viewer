# Django-Crypto-Viewer

Django-Crypto-Viewer is a Django web application that allows users to view cryptocurrency prices. It fetches real-time cryptocurrency price data from Binance API and displays it in various currencies.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MayersScott/Django-Crypto-Viewer.git
   cd Django-Crypto-Viewer
1. Create a virtual environment (venv) and activate it:
   ```python
   python -m venv venv
   ```
   source `venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
   ```python
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```python
   python manage.py migrate
   ```

7. Start the development server:
   ```python
   python manage.py runserver
   ```

9. Access the application in your web browser at `http://localhost:8000`.

## Usage
Visit the homepage to view real-time cryptocurrency prices.
Prices are displayed in `USD`, `EUR`, `RUB`, and `CNY`.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

## Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.
License
This project is licensed under the MIT License - see the `LICENSE` file for details.


