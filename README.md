# **BudgetWise – Personal Finance Tracker**

## **Project Objective**

The goal of this project is to create a full-stack personal finance tracker that integrates technologies I am passionate about while solving a real-world use case. This application is designed to run locally, allowing users to track their finances completely off-grid. 

In addition to providing practical functionality, this project emphasizes key software development skills, including:
- **Version Control** (Git/GitHub)
- **Project Management** (Agile)
- **Design Principles** (SOLID)
- **Data Structures and Algorithms (DSA)**

The **SOLID** design principles ensure the project maintains a clean, scalable codebase:
- **Single Responsibility Principle (SRP):** Each class has a single responsibility.
- **Open/Closed Principle (OCP):** Classes are open for extension but closed for modification.
- **Liskov Substitution Principle (LSP):** Objects of a superclass can be replaced with objects of its subclass without affecting the application.
- **Interface Segregation Principle (ISP):** Interfaces are small and focused, adhering to specific needs.
- **Dependency Inversion Principle (DIP):** High-level modules depend on abstractions, not concrete implementations.

## **Project Summary**

**Overview:**  
BudgetWise allows users to manage personal finances through income/expense tracking, budgeting, report generation, and visualization of trends and categorized expenses.

### **Technology Stack**
- **Frontend:** React with TypeScript
- **Backend:** Flask (Python)
- **Database:** SQLite (for local development)
- **Charts:** Chart.js, Recharts

---

## **Getting Started**

### **Installation**

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:Luvynn/finance-tracker.git
   cd FinanceTracker
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv virtual
   virtual\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### **Running the Application**

1. **Start the Application:**
   ```bash
   python main.py
   ```

2. **Access the Application:**
   - Open your browser and visit: `http://127.0.0.1:5000/`

3. **Interacting with the API (Examples):**

   - **Add a Transaction:**
     ```bash
     Invoke-WebRequest -Uri http://127.0.0.1:5000/add_transaction -Method Post -Body '{"date": "2024-08-10", "description": "Grocery Shopping", "category": "Expense", "amount": 150.75}' -ContentType "application/json"
     ```

   - **View Transactions:**
     ```bash
     Invoke-WebRequest -Uri http://127.0.0.1:5000/transactions -Method Get
     ```

   - **Add a Budget:**
     ```bash
     Invoke-WebRequest -Uri http://127.0.0.1:5000/add_budget -Method Post -Body '{"category": "Food", "amount": 500}' -ContentType "application/json"
     ```

   - **Compare Budgets:**
     ```bash
     Invoke-WebRequest -Uri http://127.0.0.1:5000/compare_budget -Method Get
     ```

   - **Export Budgets to CSV:**
     ```bash
     Invoke-WebRequest -Uri http://127.0.0.1:5000/export_budgets_to_csv -Method Get
     ```

4. **Testing:**
   - Run backend tests using:
     ```bash
     pytest
     ```

---

## **Agile Development Process**

The project is organized into several sprints, each focusing on specific functionalities:

1. **Sprint 1:** Basic setup and transactions functionality.
2. **Sprint 2:** Budgeting and localization.
3. **Sprint 3:** Reports and graphs.
4. **Sprint 4:** Refinement and user feedback.

---

## **Local Development Setup**

- **IDE:** Visual Studio Code
- **Version Control:** Git and GitHub
- **Design:** Figma for UI/UX design
- **Documentation:** Markdown within the repository
- **Testing:** 
  - **Frontend:** Vite
  - **Backend:** pytest
  - **End-to-End Testing:** Cypress

---

## **Software Architecture**

### **Frontend Components**

- **User Authentication:** Login/Signup
- **Dashboard:** Overview of transactions and budgets
- **Transaction Management:** Income/Expense forms, transaction list
- **Budget Management:** Budget forms, budget overview
- **Reports:** Generate and download financial reports
- **Graphs:** Visualize trends and categorized expenses
- **Localization:** Multi-language support
- **Settings:** Customize user preferences

### **Backend Components**

- **Authentication:** User registration and login
- **API Endpoints:** CRUD operations for transactions and budgets
- **Transaction Management:** Add, edit, delete, and view transactions
- **Budget Management:** Set, compare, and view budgets
- **Report Generation:** Generate financial reports and export to CSV
- **Graph Data:** Retrieve data for trend and category graphs
- **Localization:** Language data management

---

## **Database Design**

- **Users:** Stores user credentials and preferences
- **Transactions:** Manages user transactions (income/expenses)
- **Budgets:** Tracks user-defined budgets for categories
- **Localization:** Manages multi-language support

---

## **Monitoring and Debugging**

- **Backend Logging:** Python's logging module for backend logs.
- **Frontend Debugging:** Chrome DevTools for monitoring React application.
  
---

### **Future Enhancements**
- **User Notifications:** Real-time budget alerts and notifications.
- **Cloud Integration:** Move from local SQLite to a cloud-based database.
- **Mobile App:** Create a mobile version using React Native.
  
