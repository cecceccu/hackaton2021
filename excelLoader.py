

def load_excel(file_name):
    d = dict()
    f = open("CSV/" + file_name)
    for (i, line) in enumerate(f):
        line = line.strip('\n')
        (date_time, charge, renouvelable) = line.split(",")
        d[i] = {"date_heure": date_time, "charge": charge, "renouvelable": renouvelable}
    return d