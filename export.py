import reports
# changes
# Export functions

def open_file(file_name):  
    with open(file_name, 'r') as myFile:
        reader = myFile.read()
    return reader

results = [reports.count_games(open_file('game_stat.txt')),reports.decide(open_file('game_stat.txt'),1999),reports.get_latest(open_file('game_stat.txt')),
           reports.count_by_genre(open_file('game_stat.txt'),'First-person shooter'),reports.get_line_number_by_title(open_file('game_stat.txt'),'Counter-Strike'),
           reports.sort_abc(open_file('game_stat.txt')),reports.get_genres(open_file('game_stat.txt')),reports.when_was_top_sold_fps(open_file('game_stat.txt'))]

def export_results(results,file_name):
    with open(file_name, 'w') as file:
        file.writelines(str(i) + '\n' for i in results)

export_results(results,'export_result.txt')