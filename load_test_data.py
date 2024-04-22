import argparse
import csv
from datetime import datetime
from google.cloud import ndb
from models.note import Note
from models.user import User

# Initialize NDB client

client = ndb.Client()

parser = argparse.ArgumentParser()
parser.add_argument('csv_file', help='Path to CSV file containing note data.')
args = parser.parse_args()

#

with client.context():
    user = User(display_name='Will')
    user.put()
    with open(args.csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # Skip the header row
        next(reader)
        
        for row in reader:
            print(row)
            created_at = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S.%f')
            note = Note(
                id=row[0],
                title=row[1],
                comment=row[2],
                snippet=row[3],
                url=row[4],
                created=created_at,
                user=user
            )
            note.put()
