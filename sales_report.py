"""Generate sales report showing total melons each salesperson sold."""

def melon_sales(filename):# set intial values as empty lists
    # use a dictionary 
    melons_sold = {}

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
        # the second entry is the salesperson total
        sp_total = float(entries[1])
        # the third entry is the number of melons sold by that salesperson
        melons = int(entries[2])

        # if the salesperson is already in the list salespeople then find the 
        # index of that salesperson and add to the number of melons sold
        if salesperson in melons_sold:
            melons_sold[salesperson] += melons

        # otherwise add the salesperson's name to the salespeople list 
        # and melons sold to the melons_sold list
        else:
            melons_sold[salesperson] = melons
    return melons_sold        

def print_sales_report(melons_dict):
    for salesperson, melons_sold in melons_dict.items():
        print(f'{salesperson} sold {melons_sold} melons')


# display the list of salespersons and melons sold 
print_sales_report(melon_sales('sales-report.txt'))