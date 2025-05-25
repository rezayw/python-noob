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

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/rezayw/data-array-app.git
cd data-array-app
```

### 2. Setup enviroment
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Linux/Mac:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate

```
### 3. Configure environment variables
```bash
# Copy example environment file
cp .env.example .env

# Edit the .env file (replace with your secret key)
# FLASK_SECRET_KEY=your_super_secret_key_here
```
### 4. Run application
```bash
python app.py
```
