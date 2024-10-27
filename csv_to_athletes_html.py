import csv

def process_athlete_data(file_path):

   # Extracting athlete stats by year
   records = []

   # Extracting athlete races
   races = []           

   athlete_name = ""
   athlete_id = ""
   comments = ""

   with open(file_path, newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      data = list(reader)

      athlete_name = data[0][0]
      athlete_id = data[1][0]
      print(f"The athlete id for {athlete_name} is {athlete_id}")

      for row in data[5:-1]:
         if row[2]:
            records.append({"year": row[2], "sr": row[3]})
         else:
            races.append({
               "finish": row[1],
               "time": row[3],
               "meet": row[5],
               "url": row[6],
               "comments": row[7]
            })

   return {
      "name": athlete_name,
      "athlete_id": athlete_id,
      "season_records": records,
      "race_results": races,
      "comments": comments
   }    

def gen_athlete_page(data, outfile):
    # Start building the HTML structure
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Get your own FontAwesome ID -->
  <script src="https://kit.fontawesome.com/YOUR_ID.js" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">
  <title>{data["name"]}</title>
</head>
<body>
  <a href="#main">Skip to Main Content</a>
  <nav role="navigation" aria-label="Main Navigation">
    <ul>
      <li><a href="../index.html">Home Page</a></li>
    </ul>
  </nav>
  <header>
    <h1>{data["name"]}</h1>
    <img src="../images/profiles/{data["athlete_id"]}.jpg" alt="Headshot of {data["name"]}" width="200"> 
  </header>
  <main id="main">
    <section id="athlete-sr-table">
      <h2>Seasonal Records (SR) per Year</h2>
      <table>
        <thead>
          <tr>
            <th scope="col">Year</th>
            <th scope="col">Season Record (SR)</th>
          </tr>
        </thead>
        <tbody>
'''

    for sr in data["season_records"]:
        sr_row = f'''
          <tr>
            <td data-label="Year">{sr["year"]}</td>
            <td data-label="Season Record (SR)">{sr["sr"]}</td>
          </tr>
        '''
        html_content += sr_row

    html_content += '''
        </tbody>
      </table>
    </section>
    <section id="athlete-result-table">
      <h2>Race Results</h2>
      <table id="athlete-table">
        <thead>
          <tr>
            <th scope="col">Race</th>
            <th scope="col">Athlete Time</th>
            <th scope="col">Athlete Place</th>
            <th scope="col">Race Comments</th>
          </tr>
        </thead>
        <tbody>
'''

    # Add each race as a row into the race table 
    for race in data["race_results"]:
        race_row = f'''
          <tr class="result-row">
            <td data-label="Race">
              <a href="{race["url"]}">{race["meet"]}</a>
            </td>
            <td data-label="Athlete Time">{race["time"]}</td>
            <td data-label="Athlete Place">{race["finish"]}</td>
            <td data-label="Race Comments">{race["comments"]}</td>
          </tr>
        '''
        html_content += race_row

    html_content += '''
        </tbody>
      </table>
    </section>
    <section id="gallery">
      <h2>Gallery</h2>
      <!-- Add images here -->
    </section>
  </main>
  <footer>
    <p>
    Skyline High School<br>
    <address>
    2552 North Maple Road<br>
    Ann Arbor, MI 48103<br><br>
    <a href="https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
    Follow us on Instagram <a href="https://www.instagram.com/a2skylinexc/"><i class="fa-brands fa-instagram" aria-label="Instagram"></i></a>
    </address>
    </p>
  </footer>
</body>
</html>
'''

    with open(outfile, 'w') as output:
        output.write(html_content)

def gen_index_page(mens_athletes, womens_athletes):
    html_content = f'''<!DOCTYPE html>
   <html lang="en">
   <head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Skyline Cross Country Team</title>
   <link rel="stylesheet" href="css/reset.css">
   <link rel="stylesheet" href="css/style.css">
   </head>
   <body>
   <header>
      <h1>Skyline Cross Country Team</h1>
   </header>
   <main>
      <section>
         <h2>Men's Team Athletes</h2>
         <ul>
   '''

    for athlete_data in mens_athletes:
        athlete_name = athlete_data["name"]
        athlete_id = athlete_data["athlete_id"]
        athlete_html = f"mens_team/{athlete_name}{athlete_id}.html"
        html_content += f'        <li><a href="{athlete_html}">{athlete_name}</a></li>\n'

    html_content += '''      </ul>
    </section>
    <section>
      <h2>Women's Team Athletes</h2>
      <ul>
'''

    for athlete_data in womens_athletes:
        athlete_name = athlete_data["name"]
        athlete_id = athlete_data["athlete_id"]
        athlete_html = f"womens_team/{athlete_name}{athlete_id}.html"
        html_content += f'        <li><a href="{athlete_html}">{athlete_name}</a></li>\n'

    html_content += '''      </ul>
    </section>
  </main>
  <footer>
    <p>
    Skyline High School<br>
    <address>
    2552 North Maple Road<br>
    Ann Arbor, MI 48103<br><br>
    <a href="https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
    Follow us on Instagram <a href="https://www.instagram.com/a2skylinexc/"><i class="fa-brands fa-instagram" aria-label="Instagram"></i></a>
    </address>
    </p>
  </footer>
</body>
</html>
'''

    with open('index.html', 'w') as output:
        output.write(html_content)
def main():

   import os
   import glob

   # Define the folder path
   folder_path = 'mens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]
   mens_data = []
   womens_data = []
   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("mens_team/"+file)
      mens_data.append(athlete_data)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "mens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")


   # Define the folder path
   folder_path = 'womens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   for file in csv_file_names:

      # read data from file
      athlete_data = process_athlete_data("womens_team/"+file)
      womens_data.append(athlete_data)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, "womens_team/"+file.replace(".csv",".html"))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")
   
   gen_index_page(mens_athletes=mens_data, womens_athletes=womens_data)
      
if __name__ == '__main__':
    main()
