import reports

def open_file(file_name):  
    with open(file_name, 'r') as myFile:
        reader = myFile.read()
    return reader

# Printing functions

def print_results():
    print(reports.get_most_played(open_file('game_stat.txt')))

    print(reports.sum_sold(open_file('game_stat.txt')))

    print(reports.get_selling_avg(open_file('game_stat.txt')))

    print(reports.count_longest_title(open_file('game_stat.txt')))

    print(reports.get_date_avg(open_file('game_stat.txt')))

    print(reports.get_name(open_file('game_stat.txt'),'Minecraft'))

    print(reports.count_grouped_by_genre(open_file('game_stat.txt')))

    print(reports.get_date_ordered(open_file('game_stat.txt')))

print_results()

def get_values_from_prints():
    return print_results()
