import os
import string

def is_palindrome(word):
   words = word.lower().translate(str.maketrans('', '', string.punctuation))
   return words == words[::-1] and len(words) > 1

def process_sentences(input_file, output_file):
   if not os.path.exists(input_file):
       print(f"Error: {input_file} not found.")
       return
   
   with open(input_file, 'r') as infile, open(output_file, 'w',) as outfile:
       for line in infile:
           sentence = line.strip()
           if not sentence:
               continue  
           words = sentence.split()
           word_count = len(words)
           max_length = max(len(word) for word in words)
           longest_words = [word for word in words if len(word) == max_length]

           palindromes = []
           for word in words:
               if is_palindrome(word):
                   palindromes.append(word)

           palindrome_result = ', '.join(palindromes) if palindromes else 'None'

           outfile.write(f"Sentence: {sentence}\n")
           outfile.write(f"Word count: {word_count}\n")
           outfile.write(f"Longest word: {longest_words}\n")
           outfile.write(f"Palindrome: {palindrome_result}\n\n")


   print(f"Analysis complete. Results saved in {output_file}")


if __name__ == "__main__":
   input_filename = 'sentences.txt'
   output_filename = 'sentences_analysis.txt'
   process_sentences(input_filename, output_filename)
