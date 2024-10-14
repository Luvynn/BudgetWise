# Personal Finance Tracker

# Project Reason

To develop and challenge personal abilities by creating a fullstack project integrating a multitude of languages that I am personally passionate about encapsulating self-use cases. 

Ability to store and track my personal finances but completely off-grid and localized on my PC.

This project has an emphasis on elevating version control skills, project management (Agile), Design Principles (SOLID), DSA and applying theoretical knowledge in a real-world application. 

The SOLID design principles ensure a maintainable and scalable codebase (good coding practice). Each class has a single responsibility (SRP), is open for extension but closed for modification (OCP), and can be easily replaced with alternative implementations (LSP). Interfaces are kept focused (ISP), and dependencies are managed through abstractions (DIP), making the project flexible, testable, and resilient to change.

# Project Summary

Project Overview

Goal: Develop a personal finance tracker that supports income/expense tracking, budgeting, report generation, localization, and visualizations of trends and categorized expenses.

# Technology Stack:
-	Frontend: React with TypeScript
-   Backend: Flask with Python
-   Database: SQLite for local development
-   Charts: Chart.js, Recharts

## Getting Started

These instructions explain how to set up the project and use what has been developed so far.

### Installation

1. **Clone the Repository**:
    git clone https://github.com/keonleebv/FinanceTracker.git
    cd FinanceTracker

2. **Setup Virtual Env**:
    python -m venv virtual
    virtual\Scripts\activate

3. **Install Dependencies**:
    pip install -r requirements.txt 

### Running

1. **Start application**:
    python main.py

2. **Access application**:
    ctrl+click on the browser: http://127.0.0.1:5000/ to interact with the API.

3. **Interacting with the API**:
    I use Invoke-WebRequest to test API functionality

    Add a Transaction:

    Invoke-WebRequest -Uri http://127.0.0.1:5000/add_transaction -Method Post -Body '{"date": "2024-08-10", "description": "Grocery Shopping", "category": "Expense", "amount": 150.75}' -ContentType "application/json"

    View Transactions:

    Invoke-WebRequest -Uri http://127.0.0.1:5000/transactions -Method Get

    Add a Budget:

    Invoke-WebRequest -Uri http://127.0.0.1:5000/add_budget -Method Post -Body '{"category": "Food", "amount": 500}' -ContentType "application/json"

    Compare Budgets:

    Invoke-WebRequest -Uri http://127.0.0.1:5000/compare_budget -Method Get

    Export Budgets to CSV:

    Invoke-WebRequest -Uri http://127.0.0.1:5000/export_budgets_to_csv -Method 

4. **Testing**:
    pytest 

# Agile Development Process

Sprints: Organized into multiple sprints, each focusing on different aspects:
1. Sprint 1: Basic setup and transactions functionality
2. Sprint 2: Budgeting and localization
3. Sprint 3: Reports and graphs
4. Sprint 4: Refinement and user feedback

# Local Development Setup
IDE: Visual Studio Code with relevant extensions 
- 	Version Control: Git and GitHub (public repositories)
-	Design: Figma
-	Documentation: Markdown files within the repository
-	Testing: Vite for frontend, pytest for backend, Cypress for end-to-end testing

## Software Architecture
# Frontend Components
-	Login/Signup
-	Dashboard
-	Transaction Management: Income/Expense Form, Transaction List
-	Budget Management: Budget Form, Budget Overview
-	Reports: Report View, Download Button
-	Graphs: Trend Graphs, Category Graphs
-	Localization
-	Settings

# Backend Components
-	Authentication: User Registration, User Login
-	API Endpoints
-	Transaction Management: Add/Edit/Delete Transaction, Get Transactions
-	Budget Management: Set Budget, Get Budget
-	Generation: Generate Report, Download Report
-	Graph Data: Get Trend Data, Get Category Data
-	Localization: Language Data

# Database Tables
-	Users
-	Transactions
-	Budgets
-	Localization

# Monitoring and Debugging
-	Local Logging: Use Python's built-in logging module
- Browser Developer Tools: Chrome DevTools for frontend debugging

