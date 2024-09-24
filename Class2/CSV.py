import csv

# Step 1: Create a dataset
data = [
    {"ID": 123456, "Name": "Yaoyang", "Age": 24},
    {"ID": 123457, "Name": "Li", "Age": 25},
    {"ID": 123458, "Name": "Lily", "Age": 18},
    {"ID": 123458, "Name": "Bill", "Age": 37},
    {"ID": 123459, "Name": "Helen", "Age": 30}]
# Step 2: Write the dataset to output.csv
output_file = 'output.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["ID", "Name", "Age"])
    writer.writeheader(data)
    writer.writerows(data)
# Step 3: Open output.csv to read the data
with open(output_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # Step 4: Create a loop to read and store rows
    rows = [row for row in reader]
# Step 5: Use a loop to sort rows by the "Age" column
for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        if int(rows[i]["Age"]) > int(rows[j]["Age"]):
            # Swap rows
            rows[i], rows[j] = rows[j], rows[i]
# Step 6: Write the sorted rows to a new CSV file
sorted_output_file = 'sorted_output.csv'
with open(sorted_output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["ID", "Name", "Age"])
    writer.writeheader(rows)
    writer.writerows(rows)
print(f"Sorted data written to {sorted_output_file}")





