import random
import time

def qna(question):
    ans = input(question + " (yes/no): ").lower()

    if ans == "yes":
        result = random.choice([
            "TELLING THE TRUTH",
            "TELLING THE TRUTH",
            "LYING"
            ])
        
    elif ans == "no":
        result = random.choice([
            "LYING",
            "LYING",
            "TELLING THE TRUTH"
            ])
        
    else:
        print('Please answer with "yes" or "no" only')
        
        return  

    print("\nAnalysing....")
    time.sleep(1.5)

    print(f"Hypothesis: {result}")


