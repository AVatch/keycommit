import csv


def load_csv(f):
    with open(f, 'rb') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_key_value_pairs = {}
        for row in csv_reader:
            csv_key_value_pairs[row[0]] = row[1]

        return csv_key_value_pairs

if __name__=="__main__":
    # print load_csv('../data/assignment_operators.csv')
    pass