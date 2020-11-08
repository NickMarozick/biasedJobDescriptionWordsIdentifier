from __future__ import division
import re

def calculateBiasPercentages(biasTally):
        male=0
        female=0
        raciallyInsensitive=0


        biasKeys = biasTally.keys()


        if len(biasTally) > 0:
                if 'male' in biasKeys:
                        male = biasTally["male"]

                if 'female' in biasKeys:
                        female = biasTally["female"]

                if 'raciallyInsensitive' in biasKeys:
                        raciallyInsensitive = biasTally["raciallyInsensitive"]

                total = male + female + raciallyInsensitive


                print("Of the potentially biased words used:")
                malePercent= '{0:.0%}'.format(male/total)
                femalePercent= '{0:.0%}'.format(female/total)
                raciallyInsensitivePercent= '{0:.0%}'.format(raciallyInsensitive/total)

                print("Male Biased Words Percentage: ", malePercent)
                print("Female Biased Words Percentage: ", femalePercent)
                print("Racially Insensitive Biased Words Percentage: ", raciallyInsensitivePercent)


biasDict= {"strong": "male", "lead": "male", "analysis": "male", "analytical": "male", "analy": "male", "driving": "male", "driv": "male", "individual": "male", "proven": "male", "workforce": "male", "decision": "male", "active": "male", "adventurous": "male", "aggress": "male", "ambition": "male", "ambitious": "male", "assert": "male", "athlet": "male", "auton": "male","boast": "male", "challeng": "male", "compet": "male", "confident": "male", "courag": "male", "decide": "male", "decisive": "male", "decision": "male", "determin": "male", "domina": "male", "force": "male", "greedy": "male", "headstron": "male", "heirarch": "male", "hostil": "male", "impulsive": "male", "indepen": "male", "individual": "male", "intellect": "male", "lead": "male", "logic": "male", "masculine": "male", "objective": "male", "opinion": "male", "outspoken": "male", "persist": "male","principle": "male", "reckless": "male", "stubborn": "male", "superior": "male", "self-confiden": "male", "self confiden": "male", "self-sufficien": "male", "self sufficien": "male", "self-relian": "male", "self relian": "male", "affectionate": "female", "child": "female", "cheer": "female", "commit": "female", "communal": "female", "compassion": "female", "connect": "female", "considerate": "female", "cooperat": "female", "depend": "female", "emotiona": "female", "empath": "female", "feminine": "female", "flatterable": "female", "gentle": "female", "honest": "female", "interpersonal": "female", "interdepen": "female", "interpersona": "female", "kind": "female", "kinship": "female", "loyal": "female", "modesty": "female", "nag": "female", "nurtur": "female", "pleasant": "female", "polite": "female", "quiet": "female", "respons": "female", "sensitiv": "female", "submissive": "female", "support": "female", "sympath": "female", "tender": "female", "together": "female", "trust": "female", "understand": "female", "warm": "female", "whin": "female", "yield: ": "female", "blacklist": "raciallyInsensitive", "brown bag": "raciallyInsensitive", "latino": "raciallyInsensitive", "latina": "raciallyInsensitive", "native english speaker": "raciallyInsensitive", "native speaker": "raciallyInsensitive", "native english speaker": "raciallyInsensitive", "english native speaker": "raciallyInsensitive", "master": "raciallyInsensitive", "whitelist": "raciallyInsensitive"}

print(biasDict)

openFile= open("sampleJD.txt")

dangerWordList = {}

weightedBiasTally = {}

for line in openFile:
        line= line.lower()

        words = line.split()

        for word in words:

                found = biasDict.get(word)

                if found not in weightedBiasTally:
                        weightedBiasTally[found]=1
                else:
                        weightedBiasTally[found]+=1


                if word in biasDict:
                        if word not in dangerWordList:
                                dangerWordList[word]=1
                        else:
                                #dangerWordList[name] += 1
                                danferWordList[word]+=1

