

# Project Overview

This repository contains three mini projects developed as part of hands-on practice in Java, Python, and SQL. These projects focus on solving real-world problems using basic programming concepts, data processing, and database queries.

---

# Python Project: Social Media Content Sanitizer

## Description

This project simulates a content moderation system used in social media platforms. It scans user posts, removes inappropriate words, and extracts web links for review.

## Features

- Replaces banned words with "***"
- Extracts URLs from posts
- Tracks how many times each user posts inappropriate content
- Stores extracted links in a file

## Concepts Used

- String processing
- List handling
- Dictionary (for user tracking)
- File handling
- .replace() method
- .startswith() method

## Logic

The program reads a list of sample posts and checks each post for banned words like "bad", "toxic", and "hate". If a banned word is found, it is replaced with "***" using the `.replace()` method.

Then, the program checks each word in the post using `.startswith("http")` to identify web links and stores those links in a separate text file called `links_found.txt`.

A dictionary is used to count how many times each user posts flagged content. Finally, the program prints a summary report showing total posts screened, cleaned posts, blocked posts, and user flag details.

# Java Project: Utility Bill Generator

# Description

This project calculates electricity bills using a slab-based pricing system and generates a formatted receipt for each user.

# Features

* Takes user input for meter readings
* Validates input values
* Calculates bill using slab logic
* Adds tax to total amount
* Runs continuously until user exits

# Concepts Used

* Conditional statements (if-else)
* Loops
* Interface (for abstraction)
* Input handling using Scanner

# Logic

The program calculates units consumed based on meter readings. It then applies different rates for different unit ranges (slabs) and computes the total bill including tax.

---

# SQL Project: E-Commerce Logistics Tracker

# Description

This project analyzes shipment and delivery data to track logistics performance.

# Features

* Stores partner, shipment, and delivery data
* Identifies delayed shipments
* Analyzes delivery success and returns
* Finds most active delivery locations

# Concepts Used

* Table creation
* Joins
* Group By
* Aggregate functions

# Logic

The database stores shipment details and delivery status. SQL queries are used to filter delayed deliveries, count successful vs returned shipments, and analyze data by location.

---

# Conclusion

These projects helped in understanding core programming concepts, data handling, and problem-solving using different technologies.

---
