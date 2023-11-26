from bs4 import BeautifulSoup
import requests 
import csv
import winsound
import sys

##Define vars
id_Table=[]
titles_Table=[]
surnames_Table=[]
other_names_Table=[]
program_Table=[]
program_options_Table=[]
std_type_Table=[]


#Column per column
#APPNO,TITLES,SURNAMES,OTHER_NAMES,PROGRAM,PROGRAM_OPTIONS,STD_TYPE



def get_data(soup):
    ids = soup.find_all('span', {'class': 'gradlistgh_APPNO'})
    for span in ids:
        id_Table.append(span.text.strip())

    titles = soup.find_all('span', {'class': 'gradlistgh_TITLE'})
    for span in titles:
        titles_Table.append(span.text.strip())

    surnames = soup.find_all('span', {'class': 'gradlistgh_SURNAME'})
    for span in surnames:
        surnames_Table.append(span.text.strip())

    other_names = soup.find_all('span', {'class': 'gradlistgh_OTHERNAMES'})
    for span in other_names:
        other_names_Table.append(span.text.strip())

    program = soup.find_all('span', {'class': 'gradlistgh_PROG'})
    for span in program:
        program_Table.append(span.text.strip())

    program_options = soup.find_all('span', {'class': 'gradlistgh_SUBJECTSFULL'})
    for span in program_options:
        program_options_Table.append(span.text.strip())

    std_type = soup.find_all('span', {'class': 'gradlistgh_TYPED'})
    for span in std_type:
        std_type_Table.append(span.text.strip())

    return(id_Table,titles_Table,surnames_Table,other_names_Table,program_Table,program_options_Table,std_type_Table)
    

def main(website):
    pts = requests.get("https://admission.ug.edu.gh/ugadmitted/gradlistghlist.php?pageno="+str(website))
    if pts.status_code != 200:
        print("REQUEST FAILED")
        winsound.PlaySound('ding.wav', winsound.SND_FILENAME)
    soup = BeautifulSoup(pts.text, "html.parser")
    get_data(soup=soup)

for i in range(0,34,1):
    main(i)
    print(i," page out of 34")



def convert_to_csv():
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(id_Table)
        writer.writerow(titles_Table)
        writer.writerow(surnames_Table)
        writer.writerow(other_names_Table)
        writer.writerow(program_Table)
        writer.writerow(program_options_Table)
        writer.writerow(std_type_Table)
convert_to_csv()



# read_file = pandas.read_csv ('data.csv')
# read_file.to_excel ('Data.xlsx', index = None, header=True)

# file = open("scrapped_items.csv", "w")
# writer = csv.writer(file)

# writer.writerow(["APPNO","TITLES","SURNAMES","OTHER_NAMES","PROGRAM","PROGRAM_OPTIONS","STD_TYPE"])

