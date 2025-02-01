# GWA Automation for BulSU PRIISMS

This script automates the process of logging into the BulSU portal, fetching your grades, and calculating your General Weighted Average (GWA).

## Disclaimer

The GWA output of this script is not accurate. My official GWA is different from what I got here. I don't know the official way of calculating GWA in BulSU.

Also, this script is not being maintained and may stop working as BulSU PRIISMS change.

## Requirements

- Python 3.7+
- [Playwright](https://github.com/microsoft/playwright-python)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/gwa-calculator.git
    cd gwa-calculator
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    playwright install
    ```

## Usage

1. (If using a virtual environment) Activate the virtual environment:

    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Run the script:

    ```bash
    python gwa_calculator.py
    ```

3. Enter your BulSU PRIISMS username and password when prompted.

4. The script will log into the portal, fetch your grades, and compute your GWA.

## Notes

- Latin honors checking is based on BOR Resolution #47 Series of 2018.
- Make sure your internet connection is stable as the script interacts with the BulSU PRIISMS online.
- This GWA calculator only takes into account grades that are posted in the BulSU PRIISMS.
- Your credentials are not stored and are only used to log into the portal during the execution of the script.
