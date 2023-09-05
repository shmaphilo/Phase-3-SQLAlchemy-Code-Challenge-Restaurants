# Phase-3-SQLAlchemy-Code-Challenge-Restaurants

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Anagram Checker](#anagram-checker)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the Restaurants Application! This application provides a versatile platform for managing restaurant information, customer records, customer reviews, and even an anagram checker. Whether you're a restaurant owner, a customer, or just an anagram enthusiast, this application has something for you.

## Features

The Restaurants Application offers a range of features, including:

- **Restaurant Management**: Easily add, update, or delete restaurant information, including names and price ranges.

- **Customer Management**: Keep track of customer records, including first names and last names.

- **Review System**: Allow customers to leave detailed reviews for restaurants, complete with star ratings and feedback.

- **Anagram Checker**: Quickly find anagrams for a given word within a list of words.

## Getting Started

### Installation

To get started with the Restaurants Application, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/shmaphilo/Phase-3-SQLAlchemy-Code-Challenge-Restaurants.git


## Usage

- **Restaurant Information**: Easily access and manage restaurant details.

- **Customer Records**: Keep customer records up to date.

- **Review System**: Enable customers to leave detailed reviews for restaurants.

- **Anagram Checker**: Use the built-in anagram checker to find anagrams within a list of words.

## Database Schema

The Restaurants Application uses a simple and effective database schema consisting of three tables:

- **restaurants**: Stores essential restaurant information, including names and price ranges.

- **customers**: Maintains customer records, including first names and last names.

- **reviews**: Records customer reviews for restaurants, including star ratings and feedback.

Here's a simplified schema diagram:

```
+---------------+        +--------------+        +-------------+
|  restaurants  |   1    |   reviews    |   N    |   customers |
|---------------| ------ |--------------| ------ |-------------|
| id            |        | id           |        | id          |
| name          |   <----| restaurant_id| ---->  | first_name  |
| price         |        | customer_id  |        | last_name   |
+---------------+        | star_rating  |        +-------------+
                        | feedback     |
                        +--------------+
```

## Anagram Checker

The application includes a powerful anagram checker feature. You can input a word and a list of possible anagrams, and the program will identify and display the correct anagram(s).

## Contributing

Contributions to the Restaurants Application are encouraged and welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub. If you'd like to contribute to the project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the `MIT` License. 

## Author
It is written by Philip Ogaye.