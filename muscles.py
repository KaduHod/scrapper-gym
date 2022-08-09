import json
def main():
    with open('./jsons/muscles.json','w') as muscles :
        muscles.write(json.dumps(['Calves', 'Quadr\u00edceps', 'Hamstrings', 'Gluteus', 'Hips', 'Lower back', 'Lats', 'Trapezius', 'Abdominals', 'Chest', 'Deltoids', 'Tr\u00edceps', 'B\u00edceps', 'Forearms']))
        
if __name__ == "__main__":
    main()