# eCommerce and Sewing services application 

This is a eCommerce and Sewing services application built using Django 4, Bootstrap 4 and SQLite database to store data.

## Table of Contents

- Introduction

- Setup and Installation

- User Management

- Product Catalog

- Shopping Cart and Checkout

- Admin Dashboard for Order Management

- Service Management

- Reviews and Ratings

- Admin Panel

- Conclusion


## Introduction

In this project, we have developed a eCommerce website which includes
sewing services. Our goal is to was to combine two area into one
website. Our project aims to give sewing and design professionals 
ability to sell their own products as well as provide services.

## Setup and Installation

Clone the project to your local machine;

```
git clone https://github.com/ZygimantasB/calories_counter.git
```


## PyCharm
1. Open PyCharm and choose "Open".
2. Navigate to the root directory of your project and click "OK".
3. PyCharm should recognize your Django project and set up everything automatically.
4. You can activate your virtual environment within PyCharm by opening the terminal in PyCharm and typing the 
5. activation command

On macOS/Linux:
```
source venv/bin/activate
```

On Windows:
```
venv\scripts\activate
```


5. Once your virtual environment is active, you can run your Django server from PyCharm's terminal using:
```angular2html
python manage.py runserver
```

6. Install required dependencies from the root directory run:

```
pip install -r requirements.txt
```

## SQLite Database

1. Download the Installer:
   - For Windows: Visit the SQLite Download page (https://www.sqlite.org/download.html) and download the appropriate precompiled binary for your system. Choose the "Precompiled Binaries for Windows" section and select the package based on your system architecture (32-bit or 64-bit).
   - For macOS: You can install it using Homebrew. Open the Terminal and run the command `brew install sqlite`.
   - For Linux: Open the Terminal and run the appropriate package manager command based on your distribution:
     - Debian/Ubuntu: `sudo apt-get install sqlite3`
     - Red Hat/Fedora: `sudo dnf install sqlite`
     - Arch Linux: `sudo pacman -S sqlite`

2. Run the Installer:
   - For Windows: Double-click on the downloaded installer file and follow the on-screen instructions to complete the installation. Make sure to add SQLite to your system's PATH variable during the installation process.
   - For macOS and Linux: Follow the prompts in the Terminal and provide necessary permissions or authentication when prompted. The package manager will handle the installation process automatically.

3. Verify the Installation:
   - Open a new Terminal or Command Prompt window.
   - Run the command `sqlite3` to launch the SQLite command-line interface.
   - If SQLite launches successfully and displays the SQLite prompt (e.g., `sqlite>`), the installation is successful.

## User Management

User Management covers  user registration, 
authentication, profile management, and password reset. 

## Product Catalog

Product Catalog involves displaying a collection of products,
categorizing them into various categories. Also,
it includes search bar for easy discovery of 
products.


## Usage and Documentation

Once SQLite is installed, you can start using it for your projects. 
SQLite provides various command-line tools and APIs for interacting 
with the database.


## Shopping Cart and Checkout

Shopping Cart and Checkout enable users to add items to their cart, 
update quantities, and remove items before proceeding to the checkout
process for order placement and payment processing.

## Admin Dashboard for Order Management

Order management functionalities include order history, tracking,
confirmation, invoicing, and an admin dashboard for efficient order 
management. 

## Service Management
Service Management is about listings of 
available services, providing users with detailed information
about each service offered. It also includes ability
for users to book and schedule services based on their needs.

## Reviews and Ratings
Reviews and Ratings  allows users to share their 
feedback for products and services. These reviews and ratings are then
displayed on website.

## Admin Panel
The Admin Panel provides dashboard for
administrators, allowing them to manage products,
services, user accounts, and order-related tasks. 

## Conclusion
In conclusion, this project aimed to develop an e-commerce
platform with essential features such as user management,
product catalog, shopping cart, checkout, order management,
and service management. Future improvements may include
additional features like advanced search, personalized 
recommendations and an expanded service marketplace. 







