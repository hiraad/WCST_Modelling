import json
from models import outperform
from util import Statistics, Experiment

with open('data/conditions.txt', "r") as file:
    conditions_json = json.load(file)
criterion_order = conditions_json[0]["Criterion_Order"]
pile_order = conditions_json[1]["Target_Order"]
deck_order = conditions_json[2]["Card_Order"]


print(len(criterion_order))
print(len(pile_order))
print(len(deck_order))

for i in range(3):

    outperform.simulate(deck_order[i], criterion_order[i], pile_order[i])
    Statistics.results()
