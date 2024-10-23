import json
import csv
from dotenv import load_dotenv
import os


def lighthouse_json_to_csv(json_path, csv_path):
    # Load the Lighthouse JSON data
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Extract accessibility issues from the report
    accessibility_issues = data['categories']['accessibility']['auditRefs']
    
    # Prepare rows for CSV based on the extracted data
    rows = []
    for issue in accessibility_issues:
        audit_id = issue['id']
        audit_details = data['audits'][audit_id]

        # only select audits with a score of 0 (failed tests)
        if audit_details['score'] == 0:
          # Extract relevant details
          title = audit_details.get('title', 'N/A')
          description = audit_details.get('description', 'N/A')
          
          # Append issue data to rows
          rows.append({
              'id': '',
              'Issue title': title,
              'Component/ Area': 'Test Page',    # to be filled in
              'Comments/Explanation': description,
              'Source': 'Auto evaluation',
              'Affected Elements': audit_id,
              'Identified by': 'Lighthouse',
          })
    
    # Define the CSV columns
    columns = ['id', 'Issue title', 'Component/ Area', 'Comments/Explanation', 'Source', 'Affected Elements', 'Identified by']
    
    # Write the data to a CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

# Load environment variables from .env file
load_dotenv()

# Environment variables
json_path = os.getenv('JSON_PATH')
csv_path = os.getenv('CSV_PATH')

lighthouse_json_to_csv(json_path, csv_path)