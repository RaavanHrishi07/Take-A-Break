# Take A Break Reminder

A simple Python command-line utility that automatically opens your favourite websites at a user-defined interval to remind you to take regular breaks.

## Features

- Add multiple favourite website URLs
- Validate HTTP and HTTPS URLs
- Set a custom break interval in minutes
- Automatically open websites in the default browser
- Rotate through favourite websites on each break
- Display the next break interval
- Stop the reminder safely with `Ctrl+C`
- Includes automated unit tests

## How It Works

1. Enter one or more favourite website URLs.
2. Press Enter on an empty input when you have finished adding websites.
3. Enter the break interval in minutes.
4. The program waits for the configured interval.
5. A website is automatically opened in the default browser.
6. The program continues rotating through the configured websites.
7. Press `Ctrl+C` whenever you want to stop the reminder.

## Requirements

- Python 3.8 or newer
- A default web browser

The project uses only Python standard-library modules, so no external packages are required.

## Installation

Clone the repository:

    git clone https://github.com/RaavanHrishi07/Take-A-Break.git

Move into the project directory:

    cd Take-A-Break

## Usage

Run the program:

    python take_a_break.py

Example:

    ========================================
           TAKE A BREAK REMINDER
    ========================================

    Enter your favourite websites.
    Press Enter without typing a URL when you are finished.

    Website 1: https://www.youtube.com
    Website 2: https://github.com
    Website 3:

    Enter break interval in minutes: 120

    Favourite websites:
    1. https://www.youtube.com
    2. https://github.com

    Reminder started.
    Break interval: 120 minute(s).
    Press Ctrl+C to stop the program.

    Next break in 120 minute(s)...

    Break time! Opening: https://www.youtube.com

## Testing

For testing purposes, you can use a short interval such as:

    0.05

This represents approximately 3 seconds.

Run the automated tests with:

    python -m unittest test_take_a_break.py

## Stopping the Program

Press:

    Ctrl+C

The program will stop gracefully.

## Project Structure

    Take-A-Break/
    │
    ├── take_a_break.py
    ├── test_take_a_break.py
    ├── .gitignore
    └── README.md

## Author

Hrishikesh Sharma

GitHub: https://github.com/RaavanHrishi07

## License

This project is licensed under the MIT License.