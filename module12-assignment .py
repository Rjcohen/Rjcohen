# Module 12 Assignment: Business Analytics Fundamentals and Applications
# GreenGrocer Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("=" * 60)
print("GREENGROCER BUSINESS ANALYTICS")
print("=" * 60)

np.random.seed(42)

stores = ["Tampa", "Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000, 8000],
    "StaffCount": [45, 35, 55, 30, 25],
    "YearsOpen": [5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000, 3000, 1800, 1500]
}

store_df = pd.DataFrame(store_data)

departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits", "Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"],
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}

sales_data = []
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

store_performance = {
    "Tampa": 1.0,
    "Orlando": 0.85,
    "Miami": 1.2,
    "Jacksonville": 0.75,
    "Gainesville": 0.65
}

dept_performance = {
    "Produce": 1.2,
    "Dairy": 1.0,
    "Bakery": 0.85,
    "Grocery": 0.95,
    "Prepared Foods": 1.1
}

for date in dates:
    month = date.month
    seasonal_factor = 1.0

    if month in [6, 7, 8]:
        seasonal_factor = 1.15
    elif month == 12:
        seasonal_factor = 1.25
    elif month in [1, 2]:
        seasonal_factor = 0.9

    dow_factor = 1.3 if date.dayofweek >= 5 else 1.0

    for store in stores:
        for dept in departments:
            for category in categories[dept]:
                base_sales = np.random.normal(loc=500, scale=100)

                sales_amount = (
                    base_sales
                    * store_performance[store]
                    * dept_performance[dept]
                    * seasonal_factor
                    * dow_factor
                )

                sales_amount *= np.random.normal(loc=1.0, scale=0.1)

                base_margin = {
                    "Produce": 0.25,
                    "Dairy": 0.22,
                    "Bakery": 0.35,
                    "Grocery": 0.20,
                    "Prepared Foods": 0.40
                }[dept]

                profit_margin = base_margin * np.random.normal(loc=1.0, scale=0.05)
                profit_margin = max(min(profit_margin, 0.5), 0.15)
                profit = sales_amount * profit_margin

                sales_data.append({
                    "Date": date,
                    "Store": store,
                    "Department": dept,
                    "Category": category,
                    "Sales": round(sales_amount, 2),
                    "ProfitMargin": round(profit_margin, 4),
                    "Profit": round(profit, 2)
                })

sales_df = pd.DataFrame(sales_data)

customer_data = []
total_customers = 5000

segments = [
    "Health Enthusiast",
    "Gourmet Cook",
    "Family Shopper",
    "Budget Organic",
    "Occasional Visitor"
]

segment_probabilities = [0.25, 0.20, 0.30, 0.15, 0.10]

store_probs = {
    "Tampa": 0.25,
    "Orlando": 0.20,
    "Miami": 0.30,
    "Jacksonville": 0.15,
    "Gainesville": 0.10
}

for i in range(total_customers):
    age = int(np.random.normal(loc=42, scale=15))
    age = max(min(age, 85), 18)

    gender = np.random.choice(["M", "F"], p=[0.48, 0.52])

    income = int(np.random.normal(loc=85, scale=30))
    income = max(income, 20)

    segment = np.random.choice(segments, p=segment_probabilities)
    preferred_store = np.random.choice(stores, p=list(store_probs.values()))

    if segment == "Health Enthusiast":
        visit_frequency = np.random.randint(8, 15)
        avg_basket = np.random.normal(loc=75, scale=15)
    elif segment == "Gourmet Cook":
        visit_frequency = np.random.randint(4, 10)
        avg_basket = np.random.normal(loc=120, scale=25)
    elif segment == "Family Shopper":
        visit_frequency = np.random.randint(5, 12)
        avg_basket = np.random.normal(loc=150, scale=30)
    elif segment == "Budget Organic":
        visit_frequency = np.random.randint(6, 10)
        avg_basket = np.random.normal(loc=60, scale=10)
    else:
        visit_frequency = np.random.randint(1, 5)
        avg_basket = np.random.normal(loc=45, scale=15)

    visit_frequency = max(min(visit_frequency, 30), 1)
    avg_basket = max(avg_basket, 15)

    monthly_spend = visit_frequency * avg_basket

    if monthly_spend > 1000:
        loyalty_tier = "Platinum"
    elif monthly_spend > 500:
        loyalty_tier = "Gold"
    elif monthly_spend > 200:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"

    customer_data.append({
        "CustomerID": f"C{i+1:04d}",
        "Age": age,
        "Gender": gender,
        "Income": income * 1000,
        "Segment": segment,
        "PreferredStore": preferred_store,
        "VisitsPerMonth": visit_frequency,
        "AvgBasketSize": round(avg_basket, 2),
        "MonthlySpend": round(monthly_spend, 2),
        "LoyaltyTier": loyalty_tier
    })

customer_df = pd.DataFrame(customer_data)

operational_data = []

for store in stores:
    store_row = store_df[store_df["Store"] == store].iloc[0]
    square_footage = store_row["SquareFootage"]
    staff_count = store_row["StaffCount"]

    store_sales = sales_df[sales_df["Store"] == store]["Sales"].sum()
    store_profit = sales_df[sales_df["Store"] == store]["Profit"].sum()

    sales_per_sqft = store_sales / square_footage
    profit_per_sqft = store_profit / square_footage
    sales_per_staff = store_sales / staff_count
    inventory_turnover = np.random.uniform(12, 18) * store_performance[store]
    customer_satisfaction = min(
        5,
        np.random.normal(loc=4.0, scale=0.3) * (store_performance[store] ** 0.5)
    )

    operational_data.append({
        "Store": store,
        "AnnualSales": round(store_sales, 2),
        "AnnualProfit": round(store_profit, 2),
        "SalesPerSqFt": round(sales_per_sqft, 2),
        "ProfitPerSqFt": round(profit_per_sqft, 2),
        "SalesPerStaff": round(sales_per_staff, 2),
        "InventoryTurnover": round(inventory_turnover, 2),
        "CustomerSatisfaction": round(customer_satisfaction, 2)
    })

operational_df = pd.DataFrame(operational_data)


def analyze_sales_performance():
    total_sales = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    avg_profit_margin = sales_df["ProfitMargin"].mean()
    sales_by_store = sales_df.groupby("Store")["Sales"].sum()
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum()

    return {
        "total_sales": float(total_sales),
        "total_profit": float(total_profit),
        "avg_profit_margin": float(avg_profit_margin),
        "sales_by_store": sales_by_store,
        "sales_by_dept": sales_by_dept
    }


def visualize_sales_distribution():
    store_fig, ax1 = plt.subplots()
    sales_df.groupby("Store")["Sales"].sum().plot(kind="bar", ax=ax1)
    ax1.set_title("Sales by Store")
    ax1.set_xlabel("Store")
    ax1.set_ylabel("Sales")

    dept_fig, ax2 = plt.subplots()
    sales_df.groupby("Department")["Sales"].sum().plot(kind="bar", ax=ax2)
    ax2.set_title("Sales by Department")
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Sales")

    time_fig, ax3 = plt.subplots()
    sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum().plot(
        kind="line",
        marker="o",
        ax=ax3
    )
    ax3.set_title("Monthly Sales")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Sales")

    return store_fig, dept_fig, time_fig


def analyze_customer_segments():
    segment_counts = customer_df["Segment"].value_counts()
    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean()
    segment_loyalty = pd.crosstab(customer_df["Segment"], customer_df["LoyaltyTier"])

    return {
        "segment_counts": segment_counts,
        "segment_avg_spend": segment_avg_spend,
        "segment_loyalty": segment_loyalty
    }


def analyze_sales_correlations():
    store_metrics = pd.merge(store_df, operational_df, on="Store")
    numeric_data = store_metrics.select_dtypes(include=[np.number])
    store_correlations = numeric_data.corr()

    correlations = store_correlations["AnnualSales"].drop("AnnualSales").sort_values(ascending=False)
    top_correlations = list(correlations.items())[:5]

    correlation_fig, ax = plt.subplots()
    ax.imshow(store_correlations)
    ax.set_title("Store Metrics Correlation Matrix")
    ax.set_xticks(range(len(store_correlations.columns)))
    ax.set_yticks(range(len(store_correlations.columns)))
    ax.set_xticklabels(store_correlations.columns, rotation=90)
    ax.set_yticklabels(store_correlations.columns)

    return {
        "store_correlations": store_correlations,
        "top_correlations": top_correlations,
        "correlation_fig": correlation_fig
    }


def compare_store_performance():
    efficiency_metrics = operational_df[["Store", "SalesPerSqFt", "SalesPerStaff"]].set_index("Store")
    performance_ranking = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)

    comparison_fig, ax = plt.subplots()
    efficiency_metrics.plot(kind="bar", ax=ax)
    ax.set_title("Store Efficiency Comparison")
    ax.set_xlabel("Store")
    ax.set_ylabel("Metric Value")

    return {
        "efficiency_metrics": efficiency_metrics,
        "performance_ranking": performance_ranking,
        "comparison_fig": comparison_fig
    }


def analyze_seasonal_patterns():
    monthly_sales = sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum()
    dow_sales = sales_df.groupby(sales_df["Date"].dt.day_name())["Sales"].sum()

    seasonal_fig, ax = plt.subplots()
    monthly_sales.plot(kind="line", marker="o", ax=ax)
    ax.set_title("Seasonal Monthly Sales Pattern")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")

    return {
        "monthly_sales": monthly_sales,
        "dow_sales": dow_sales,
        "seasonal_fig": seasonal_fig
    }


def predict_store_sales():
    model_data = pd.merge(store_df, operational_df, on="Store")

    x = model_data[["SquareFootage", "StaffCount", "WeeklyMarketingSpend"]]
    y = model_data["AnnualSales"]

    x_matrix = np.column_stack([np.ones(len(x)), x])
    coefficients_array = np.linalg.lstsq(x_matrix, y, rcond=None)[0]

    predicted_values = x_matrix @ coefficients_array

    ss_total = np.sum((y - y.mean()) ** 2)
    ss_residual = np.sum((y - predicted_values) ** 2)
    r_squared = 1 - (ss_residual / ss_total)

    coefficients = {
        "Intercept": coefficients_array[0],
        "SquareFootage": coefficients_array[1],
        "StaffCount": coefficients_array[2],
        "WeeklyMarketingSpend": coefficients_array[3]
    }

    predictions = pd.Series(predicted_values, index=model_data["Store"])

    model_fig, ax = plt.subplots()
    ax.scatter(y, predictions)
    ax.set_title("Actual vs Predicted Store Sales")
    ax.set_xlabel("Actual Sales")
    ax.set_ylabel("Predicted Sales")

    return {
        "coefficients": coefficients,
        "r_squared": float(r_squared),
        "predictions": predictions,
        "model_fig": model_fig
    }


def forecast_department_sales():
    sales_copy = sales_df.copy()
    sales_copy["Month"] = sales_copy["Date"].dt.month

    dept_trends = sales_copy.groupby(["Month", "Department"])["Sales"].sum().unstack()
    growth_rates = dept_trends.pct_change().mean()

    forecast_fig, ax = plt.subplots()
    dept_trends.plot(ax=ax)
    ax.set_title("Department Sales Trends")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")

    return {
        "dept_trends": dept_trends,
        "growth_rates": growth_rates,
        "forecast_fig": forecast_fig
    }


def identify_profit_opportunities():
    combo = sales_df.groupby(["Store", "Department"])["Profit"].sum().reset_index()

    top_combinations = combo.sort_values("Profit", ascending=False).head(10)
    underperforming = combo.sort_values("Profit", ascending=True).head(10)
    opportunity_score = combo.groupby("Store")["Profit"].sum().sort_values(ascending=False)

    return {
        "top_combinations": top_combinations,
        "underperforming": underperforming,
        "opportunity_score": opportunity_score
    }


def develop_recommendations():
    return [
        "Increase marketing support for Miami because it produces the highest overall sales and profit.",
        "Improve Gainesville performance by reviewing staffing, marketing spend, and store operations.",
        "Focus on Prepared Foods because it has strong profit margins and can improve profitability.",
        "Run more weekend promotions because weekend sales are higher than weekday sales.",
        "Target Family Shopper and Gourmet Cook customers because they tend to have larger basket sizes."
    ]


def generate_executive_summary():
    print("\nOverview:")
    print("GreenGrocer has strong overall performance, but results vary by store, department, and customer segment.")

    print("\nKey Findings:")
    print("- Miami is the strongest overall store.")
    print("- Gainesville is one of the weaker stores and has room for improvement.")
    print("- Prepared Foods is one of the most profitable departments.")
    print("- Sales increase during weekends and stronger seasonal months.")
    print("- Customer segments with larger baskets create major revenue opportunities.")

    print("\nRecommendations:")
    print("- Increase investment in high-performing locations.")
    print("- Improve operations in lower-performing stores.")
    print("- Promote high-margin departments.")
    print("- Use weekend and seasonal promotions.")
    print("- Target high-value customer segments.")

    print("\nExpected Impact:")
    print("These changes should help GreenGrocer increase sales, improve profit margins, and make better business decisions.")


def main():
    print("\n" + "=" * 60)
    print("GREENGROCER BUSINESS ANALYTICS RESULTS")
    print("=" * 60)

    print("\n--- DESCRIPTIVE ANALYTICS: CURRENT PERFORMANCE ---")
    sales_metrics = analyze_sales_performance()
    dist_figs = visualize_sales_distribution()
    customer_analysis = analyze_customer_segments()

    print("\n--- DIAGNOSTIC ANALYTICS: UNDERSTANDING RELATIONSHIPS ---")
    correlations = analyze_sales_correlations()
    store_comparison = compare_store_performance()
    seasonality = analyze_seasonal_patterns()

    print("\n--- PREDICTIVE ANALYTICS: FORECASTING ---")
    sales_model = predict_store_sales()
    dept_forecast = forecast_department_sales()

    print("\n--- BUSINESS INSIGHTS AND RECOMMENDATIONS ---")
    opportunities = identify_profit_opportunities()
    recommendations = develop_recommendations()

    print("\n--- EXECUTIVE SUMMARY ---")
    generate_executive_summary()

    plt.show()

    return {
        "sales_metrics": sales_metrics,
        "customer_analysis": customer_analysis,
        "correlations": correlations,
        "store_comparison": store_comparison,
        "seasonality": seasonality,
        "sales_model": sales_model,
        "dept_forecast": dept_forecast,
        "opportunities": opportunities,
        "recommendations": recommendations
    }


if __name__ == "__main__":
    results = main()
