import json
import csv
from datetime import datetime, timedelta


post_number = 3

# Input and output file paths
input_file = 'all-posts.json'
output_json_file = f"comments_number_{post_number}.json"
output_csv_file = f"comments_number_{post_number}.csv"

# Read the JSON file
with open(input_file, 'r') as file:
    data = json.load(file)

# Extract the comments field from the object with "number" == post_number
comments = []
for item in data:
    if item.get("number") == post_number:
        comments = item.get("comments", [])
        break

# Write the comments to a new JSON file
with open(output_json_file, 'w') as file:
    json.dump(comments, file, indent=4)

print(f"Comments for 'number' == post_number have been written to {output_json_file}")


# Input and output file paths

# Load the JSON data
with open(output_json_file, 'r') as f:
    data = json.load(f)
    # Function to escape line breaks in text
    def escape_line_breaks(text):
        return text.replace('\n', '\\n')

    # Apply escaping to all text fields in the comments
    for comment in data:
        comment['text'] = escape_line_breaks(comment['text'])
        # Convert the created_at timestamp from GMT+11 to GMT-7 (Pacific Daylight Time)
        created_at = comment['created_at']
        try:
            gmt_plus_11 = datetime.strptime(created_at[0:19], '%Y-%m-%dT%H:%M:%S')
        except ValueError as e:
            raise ValueError(f"Error parsing 'created_at': {created_at}. Ensure it matches the format '%Y-%m-%dT%H:%M:%S'. Original error: {e}")
        pacific_time = gmt_plus_11 - timedelta(hours=18)  # Difference between GMT+11 and GMT-7 is 18 hours
        comment['created_at'] = pacific_time.strftime('%Y-%m-%dT%H:%M:%S')
# Extract the comments
comments = data

# Write to CSV
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # Write the header
    csvwriter.writerow(['name', 'email', 'created_at', 'text'])
    
    # Write the rows
    for comment in comments:
        name = comment['user']['name']
        email = comment['user']['email']
        created_at = comment['created_at']
        text = comment['text']
        csvwriter.writerow([name, email, created_at, text])

print(f"Data has been exported to {output_csv_file}")

