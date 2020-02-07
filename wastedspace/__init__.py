# constants for use in 13th Floor Personality Test

from .creatures import SOLO_CREATURES, GROUP_CREATURES, CREATURES

SYM_AGREE = "♆"     # antimony
ASK_AGREE = "Do you agree?"
OPTS_AGREE = {1: "I disagree.",
              2: "It depends, am I gonna like it?",
              3: "Yes.",
              4: "We are a Yes Machine!",
             }

AGREE = {"symbol": SYM_AGREE,
         "ask": ASK_AGREE,
         "opts": OPTS_AGREE
        }

#---

SYM_IDEAS = "☿"     # mercury
ASK_IDEAS = "Do you have any ideas?"
OPTS_IDEAS = {1: "No idea.",
              2: "I have one bad idea.",
              3: "There are no bad ideas, just inappropriate clothing.",
              4: "Let me answer this in the form of improv dance spellcasting.",
             }

IDEAS = {"symbol": SYM_IDEAS,
         "ask": ASK_IDEAS,
         "opts": OPTS_IDEAS,
        }

#---

SYM_SENSES = "⇞"    # sulphur
ASK_SENSES = "How's your energy level right now?"
OPTS_SENSES = {1: "Got anywhere to sit down?",
               2: "Dancing might feel good.",
               3: "Ready for anything!",
               4: "I AM LITERALLY TIGGER",
              }

SENSES = {"symbol": SYM_SENSES,
          "ask": ASK_SENSES,
          "opts": OPTS_SENSES,
         }

#---

SYM_RULES = "🜔"     # salt
ASK_RULES = "How do you feel about rules right now?"
OPTS_RULES = {1: "I am chaos incarnate!",
              2: "Some kind of decorum is usually a good idea, right?",
              3: "There is a natural order.",
              4: "I AM THE LAW.",
             }

RULES = {"symbol": SYM_RULES,
         "ask": ASK_RULES,
         "opts": OPTS_RULES,
        }

#--- END

#--- BEGIN calculator functions

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

#--- END calculators
