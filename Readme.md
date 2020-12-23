Whole process: Grammar_content -> State_map  
&nbsp;·&nbsp;step1: Take out keyword.  
&nbsp;·&nbsp;step2: Deal with multi-sentences.  
&nbsp;·&nbsp;step3: Generate state map.  
Then use map machine can check if input is legal.  
  
Grammar content rules:  
&nbsp;&nbsp;1.Use <> to include a word, which indicate that the word is a keyword.  
&nbsp;&nbsp;2.Use \ to make the meaning of next char non-transferred. When it occur in the end of line, that means joint next line.
&nbsp;&nbsp;3.Use | to indicate the key word has one more equation of other keyword and identify.  
Notice that space will be ignore unless use \ to sign it.
