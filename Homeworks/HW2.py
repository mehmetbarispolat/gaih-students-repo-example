cvs = {
    'cv_1': {
        'Name' : "Ahmet",
        'Surname' : "Poyraz",
        'Job Title' : "Software Developer"
    },
    'cv_2' : {
        'Name' : "Veli",
        'Surname' : "Poyraz",
        'Job Title' : "Backend Developer"
    }, 
    'cv_3' : {
        'Name' : "Ali",
        'Surname' : "Polat",
        'Job Title' : "Frontend Developer"
    }, 
    'cv_4' : {
        'Name' : "Cengiz",
        'Surname' : "Deniz",
        'Job Title' : "Software Engineer"
    }, 
    'cv_5' : {
        'Name' : "Ömer",
        'Surname' : "Seyfettin",
        'Job Title' : "Writer"
    }
} 

for key, value in cvs.items():
    print(f'{key} -- ')
    for k,v in value.items():
        print(f'{k} : {v}')
