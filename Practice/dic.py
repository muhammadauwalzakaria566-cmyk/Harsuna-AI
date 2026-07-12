progress = {
    'name': 'Auwal',
    'day': 10,
    'skill_learn': ['loops', 'functions', 'classes'],
    'projects': 'Harsuna AI'
}

# Print each value using keys
print(progress['name'])
print(progress['day'])
print(progress['skill_learn'])
print(progress['projects'])

# Update the day
progress['day'] = 15

# Add a new key
progress['next_goal'] = 'Learn Git and GitHub'

# Loop through and print everything
for key in progress:
    print(key + ' : ' + str(progress[key]))