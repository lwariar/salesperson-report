"""Generate sales report showing total melons each salesperson sold."""

# set intial values as empty lists
salespeople = []
melons_sold = []

# open the file 'sales-report.txt'
f = open('sales-report.txt')
# loop through each line in the file f to get the salesperson's info 
for line in f:
    # remove trailing white spaces
    line = line.rstrip() 
    # store the data separated by | in a list
    entries = line.split('|')

    # the first entry is the salesperson's name
    salesperson = entries[0]
    # the third entry is the number of melons sold by that salesperson
    melons = int(entries[2])

    # if the salesperson is already in the list salespeople then find the 
    # index of that salesperson and add to the number of melons sold
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
        
    # otherwise add the salesperson's name to the salespeople list 
    # and melons sold to the melons_sold list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# display the list of salespersons and melons sold 
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
