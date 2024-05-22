# GWA Automation for BulSU PRIISMS

This script automates the process of logging into the BulSU portal, fetching your grades, and calculating your General Weighted Average (GWA).

## Requirements

- Python 3.7+
- [Playwright](https://playwright.dev/python/docs/intro) Python library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/gwa-calculator.git
    cd gwa-calculator
    ```

2. Install the required Python packages:

    ```bash
    pip install playwright
    playwright install
    ```

## Usage

1. Run the script:

    ```bash
    python gwa_calculator.py
    ```

2. Enter your BulSU Portal username and password when prompted.

3. Enter your grade for Numerical Analysis (temporary while the portal is not updated).

4. The script will log into the portal, fetch your grades, and compute your GWA.

## Notes

- Make sure your internet connection is stable as the script interacts with the BulSU Portal online.
- Your credentials are not stored and are only used to log into the portal during the execution of the script.
