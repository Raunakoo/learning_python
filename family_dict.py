import pprint


#Dictionary Jasmeen Walia
Jasmeen_Walia = {
    "jName":"Jasmeen Walia", "jAge":"37",
    "jGender":"Female",
    "jDisguise":"None",
    "jReal_Identity":"Human",
    "jInterests":"Torture and Drawing",
    "jBrain(s)":"1",
    "jSmartRank":"8",
    "jAddInformation":"Ability to ignore others feelings toward her",
}

#Dictionary Mandeep_Singh
Mandeep_Singh = {
    "mName":"Mandeep Singh",
    "mAge":"41",
    "mGender":"Male",
    "mDisguise":"Male Human",
    "mReal_Identity":"Wild Boar and Donkey",
    "mInterests":"Sleeping and Coding",
    "mBrain(s)":"0",
    "mSmartRank":"6",
    "mAddInformation":"HOW does he do coding after being so dumb?",
}

x = input("Write Here ").upper()

if x == "M":
    pprint.pprint(Mandeep_Singh)

else:
    pprint.pprint(Jasmeen_Walia) 