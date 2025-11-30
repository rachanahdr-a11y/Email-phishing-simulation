# Gmail Phishing Simulator

## Overview

This project is a phishing simulation tool designed to mimic the Google Gmail login page. It captures entered credentials and saves them to a file for educational and testing purposes. The tool demonstrates how phishing attacks can be crafted to deceive users into revealing sensitive information.

-----------------------

## How It Works

- The app is built using Flask, a lightweight Python web framework.
- When accessed, it serves a login page styled to closely resemble the official Google Gmail login.
- Users enter their email and password, which are then logged to a file named `phished_credentials.txt` in the project root.
- After submission, the user is shown an error message to simulate a failed login attempt, encouraging them to try again.
- The app uses Flask's flash messaging to display error messages and redirects back to the login page after each submission.

------------------------

## Features

- Realistic UI with animations and color schemes similar to Google's login page.
- Securely logs credentials to a local file for analysis.
- Simple and easy to deploy with minimal dependencies (only Flask).
- Can be adapted to simulate phishing pages for other popular sites such as:
  - Bank login portals
  - Social media platforms like Twitter, Instagram, Facebook
  - Other email providers and online services

-------------------------

## Installation

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements/requirements.txt
   ```
3. Run the app:
   ```
   python src/app.py
   ```
4. Access the login page at `http://127.0.0.1:5000/` in your browser.

----------------------------

## Usage Tips & Security Awareness

Phishing attacks like this exploit trust by mimicking legitimate websites. To protect yourself:

- Always check the URL in your browser’s address bar before entering credentials.
- Look for HTTPS and valid security certificates.
- Be cautious of unsolicited emails or links asking for login information.
- Use two-factor authentication (2FA) wherever possible.
- Keep your software and browsers updated.
- Educate yourself and others about common phishing tactics.

-----------------------------
