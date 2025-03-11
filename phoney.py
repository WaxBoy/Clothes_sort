import pandas as pd

print(pd.__version__)

# Create a dictionary containing our phone usage data
phone_data = {
    "Usage Range": ["0-1 hours", "1-3 hours", "3-5 hours", "5-7 hours", 
                   "7-9 hours", "9-11 hours", "11+ hours"],
    "Number of Students": [0, 2, 3, 2, 3, 0, 1]  # Example values - we'll update with our real data
}

# Convert this dictionary to a DataFrame
df = pd.DataFrame(phone_data)

# Display the DataFrame
print(df)

# Get summary statistics
print("\nSummary Statistics:")
print(df["Number of Students"].describe())

# Find the most common usage range
most_common_index = df["Number of Students"].idxmax()
print(f"\nMost common phone usage: {df['Usage Range'][most_common_index]} "
      f"with {df['Number of Students'][most_common_index]} students")

# Calculate the total number of students
total_students = df["Number of Students"].sum()
print(f"\nTotal number of students: {total_students}")

# Create a simple text-based bar chart
print("\nText-Based Bar Chart:")

# Prepare the data for the chart (ensuring all usage ranges are the same length)
max_length = max(len(row['Usage Range']) for i,row in df.iterrows())

# Print the chart
for i, row in df.iterrows():
    print(f"{row['Usage Range'].rjust(max_length)}: {'#' * row['Number of Students']}")