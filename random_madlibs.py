from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "main":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()
