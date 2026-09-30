import time
import webbrowser
from urllib.parse import urlparse


def is_valid_url(url):
    """Check whether the URL has a valid HTTP or HTTPS format."""
    try:
        parsed_url = urlparse(url)
        return parsed_url.scheme in {"http", "https"} and bool(parsed_url.netloc)
    except ValueError:
        return False


def get_favourite_urls():
    """Collect and validate favourite URLs from the user."""
    urls = []

    print("\nEnter your favourite websites.")
    print("Press Enter without typing a URL when you are finished.\n")

    while True:
        url = input(f"Website {len(urls) + 1}: ").strip()

        if not url:
            break

        if is_valid_url(url):
            urls.append(url)
        else:
            print("Invalid URL. Please enter a valid HTTP or HTTPS URL.")

    return urls


def open_break_url(url):
    """Open the selected URL in the default web browser."""
    opened = webbrowser.open(url)

    if opened:
        print(f"\nBreak time! Opening: {url}")
    else:
        print("\nCould not open the URL in the browser.")


def get_break_interval():
    """Get a positive break interval from the user in minutes."""
    while True:
        try:
            minutes = float(input("\nEnter break interval in minutes: "))

            if minutes <= 0:
                print("Interval must be greater than 0.")
                continue

            return minutes * 60

        except ValueError:
            print("Please enter a valid number.")


def wait_for_break(seconds):
    """Wait for the configured break interval."""
    minutes = seconds / 60
    print(f"\nNext break in {minutes:g} minute(s)...")
    time.sleep(seconds)


def main():
    print("=" * 40)
    print("       TAKE A BREAK REMINDER")
    print("=" * 40)

    urls = get_favourite_urls()

    if not urls:
        print("No valid URLs were added.")
        return

    interval_seconds = get_break_interval()

    print("\nFavourite websites:")
    for number, url in enumerate(urls, start=1):
        print(f"{number}. {url}")

    interval_minutes = interval_seconds / 60

    print("\nReminder started.")
    print(f"Break interval: {interval_minutes:g} minute(s).")
    print("Press Ctrl+C to stop the program.")

    current_url = 0

    try:
        while True:
            wait_for_break(interval_seconds)

            open_break_url(urls[current_url])

            current_url = (current_url + 1) % len(urls)

    except KeyboardInterrupt:
        print("\nTake A Break Reminder stopped.")


if __name__ == "__main__":
    main()
    