import streamlit as st

# Define minimum investment requirements and profit ranges for each plan
investment_plans = {
    "Six months": {"min_investment": 100000, "profit_range": (2.0, 2.2)},
    "One year": {"min_investment": 0, "profit_range": (2.2, 2.6)},
    "Two years": {"min_investment": 2000000, "profit_range": (2.6, 2.9)},
    "Three years": {"min_investment": 5000000, "profit_range": (3.0, 3.3)},
}

# Investment plan duration in months
plan_durations = {
    "Six months": 6,
    "One year": 12,
    "Two years": 24,
    "Three years": 36
}

def calculate_investment(plan, investment_amount, chosen_profit_rate):
    months = plan_durations.get(plan, 0)
    monthly_return = investment_amount * (chosen_profit_rate / 100)
    total_profit = monthly_return * months
    total_value = investment_amount + total_profit

    st.success(f"**Investment Plan:** {plan}")
    st.write(f"**Investment Amount:** {investment_amount:,.2f} PKR")
    st.write(f"**Chosen Monthly Profit Rate:** {chosen_profit_rate}%")
    st.write(f"**Monthly Return:** {monthly_return:,.2f} PKR")
    st.write(f"**Total Profit Over {months} Months:** {total_profit:,.2f} PKR")
    st.write(f"**Total Value at Maturity:** {total_value:,.2f} PKR")

# Streamlit layout settings
st.title("Investment Calculator")

# Function to reset the input fields by clearing session state
def reset_calculation():
    st.session_state["plan"] = list(investment_plans.keys())[0]
    st.session_state["investment_amount"] = 0.0
    st.session_state["chosen_profit_rate"] = investment_plans[st.session_state["plan"]]["profit_range"][0]

# Step 1: Choose investment plan
st.subheader("Step 1: Choose Your Investment Plan")
plan = st.selectbox("Select an investment plan", list(investment_plans.keys()), key="plan")

# Display minimum investment and profit range for selected plan
plan_details = investment_plans[plan]
st.write(f"**Minimum Investment:** {plan_details['min_investment']:,.2f} PKR")
st.write(f"**Profit Range:** {plan_details['profit_range'][0]}% to {plan_details['profit_range'][1]}% per month")

# Step 2: Enter investment amount with validation
st.subheader("Step 2: Enter Investment Amount")
investment_amount = st.number_input("Enter your investment amount (in PKR)", min_value=0.0, step=10000.0, format="%f", key="investment_amount")
if investment_amount < plan_details["min_investment"]:
    st.error(f"Minimum investment for this plan is {plan_details['min_investment']:,.2f} PKR.")

# Step 3: Choose profit rate within allowed range using a slider
st.subheader("Step 3: Select Profit Rate (%)")
chosen_profit_rate = st.slider("Choose your monthly profit rate", 
                               min_value=plan_details['profit_range'][0], 
                               max_value=plan_details['profit_range'][1], 
                               step=0.1, key="chosen_profit_rate")

# Step 4: Calculate and display results if inputs are valid
st.subheader("Step 4: Calculate Results")
if st.button("Calculate") and investment_amount >= plan_details["min_investment"]:
    calculate_investment(plan, investment_amount, chosen_profit_rate)

# Step 5: Additional Actions
st.subheader("Step 5: Additional Actions")
col1, col2, col3 = st.columns(3)

# Action buttons
with col1:
    if st.button("Save as PDF"):
        st.write("PDF feature coming soon!")  # Placeholder for PDF generation functionality
with col2:
    if st.button("Email Results"):
        st.write("Email feature coming soon!")  # Placeholder for email functionality
with col3:
    if st.button("Start New Calculation"):
        reset_calculation()  # Resets the input fields


