import json
from deepdiff import DeepDiff

with open("TrueCurriculumVitae.json") as f:
    data1 = json.load(f)

with open("dacorreggere.json") as f:
    data2 = json.load(f)

diff = DeepDiff(data1, data2)

if diff:
    print("I file sono diversi")
else:
    print("I file sono uguali")
