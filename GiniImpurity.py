import pandas as pd

data = {
    "Weather": ["Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast", "Sunny"],
    "Temperature": ["Hot", "Mild", "Cool", "Cool", "Mild", "Hot", "Mild", "Cool"],
    "Play": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

dataset = list(zip(*data.values()))
dataset = [list(row) for row in dataset]

group_col = "Weather"
label_col = "Play"
def gini_impurity ():
    total_instance = len(df)
    if total_instance == 0:
        return 0
    else:
        grouped = {}
        for weather, play in zip(data[group_col], data[label_col]):
            # Convert 'Yes'/'No' to 'y'/'n'
            play_symbol = 'y' if play.lower() == 'yes' else 'n'

            # Create the entry if it doesn't exist
            if weather not in grouped:
                grouped[weather] = {'y': 0, 'n': 0}

            # Increment the correct counter
            grouped[weather][play_symbol] += 1

            # calculate gini impurity for each group
            weighted_gini = []
        print(grouped)
        for key in grouped:
            itemValue = grouped[key]
            total = itemValue['y'] + itemValue['n']
            prob_y = itemValue['y'] / total
            prob_x = itemValue['n'] / total
            gini = 1 - (prob_y ** 2 + prob_x ** 2)
            weighted_gini.append((key , gini))

        weighted_gini_impurity = 0
        for wg  in weighted_gini:
            grouped_value = grouped[wg[0]]
            total = grouped_value['y'] + grouped_value['n']
            weighted_gini_impurity = weighted_gini_impurity + total * wg[1] / total_instance


    return weighted_gini_impurity




print(gini_impurity())
print (df)