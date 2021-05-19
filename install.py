import os
if os.name == 'nt':
    print('using os: Windows')
    calls =[
        'python -m pip install --user --upgrade pip',
        'python -m pip install --user pipenv',
        'python -m pipenv install'
    ]
else:
    print('using os: unix')
    calls =[
        'python3 -m pip install --upgrade pip',
        'python3 -m pip install pipenv',
        'python3 -m pipenv install'
    ]

for i in range(len(calls)):

    os.system(calls[i])
    percentage = 100*((i+ 1)/len(calls))
    hashMarks = (int(percentage))
    print("\r[{}{}] {:5.2f}".format(hashMarks*"#",(100 - hashMarks)*"_", percentage), end="")
