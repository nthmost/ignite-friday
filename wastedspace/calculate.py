# Match calculators for creatures

def upper_match(code, group):
    creatures = wastedspace.SOLO_CREATURES
    if group:
        creatures = wastedspace.GROUP_CREATURES
        
    while code < 4444:
        code += 1
        if creatures.get(code):
            return creatures[code]

def lower_match(code, group):
    creatures = wastedspace.SOLO_CREATURES
    if group:
        creatures = wastedspace.GROUP_CREATURES

    while code > 1111:
        code = code - 1
        if creatures.get(code):
            return creatures[code]

def is_match(code, group):
    creatures = wastedspace.SOLO_CREATURES
    if group:
        creatures = wastedspace.GROUP_CREATURES
    if creatures.get(code):
        return creatures[code]
    return None


