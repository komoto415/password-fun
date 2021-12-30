import sys
import random
DICE_ROLLS = 5
    
def main(num_words):
    pwd = ""
    with open("eff_large_wordlist.txt", "r") as f:
        word_list = {line.strip().split("\t")[0]: line.strip().split("\t")[1] for line in f.readlines()}
        for _ in range(int(num_words)):
            num = ""
            for _ in range(DICE_ROLLS):
                dice_roll = random.randint(1,6)
                num += str(dice_roll)
            print(num)
            word = word_list[num]
            pwd += f"{word[0].upper()}{word[1:]}"
    print(pwd)

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        pass
