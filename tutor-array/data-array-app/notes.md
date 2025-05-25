# Data Array App

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

A Flask web application for performing various operations on number arrays with persistent session storage.

## Features

- 🧮 Array operations:
  - Get first/last elements
  - Find maximum/minimum values
  - Filter even/odd numbers
  - Array slicing
- 🔄 Session persistence (data remains until browser refresh)
- ♻️ Reset to original array
- 📱 Responsive design

## Live Demo

[Try it here!](https://rezayw-data-array-app.herokuapp.com) (if deployed)

## Screenshot

![App Screenshot](/screenshot.png) <!-- Add your screenshot file -->

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/rezayw/data-array-app.git
cd data-array-app

python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

cp .env.example .env

FLASK_SECRET_KEY=your_super_secret_key_here

python app.py