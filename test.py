from random import choice

EmotionScore:dict = {
            "emotion": str,
            "EMT_score": int,
        }
        
class Life:
    def __init__(self):
        self.emotions: list = []

    def add_to_life(self, EMT: EmotionScore):
        if EMT["EMT_score"] < -1:
            self.re_evaluate(EMT)
            self.add_to_life(EMT)
        elif EMT["EMT_score"] > 0:
            self.emotions.append(EMT)
        elif EMT["EMT_score"] > 10:
            self.re_evaluate(EMT)
            self.add_to_life(EMT)

    def re_evaluate(self, EMT: EmotionScore):
        EMT["emotion"] = EMT["emotion"] + "_RE_EVALUATED"
        EMT["EMT_score"] = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    def display(self):
        for emotion in self.emotions:
            print(emotion)

zsdnsou = Life()
zsdnsou.add_to_life({
            "emotion": "Joy",
            "EMT_score": 3,
        })
zsdnsou.add_to_life({
            "emotion": "sorrow",
            "EMT_score": -10,
        })
zsdnsou.add_to_life({
            "emotion": "restlessness",
            "EMT_score": -5,
        })
zsdnsou.display()
