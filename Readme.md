Whole process: Grammar_content -> State_map  
step1: Take out keyword.  
step2: Deal with multi-sentences.  
step3: Generate state map.  
Then use map machine can check if input is legal.  
  
Grammar content rules:  
1.Use <> to include a word, which indicate that the word is a keyword.  
2.Use \ to make the meaning of next char non-transferred.  
3.Use | to indicate the key word has one more equation of other keyword and identify.
