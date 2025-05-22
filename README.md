# Automation_playground_crm

# 🚀 CRM Automation Task – Automation Playground

## 🔗 Application URL

[https://automationplayground.com/crm/login.html](https://automationplayground.com/crm/login.html)


## 📌 Project Overview

This automation project is designed to validate key user workflows on the Automation Playground CRM application using the Page Object Model (POM) approach. 
The automation covers logging into the system, adding a new customer, and logging out successfully.


## 🎯 Scope of Automation

The following user flows are automated:

### 1. 🔐 Login Page

* Automates user login using valid credentials.
* Verifies successful login by checking redirection or dashboard element visibility.

### 2. 🏠 Homepage – Add Customer Action

* After login, clicks on the **"Add Customer"** button to open the customer entry form.

### 3. 🧾 Add Customer Form

* Fills out all mandatory fields in the **Add Customer** form with appropriate test data.
* Submits the form and verifies customer addition (confirmation message or page redirection).

### 4. 🔓 Logout Process

* Automates logout process once the customer is successfully added.
* Validates redirection back to the login screen or appropriate logout confirmation.

## 🧱 Project Structure (POM)

📁 automation-playground-crm/
├── 📁 pages/                  # Page Object Classes
│   ├── login_page.py
│   ├── home_page.py
│   └── add_customer_page.py
├── 📁 tests/                  # Test Cases
│   └── test_crm_flow.py
├── 📁 utils/                  # Utilities (e.g., config, data)
│   └── test_data.py
├── conftest.py               # Pytest fixtures and setup
├── requirements.txt          # Dependencies
└── README.md                 # Project Documentation


## 🧪 Technologies & Tools

* Language: Python
* Framework: PyTest 
* Automation Tool: Selenium WebDriver
* Design Pattern: Page Object Model (POM)
Other Tools: WebDriver Manager, ChromeDriver,


## ▶️ How to Run the Tests

1. Clone the Repository

git clone https://github.com/yourusername/automation-playground-crm.git
cd automation-playground-crm


2. Installed Dependencies

pip install -r requirements.txt

3. Run the Tests


pytest 

## ✅ Test Data Example

You can modify/add test data in `utils/test_data.py`:

```python
login_credentials = {
    "username": "testuser",
    "password": "testpass"
}

new_customer = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com", 
}
