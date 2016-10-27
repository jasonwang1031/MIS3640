ximport os
'''
fout = open('output.txt','w')

line_1 = 'How many roads does a man walk down\d'

fout.write(line_1)

line_2 = 'Before you call'

fout.write(line_2)

def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    file_in = open(source,'r')
    f_out = open(dest,'w')

    for line in file_in:
        new_line = line.replace(pattern,replace)
        new_line = 
        f_out.write(new_line)

    file_in.close()
    f_out.close()


def main():
    pattern = 'Hey Jude'
    replace = 'Hi Jerry'
    source = 'sed_tester.txt'
    dest = 'new_' + source
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()

#def walk2(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    count = 0
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))
            count += 1
    print(count,'files in total')
#walk2(os.getcwd())

# use this when you think something will be wrong
try:    
    fin = open('bad_file')
except:
    print('Something went wrong.')
print('still works here')
\

import dbm
import random

ROSTER = {"Beshansky": 0,
          "Collins": 1,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 1,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 1,
          "Wolf": 0}


def create_db(db_name, roster=ROSTER):

    db = dbm.open(db_name, 'c')
    for student, visits in roster.items():
        db[student] = str(visits)
    db.close()
    return db

def call(db_name):

    db = dbm.open(db_name, 'c')

    visits_list = []
    for student in db:
        visits_list.append(int(db[student]))

    min_visits = min(visits_list)

    names = []
    for student in db:
        if int(db[student]) == min_visits:
            names.append(student)

    name_to_update = random.choice(names)
    db[name_to_update] = str(min_visits + 1)
    return name_to_update


def display_all(db_name):
    """
    display all names and values
    db_name: the name of database
    """
    db = dbm.open(db_name, 'r')
    for student in db:
        print(student, int(db[student]))
    db.close()


def main():
    new_db = create_db('db_student')

    display_all('db_student')
    for i in range(3):
        print(call('db_student'))


if __name__ == '__main__':
    main()

import dbm
import random
Hotel = ('SPG','Marriott','Hyatt','Fairmont','Ritz','Four Seasons')

Price = ['100','200','300']

db = dbm.open('db_hotel','c')
for hotel in Hotel:
    db[hotel] = random.choice(Price)
for key in db:
    print(key,db[key])
db.close()
'''
#remember pickle
import pickle
t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print(t2)