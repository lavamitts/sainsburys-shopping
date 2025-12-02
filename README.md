# Make shopping lists

## About this repository

This repo performs two actions:

- Generates shopping lists from a template based on a provided start date
- Generates QR codes for hyperlinked recipes

## Installation

- Create and activate a virtual environment, e.g.

  ```shell
  uv venv .venv
  source .venv/bin/activate  # (MacOS)
  .venv\Scripts\Activate  # (Windows)
  ```

- Install the required packages:

  ```shell
  uv pip install -r requirements.txt
  ```

## Configuration

- Review env.sample
- Take a copy and rename as .env
- Complete configuration as per instructions

## Running 

### Generates an empty shopping list

- `python gen.py yymmdd`

  *or *

- `python gen.py yymmdd no-qr`

### Searches a shopping list for hyperlinks, generates a QR code where a link is found

- `python qr.py yymmdd`
