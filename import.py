import csv

# replace "signups.csv" with filename of csv file from google sheets
with open('signups.csv', 'r') as file:
    reader = csv.DictReader(file)

    with open('parsed.txt', 'w') as parsed:
        writer = csv.writer(parsed)
        for line in reader:
            # use the key from your csv file headings
            crs = line['crsid'].replace("@cam.ac.uk", "").strip().lower() + '@cam.ac.uk'
            writer.writerow([crs])
            
# output will be a list of crsids in one format which can then be inputted to sympa
