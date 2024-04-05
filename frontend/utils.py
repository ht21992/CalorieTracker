def convert_status_to_description(value):
    indexes = {0: 'Extremely Weak',1:'Weak', 2:'Normal', 3:'Overweight', 4:'Obesity', 5:'Extreme Obesity'}
    return indexes.get(value[0])