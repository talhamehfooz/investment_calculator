import streamlit as st

# Define minimum investment requirements and profit ranges for each plan
investment_plans = {
    "Six months": {"min_investment": 100000, "profit_range": (2.0, 2.2)},
    "One year": {"min_investment": 0, "profit_range": (2.2, 2.6)},
    "Two years": {"min_investment": 2000000, "profit_range": (2.6, 2.9)},
    "Three years": {"min_investment": 5000000, "profit_range": (3.0, 3.3)},
}

def calculate_investment(plan, investment_amount, chosen_profit_rate):
    # Get the number of months for the selected plan
    plan_durations = {
        "Six months": 6,
        "One year": 12,
        "Two years": 24,
        "Three years": 36
    }
    months = plan_durations.get(plan, 0)

    # Calculate the monthly return and total profit
    monthly_return = investment_amount * (chosen_profit_rate / 100)
    total_profit = monthly_return * months
    total_value = investment_amount + total_profit

    # Display results
    st.success(f"**Investment Plan:** {plan}")
    st.write(f"**Investment Amount:** {investment_amount:,.2f} PKR")
    st.write(f"**Chosen Monthly Profit Rate:** {chosen_profit_rate}%")
    st.write(f"**Monthly Return:** {monthly_return:,.2f} PKR")
    st.write(f"**Total Profit Over {months} Months:** {total_profit:,.2f} PKR")
    st.write(f"**Total Value at Maturity:** {total_value:,.2f} PKR")

# Streamlit layout settings
st.title("Investment Calculator")

# Display investment plans
st.subheader("Choose Your Investment Plan")
plan = st.selectbox("Select an investment plan", list(investment_plans.keys()))

# Show plan details based on selection
plan_details = investment_plans[plan]
st.write(f"**Minimum Investment:** {plan_details['min_investment']:,.2f} PKR")
st.write(f"**Profit Range:** {plan_details['profit_range'][0]}% to {plan_details['profit_range'][1]}% per month")

# Investment amount input with validation
investment_amount = st.number_input("Enter your investment amount (in PKR)", min_value=0.0, step=10000.0, format="%f")
if investment_amount < plan_details["min_investment"]:
    st.error(f"Minimum investment for this plan is {plan_details['min_investment']:,.2f} PKR.")

# Chosen profit rate input with validation
chosen_profit_rate = st.number_input("Enter your chosen monthly profit rate (%)", min_value=0.0, step=0.1, format="%f")
if not (plan_details["profit_range"][0] <= chosen_profit_rate <= plan_details["profit_range"][1]):
    st.error(f"Profit rate must be between {plan_details['profit_range'][0]}% and {plan_details['profit_range'][1]}%.")

# Calculate button
if st.button("Calculate") and investment_amount >= plan_details["min_investment"]:
    if plan_details["profit_range"][0] <= chosen_profit_rate <= plan_details["profit_range"][1]:
        calculate_investment(plan, investment_amount, chosen_profit_rate)
    else:
        st.warning("Please enter a valid profit rate within the specified range.")
