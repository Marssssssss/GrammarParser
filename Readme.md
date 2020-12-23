Whole process: Grammar_content -> State_map  
&nbsp;·&nbsp;step1: Take out keyword.  
&nbsp;·&nbsp;step2: Deal with multi-sentences.  
&nbsp;·&nbsp;step3: Deal with left recursion(Direct and Indirect).  
Then use map machine can check if input is legal.  
  
Grammar content rules:  
&nbsp;&nbsp;1.Use <> to include a word, which indicate that the word is a keyword.  
&nbsp;&nbsp;2.Use \ to make the meaning of next char non-transferred. When it occur in the end of line, that means joint next line.  
&nbsp;&nbsp;3.Use | to indicate the key word has one more equation of other keyword and identify.  
&nbsp;&nbsp;4.Only the first = mean equal in a line, other = is just sign.(will replace = with -> after)  
Notice that space will be ignore unless use \ to sign it.
