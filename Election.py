import csv
import pprint
pp = pprint.PrettyPrinter(indent=4)


""" This function below is the first function which reads 
a csv file and returns the a list of dictionaries as an output  """
def csv_file():
    with open("Results_sheet.csv", "r") as file:
        election_reader = csv.DictReader(file)
        list_of_dict = list(election_reader)  
        for row in list_of_dict:
            row["Hichilema"] = int(row["Hichilema"] )
            row["Lungu"] = int(row["Lungu"] )
            row["Totalvotes"]  = int(row["Totalvotes"] )
            row["Regvoters"]  = int(row["Regvoters"] )
            row["Turnout"]  = int(row["Turnout"] )
            row["UNDP%2021"] =  int(row["UNDP%2021"] )
            row["PF%2021"] =  int(row["PF%2021"])
    return list_of_dict


""" This function is comparing results between Hichilema and Lungu,
 its taking a list of dictionary as an input and returnig a list as an output """
def compare(list_of_data):
    district = []
    for row in list_of_data:
        print(row)
        if int(row["Hichilema"]) > int(row["Lungu"]):
            district.append(row["district"])
    return district


"""" Finding the State with highest value of total voters. 
     Taking list of dict as the input and and returning a dictionary """
def state_with_highest(list_of_dict): 
    max_value = max(list_of_dict, key=lambda x:x['Totalvotes'])
    return max_value 
   

""" This function is sorting the list of dict according to districts in ascending order.
   Taking in a list of dict as input and and list of dict as an output"""
def sort_list(list_of_dict):
    sorted_state = sorted(list_of_dict, key = lambda i: i['district'])
    return sorted_state 


""" This function is filtering the districts that only found in Eastern state
  getting a list of dict as an input and list of dict for eastern state as output """
def filtrating(list_of_dict):
    filtered = []
    for row in list_of_dict:
        filtered =  [row for row in list_of_dict if row['State']=="EASTERN"]
        filtered.append(row["district"])
    return filtered


""" This is the main function where the program starts executing and the above functions are called"""  
if __name__ == '__main__':
    printcompare(csv_file())
    pp.pprint(state_with_highest(csv_file()))
    pp.pprint(get_state(csv_file()))
    pp.pprint(sort_list(csv_file()))
    pp.pprint(filtrating(csv_file()))
