📊 Ecommerce Sales Analytics Dashboard (Power BI)
📌 Project Overview

This project showcases an end-to-end Ecommerce Sales Analytics Dashboard built using Power BI with a fact–dimension (star schema) data model.
The dashboard helps analyze sales performance, customer behavior, product trends, and payment method insights through interactive visuals and DAX-driven KPIs.

🛠 Tools & Technologies

Power BI

MySQL (Data Source)

DAX (Data Analysis Expressions)

SQL

Data Modeling (Fact & Dimension Tables)

🗂 Data Model

The project follows a star schema design:

Fact Table

fact_sales_final

Sales Amount

Transaction ID

Date ID

Product ID

Customer ID

Payment ID

Dimension Tables

dim_customer (Age, Age Group, Country)

dim_product (Product Category)

dim_date (Year, Month, Date)

dim_payment (Payment Method)

📈 Key KPIs

Total Sales

Total Customers

Total Transactions

Average Order Value (AOV)

📊 Dashboard Pages
🔹 Page 1: Sales Overview

Total Sales, Customers, Transactions, AOV

Sales by Product Category

Sales by Country

Monthly Sales Trend (YoY)

Transactions by Payment Method

Interactive slicers (Year, Month, Product Category, Country)

🔹 Page 2: Customer & Payment Insights

Customers by Age Group

Average Order Value by Product Category

Average Order Value by Country

Customers by Payment Method

AOV by Payment Method

🧮 DAX Measures Used
Total Sales = SUM(fact_sales_final[sales_amount])

Total Customers = DISTINCTCOUNT(fact_sales_final[customer_id])

Total Transactions = COUNT(fact_sales_final[transaction_id])

Average Order Value = DIVIDE([Total Sales], [Total Transactions])

🎯 Key Insights

Identified top-performing product categories and countries

Analyzed customer purchasing behavior by age group

Compared payment methods based on transactions and AOV

Tracked monthly and yearly sales trends

🚀 How to Use

Open the .pbix file in Power BI Desktop

Refresh data (MySQL connection required)

Use slicers to interact with the dashboard

📌 Future Enhancements

Add profit & margin analysis

Customer retention & repeat purchase metrics

Drill-through pages for product-level insights

Power BI Service publishing with scheduled refresh
