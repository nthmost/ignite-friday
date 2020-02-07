
# code -> {"name": "creaturename",
#           "desc": "description",}
      
CREATURES = {}

SOLO_CREATURES = {}
GROUP_CREATURES = {}

with open("creatures.csv") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() == "":
            continue
        parts = line.strip().split(",")
        code = int(''.join(parts[1:5]))

        if parts[6].strip() == "group":
            GROUP_CREATURES[code] = {"name": parts[0], "desc": parts[5]}
        else:
            SOLO_CREATURES[code] = {"name": parts[0], "desc": parts[5]}

        CREATURES[code] = {"name": parts[0], "desc": parts[5]}

