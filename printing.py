import reports

def open_file(file_name):  
    with open(file_name, 'r') as myFile:
        reader = myFile.read()
    return reader

# Printing functions

def print_results():
    print(reports.count_games(open_file('game_stat.txt')))

    print(reports.decide(open_file('game_stat.txt'),1999))

    print(reports.get_latest(open_file('game_stat.txt')))

    print(reports.count_by_genre(open_file('game_stat.txt'),'First-person shooter'))

    print(reports.get_line_number_by_title(open_file('game_stat.txt'),'Counter-Strike'))

    print(reports.sort_abc(open_file('game_stat.txt')))

    print(reports.get_genres(open_file('game_stat.txt')))

    print(reports.when_was_top_sold_fps(open_file('game_stat.txt')))

print_results()

def get_values_from_prints():
    return print_results()