import json
import datetime
import time
from typing import Dict, List


class PersonalFinanceAssistant:
    def __init__(self):
        self.expenses: List[Dict[str, float]] = []
        self.income: List[Dict[str, float]] = []
        self.budget: Dict[str, float] = {}
        self.financial_goals: List[Dict[str, float]] = []

    def track_expense(self, category: str, amount: float):
        expense = {
            "category": category,
            "amount": amount,
            "date": str(datetime.date.today())
        }
        self.expenses.append(expense)

    def track_income(self, source: str, amount: float):
        income = {
            "source": source,
            "amount": amount,
            "date": str(datetime.date.today())
        }
        self.income.append(income)

    def create_budget(self, category: str, allocation: float):
        self.budget[category] = allocation

    def set_financial_goal(self, goal: str, target_amount: float):
        financial_goal = {
            "goal": goal,
            "target_amount": target_amount,
            "current_amount": 0
        }
        self.financial_goals.append(financial_goal)

    def update_financial_goal(self, goal: str, amount: float):
        for financial_goal in self.financial_goals:
            if financial_goal["goal"] == goal:
                financial_goal["current_amount"] += amount
                break

    def analyze_expenses(self) -> Dict[str, float]:
        expense_summary = {}
        for expense in self.expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category in expense_summary:
                expense_summary[category] += amount
            else:
                expense_summary[category] = amount
        return expense_summary

    def analyze_income(self) -> Dict[str, float]:
        income_summary = {}
        for income in self.income:
            source = income["source"]
            amount = income["amount"]
            if source in income_summary:
                income_summary[source] += amount
            else:
                income_summary[source] = amount
        return income_summary

    def generate_financial_report(self) -> Dict[str, any]:
        total_income = sum(income["amount"] for income in self.income)
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        net_worth = total_income - total_expenses

        expense_summary = self.analyze_expenses()

        financial_report = {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_worth": net_worth,
            "expense_summary": expense_summary
        }
        return financial_report

    def generate_financial_report_extended(self) -> Dict[str, any]:
        total_income = sum(income["amount"] for income in self.income)
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        net_worth = total_income - total_expenses

        expense_summary = self.analyze_expenses()
        income_summary = self.analyze_income()

        financial_report = {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_worth": net_worth,
            "expense_summary": expense_summary,
            "income_summary": income_summary
        }
        return financial_report

    def save_data(self):
        data = {
            "expenses": self.expenses,
            "income": self.income,
            "budget": self.budget,
            "financial_goals": self.financial_goals
        }
        with open("data.json", "w") as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                self.expenses = data["expenses"]
                self.income = data["income"]
                self.budget = data["budget"]
                self.financial_goals = data["financial_goals"]
        except FileNotFoundError:
            print("No data file found.")

    def autonomous_assistant(self):
        while True:
            print("\n===== Personal Finance Assistant =====")
            print("1. Track Expense")
            print("2. Track Income")
            print("3. Create Budget")
            print("4. Set Financial Goal")
            print("5. Analyze Expenses")
            print("6. Analyze Income")
            print("7. Generate Financial Report")
            print("8. Save Data")
            print("9. Load Data")
            print("10. Exit")

            choice = input("Enter your choice (1-10): ")

            if choice == "1":
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))
                self.track_expense(category, amount)
                print("Expense tracked successfully!")

            elif choice == "2":
                source = input("Enter income source: ")
                amount = float(input("Enter income amount: "))
                self.track_income(source, amount)
                print("Income tracked successfully!")

            elif choice == "3":
                category = input("Enter budget category: ")
                allocation = float(input("Enter budget allocation: "))
                self.create_budget(category, allocation)
                print("Budget created successfully!")

            elif choice == "4":
                goal = input("Enter financial goal: ")
                target_amount = float(input("Enter target amount: "))
                self.set_financial_goal(goal, target_amount)
                print("Financial goal set successfully!")

            elif choice == "5":
                expense_summary = self.analyze_expenses()
                print("Expense Analysis:")
                for category, amount in expense_summary.items():
                    print(f"{category}: {amount}")

            elif choice == "6":
                income_summary = self.analyze_income()
                print("Income Analysis:")
                for source, amount in income_summary.items():
                    print(f"{source}: {amount}")

            elif choice == "7":
                financial_report = self.generate_financial_report_extended()
                print("Financial Report:")
                print(f"Total Income: {financial_report['total_income']}")
                print(f"Total Expenses: {financial_report['total_expenses']}")
                print(f"Net Worth: {financial_report['net_worth']}")
                print("Expense Summary:")
                for category, amount in financial_report['expense_summary'].items():
                    print(f"{category}: {amount}")
                print("Income Summary:")
                for source, amount in financial_report['income_summary'].items():
                    print(f"{source}: {amount}")

            elif choice == "8":
                self.save_data()
                print("Data saved successfully!")

            elif choice == "9":
                self.load_data()
                print("Data loaded successfully!")

            elif choice == "10":
                break

            else:
                print("Invalid choice. Please try again.")

    def retry_function(self, function, *args, **kwargs):
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                return function(*args, **kwargs)
            except Exception as e:
                print(f"Error: {e}")
                print("Retrying...")
                time.sleep(1)
                attempts += 1
        print("Max attempts reached. Exiting...")
        exit()


class PersonalFinanceAssistantExtended(PersonalFinanceAssistant):
    def __init__(self):
        super().__init__()


class InvestmentAssistant(PersonalFinanceAssistantExtended):
    def __init__(self):
        super().__init__()

    def track_investment(self, investment: str, amount: float):
        investment = {
            "investment": investment,
            "amount": amount,
            "date": str(datetime.date.today())
        }
        self.income.append(investment)

    def analyze_investments(self) -> Dict[str, float]:
        investment_summary = {}
        for investment in self.income:
            investment_name = investment["investment"]
            amount = investment["amount"]
            if investment_name in investment_summary:
                investment_summary[investment_name] += amount
            else:
                investment_summary[investment_name] = amount
        return investment_summary

    def generate_investment_report(self) -> Dict[str, any]:
        total_investments = sum(investment["amount"]
                                for investment in self.income)

        investment_summary = self.analyze_investments()

        investment_report = {
            "total_investments": total_investments,
            "investment_summary": investment_summary
        }
        return investment_report

    def autonomous_assistant_extended(self):
        while True:
            print("\n===== Investment Assistant =====")
            print("1. Track Expense")
            print("2. Track Income")
            print("3. Create Budget")
            print("4. Set Financial Goal")
            print("5. Analyze Expenses")
            print("6. Analyze Income")
            print("7. Generate Financial Report")
            print("8. Analyze Investments")
            print("9. Generate Investment Report")
            print("10. Save Data")
            print("11. Load Data")
            print("12. Exit")

            choice = input("Enter your choice (1-12): ")

            if choice == "1":
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))
                self.track_expense(category, amount)
                print("Expense tracked successfully!")

            elif choice == "2":
                source = input("Enter income source: ")
                amount = float(input("Enter income amount: "))
                self.track_income(source, amount)
                print("Income tracked successfully!")

            elif choice == "3":
                category = input("Enter budget category: ")
                allocation = float(input("Enter budget allocation: "))
                self.create_budget(category, allocation)
                print("Budget created successfully!")

            elif choice == "4":
                goal = input("Enter financial goal: ")
                target_amount = float(input("Enter target amount: "))
                self.set_financial_goal(goal, target_amount)
                print("Financial goal set successfully!")

            elif choice == "5":
                expense_summary = self.analyze_expenses()
                print("Expense Analysis:")
                for category, amount in expense_summary.items():
                    print(f"{category}: {amount}")

            elif choice == "6":
                income_summary = self.analyze_income()
                print("Income Analysis:")
                for source, amount in income_summary.items():
                    print(f"{source}: {amount}")

            elif choice == "7":
                financial_report = self.generate_financial_report_extended()
                print("Financial Report:")
                print(f"Total Income: {financial_report['total_income']}")
                print(f"Total Expenses: {financial_report['total_expenses']}")
                print(f"Net Worth: {financial_report['net_worth']}")
                print("Expense Summary:")
                for category, amount in financial_report['expense_summary'].items():
                    print(f"{category}: {amount}")
                print("Income Summary:")
                for source, amount in financial_report['income_summary'].items():
                    print(f"{source}: {amount}")

            elif choice == "8":
                investment_summary = self.analyze_investments()
                print("Investment Analysis:")
                for investment, amount in investment_summary.items():
                    print(f"{investment}: {amount}")

            elif choice == "9":
                investment_report = self.generate_investment_report()
                print("Investment Report:")
                print(
                    f"Total Investments: {investment_report['total_investments']}")
                print("Investment Summary:")
                for investment, amount in investment_report['investment_summary'].items():
                    print(f"{investment}: {amount}")

            elif choice == "10":
                self.save_data()
                print("Data saved successfully!")

            elif choice == "11":
                self.load_data()
                print("Data loaded successfully!")

            elif choice == "12":
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    ia = InvestmentAssistant()
    ia.retry_function(ia.autonomous_assistant_extended)
