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


语法状态表生成部分  
整个管线目标是：上下文无关文法到状态表（后续支持永久化）  
步骤：  
1、抽取关键词  
2、从一个文法规则里面抽离出用 '|' 分隔的多个情况  
3、解决左递归（寻找递归->解决递归->寻找递归，直到没有递归为止，必须要能够支持直接和间接左递归）  

状态推移部分  
根据状态表对输入进行状态解析，从而判断合法性或者给出错误。  

语法：  
1、使用<>标识关键字  
2、用 | 来分隔多种情况  
3、表达式只有第一个 = 是有文法匹配含义的，后续的都算字符  
4、使用\来恢复上述字符原义  
