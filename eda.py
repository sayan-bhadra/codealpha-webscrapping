import pandas as pd

# 1. Load the data
df = pd.read_csv("books_data.csv")

print("=== FIRST 5 ROWS ===")
print(df.head(), "\n")

print("=== SHAPE (rows, columns) ===")
print(df.shape, "\n")

print("=== DATA TYPES ===")
print(df.dtypes, "\n")

# 2. Clean the price column: keep only digits and the dot, then make it a number
df["price"] = df["price"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

# 3. Check for data problems
print("=== MISSING VALUES ===")
print(df.isnull().sum(), "\n")

print("=== DUPLICATE ROWS ===")
print(df.duplicated().sum(), "\n")

# 4. Summary statistics
print("=== PRICE SUMMARY ===")
print(df["price"].describe(), "\n")

# 5. Answer questions about the data
print("=== BOOKS PER RATING ===")
print(df["rating"].value_counts().sort_index(), "\n")

print("=== AVERAGE PRICE BY RATING ===")
print(df.groupby("rating")["price"].mean().round(2), "\n")

print("=== TOP 5 MOST EXPENSIVE BOOKS ===")
print(df.nlargest(5, "price")[["title", "price", "rating"]], "\n")

print("=== TOP 5 CHEAPEST BOOKS ===")
print(df.nsmallest(5, "price")[["title", "price", "rating"]], "\n")

# 6. Save the cleaned data for the visualization task
df.to_csv("books_clean.csv", index=False)
print("Cleaned data saved to books_clean.csv")
