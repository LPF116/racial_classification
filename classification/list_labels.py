# Import any libraries here
import csv

# I've set up the skeleton for this script, but you'll need to fill in / replace any TODO line with real code.
# You may also have to import a library for the CSV reader - put that up top.

#-------------------------------------------------------

# Create an empty list. This list will hold all of the labels we find in the label file.
labels = [] # done

# Open the `fairface_original/fairface_label_train.csv` file (in read mode)
with open('fairface_original/fairface_label_train.csv') as f: # TODO
    # Read the file contents as a CSV. (Remember that the first line contains the headers/field names for the file)
    csvreader = csv.reader(f, delimiter=',')
    line_count = 0
    # Loop through all lines in the CSV reader
    for line in csvreader:
        if line_count == 0:
            print("columns are: file,age,gender,race,service_test")
            line_count += 1
        # get the label out of this line
        else:
            label = line[3]
            line_count+= 1
        # # If we see a new label
            if label not in labels:
                labels.append(label)
                #print(labels)


# # After going through the whole file, slightly rename each label to make our lives easier (all lowercase, no spaces)
labels = [label.replace(' ','_') for label in labels]

labels = [label.lower() for label in labels]

#print(labels)


# # Open the `fairface_clean/labels.txt` file (in write mode)
with open('fairface_clean/labels.txt', 'w') as labels_file:
    # Write out the list of labels, one per line.
    for label in labels:
        labels_file.write(label +'\n')
    
    print(labels_file)
        



# # All done!