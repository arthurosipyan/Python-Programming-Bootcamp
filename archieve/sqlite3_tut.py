import random

f_names = ["Michael", "Christopher", "Joshua", "Matthew", "David",
           "Daniel", "Andrew", "Joseph", "Justin", "James",
           "Jessica", "Ashley", "Brittany", "Amanda", "Melissa",
           "Stephanie", "Jennifer", "Samantha", "Sarah", "Megan", "Lauren"]

l_names = ["Smith", "Johnson", "Williams", "Jones", "Brown",
           "Davis", "Miller", "Wilson", "Moore", "Taylor",
           "Anderson", "Thomas", "Jackson", "White", "Harris",
           "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]


def create_students(how_many):
    for i in range(how_many):
        f_name = f_names[random.randint(0, len(f_names) - 1)]
        l_name = l_names[random.randint(0, len(l_names) - 1)]

        sex = random.choice(['M', 'F'])
        print(f"INSERT INTO student(f_name, l_name, sex) VALUES ('{f_name}', '{l_name}', '{sex}');")


def create_test_scores(num_tests, num_studs):
    for i in range(1, num_tests+1):
        for j in range(1, num_studs+1):
            score = random.randrange(1, 25)
            print(f"INSERT INTO test_score VALUES ({j}, {i}, {score});")


create_students(10)
create_test_scores(4, 10)
