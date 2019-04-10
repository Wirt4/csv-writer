"""
*******************************************************
Happy csv file writer
takes in a text file and writes it to a csv
******************
"""

def trim_string(the_string, sub):
    if the_string.endswith(sub):
        return the_string[:-len(sub)]
    else:
        return the_string

def make_2D_array(raw_text, headers, delimeter):
#makes a 2D array from a chunk of raw text, assumes consistency with headers and delimeter
    output_array = []
    cleaned_cells = []
    pre_split_rows = raw_text.split(headers[0]+delimeter)
    for row in pre_split_rows:
        cells = row.split(delimeter)
        for cell in cells:
          for name in headers:
            if cell.endswith(name):
              clean_cell = trim_string(cell, name);
              cleaned_cells.append(clean_cell)
        output_array.append(cleaned_cells)
        cleaned_cells = []
    return output_array


def main():
    from csv import reader, writer
    
    in_file_name = input("Input file: ")+".txt"
    out_file_name =input("Output file: ")+".csv"
    
    in_file_txt = open(in_file_name, "r")
    out_file_csv = open(out_file_name, "w")
    w = writer(out_file_csv)

    header = ["Title",
              "Type",
              "Session",
              "Center",
              "Building",
              "Room",
              "Description",
              "Computer/Software Skills",
              "Technical Skills",
              "Other Skills",
              "Academic Levels",
              "Majors"
              "Mission directorate(s) directly benefiting from the tasks involved in this internship"]
    w.writerow(header)
    
    raw_text = ""
   
    for line in in_file_txt:
        #removing empty lines
        raw_text += line.strip()+""
    split_rows = make_2D_array(raw_text, header, ":")
    
    for row in split_rows:
        w.writerow(row)
 
    in_file_txt.close()
    out_file_csv.close()
    print(".csv created")
    
main()
          
          
          
          
