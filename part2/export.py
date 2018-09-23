import reports

# Export functions

def open_file(file_name):  
    with open(file_name, 'r') as myFile:
        reader = myFile.read()
    return reader

results = [reports.get_most_played(open_file('game_stat.txt')),reports.sum_sold(open_file('game_stat.txt')),reports.get_selling_avg(open_file('game_stat.txt')),
           reports.count_longest_title(open_file('game_stat.txt')),reports.get_date_avg(open_file('game_stat.txt')),reports.get_name(open_file('game_stat.txt'),'Minecraft'),
           reports.count_grouped_by_genre(open_file('game_stat.txt')),reports.get_date_ordered(open_file('game_stat.txt'))]

def export_results(results,file_name):
    with open(file_name, 'w') as file:
        file.writelines(str(i) + '\n' for i in results)

export_results(results,'export_result2.txt')
