__Modern Computer Architecture and Organization Third Edition__, by Jim Ledin. Published by Packt Publishing.
# Chapter 15, Exercise 2

Modify the nanoGPT code to print the input tokens and their indices for the prompt “Tell me about GPT-2.”

# Answer
1.	In _sample.py_, locate the line that contains `start_ids = encode(start)`. This line performs token encoding. Insert this code immediately after that line:
```
for tok in start_ids:
    print(f'{str(tok).ljust(5)} : "{enc.decode([tok])}"')`
```
2. The output resulting from this code is:
```
24446 : "Tell"
502   : " me"
546   : " about"
402   : " G"
11571 : "PT"
12    : "-"
17    : "2"
13    : "."`
```
3. This output provides a list of the indices within the token vector and the text of each token, including leading spaces that are part of some of the tokens.
