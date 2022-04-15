import array_dispose

def main(path):
    if str(path[-3:]) == "txt":
        array_dispose.read_txt(path)
    elif str(path[-3:]) == "csv":
        array_dispose.read_csv(path)
    elif str(path[-3:]) == "xls":
        array_dispose.read_xls(path)
    elif str(path[-3:]) == "xlsx":
        array_dispose.read_xlsx(path)
    elif str(path[-3:]) == "son":
        array_dispose.read_json(path)

if __name__ == '__main__':
    path = "../data/ahc_txt.txt"

    # path_csv = "./data/datas.csv"
    # path_json = "./data/data.json"
    #
    # path_xls = "./data/data.xls"
    # path_xlsx = "./data/data.xlsx"

    # array_dispose.read_txt(path)
    main(path)