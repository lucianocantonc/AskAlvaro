#-*- coding: utf-8 -*-
import csv

class User(object):

    def __init__(self, name, project, question):
        self.name = name
        self.project = project
        self.question = question

    def save_dict(self, users):
        csv_columns = ['name', 'project','question']
        csv_file = 'contacts.csv'
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            
            for user in users:
                writer.writerow(user)
        
    


def main():

    users = []

    for _ in range(4):

        user = User("", "", "")
        print('Bem-vindo ao "Ask Alvaro"')
        print('')
        user.name = str(input('O qual é o seu nome?: '))
        print('')
        user.project = str(input('Seu projeto: '))
        print('')
        user.question = str(input('Faca aqui a sua pergunta: '))

        # user = User(name, project, question)
        users.append(user.__dict__)

    tmp_user = User("", "", "")
    tmp_user.save_dict(users)
    
    
    
if __name__ == '__main__':
    main()


# def main():
#         print('Bem-vindo ao "Ask Alvaro"')
#         print('')
#         name = str(input('O qual é o seu nome?: '))
#         print('')
#         project = str(input('Seu projeto: '))
#         print('')
#         question = str(input('Faca aqui a sua pergunta: '))

            
#         with open('notebook.csv', 'a', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow([name, project, question])**/
