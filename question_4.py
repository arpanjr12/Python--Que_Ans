
# Create a program that counts the number of vowels in a sentence.





def check(sentence): 
    vowels='aeiouAEIOU'
    count=0
    for char in sentence:
      if  char in vowels:
            count +=1

    return count

if __name__ == "__main__":

    sentence=input("enter your sentence: ")
    vowel_count = check(sentence)
    
print(f" the number of vowels in the sentence is {vowel_count}")




