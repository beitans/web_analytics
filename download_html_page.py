import datetime
import requests
import pandas as pd
from requests_html import HTML


now = datetime.datetime.now()
year = now.year

def url_to_file(url, filname="world.hmtl", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", "w") as f:
                f.write(html_text)
        return html_text
    return ""

url = "http://adragon202.no-ip.org/Shadowrun/index.php/SR5:Spell_List"

html_text = url_to_file(url)

r_html = HTML(html=html_text)
table_class = "sortable wikitable jquery-tablesorter"
#table_class = "#table"

r_table = r_html.find(table_class)
#print(r_table)
table_data = []
header_names = []
if len(r_table) == 1:
    print(r_table[0].text)
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_row = header_row.find('th')
    header_names = [x.text for x in header_row]
    for row in rows[1:]:
        print(row.text)
        cols= row.find("td")
        row_data = []
        for i, col in enumerate(cols):
            #print(i, col.text, '\n\n')
            row_data.append(col.text)
        table_data.append(row_data)
        
print(header_names)        
print(table_data)

df = pd.DataFrame(table_data, columns = header_names)
df.to_csv('movies.csv', index=False)