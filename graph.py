import matplotlib.pyplot as plt
import json 

json_file = "myjsonfile.json"
with open(json_file) as jsons_file:
    data = json.load(jsons_file)
    

    left = data['table'][0]['letter'],data['table'][1]['letter'],data['table'][2]['letter'],data['table'][3]['letter'],data['table'][4]['letter'],data['table'][5]['letter'],data['table'][6]['letter'],data['table'][7]['letter'],data['table'][8]['letter'],data['table'][9]['letter'],data['table'][10]['letter'],data['table'][11]['letter'],data['table'][12]['letter'],data['table'][13]['letter'],data['table'][14]['letter'],data['table'][15]['letter'],data['table'][16]['letter'],data['table'][17]['letter'],data['table'][18]['letter'],data['table'][19]['letter'],data['table'][20]['letter'],data['table'][21]['letter'],data['table'][22]['letter'],data['table'][23]['letter'],data['table'][24]['letter'],data['table'][25]['letter']
    height = data['table'][0]['counts'],data['table'][1]['counts'],data['table'][2]['counts'],data['table'][3]['counts'],data['table'][4]['counts'],data['table'][5]['counts'],data['table'][6]['counts'],data['table'][7]['counts'],data['table'][8]['counts'],data['table'][9]['counts'],data['table'][10]['counts'],data['table'][11]['counts'],data['table'][12]['counts'],data['table'][13]['counts'],data['table'][14]['counts'],data['table'][15]['counts'],data['table'][16]['counts'],data['table'][17]['counts'],data['table'][18]['counts'],data['table'][19]['counts'],data['table'][20]['counts'],data['table'][21]['counts'],data['table'][22]['counts'],data['table'][23]['counts'],data['table'][24]['counts'],data['table'][25]['counts']
    print("Type:", type(data))
 
    tick_label = [data['table'][0]['letter'],data['table'][1]['letter'],data['table'][2]['letter'],data['table'][3]['letter'],data['table'][4]['letter'],data['table'][5]['letter'],data['table'][6]['letter'],data['table'][7]['letter'],data['table'][8]['letter'],data['table'][9]['letter'],data['table'][10]['letter'],data['table'][11]['letter'],data['table'][12]['letter'],data['table'][13]['letter'],data['table'][14]['letter'],data['table'][15]['letter'],data['table'][16]['letter'],data['table'][17]['letter'],data['table'][18]['letter'],data['table'][19]['letter'],data['table'][20]['letter'],data['table'][21]['letter'],data['table'][22]['letter'],data['table'][23]['letter'],data['table'][24]['letter'],data['table'][25]['letter']]
    plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])

    plt.xlabel('Alphabets')
    plt.ylabel('Occurences')
    plt.title('Occurences of letters in the english alphabet (five letter words)')
    
    plt.show()
    print("letters:", data['table'][0]['letter'])