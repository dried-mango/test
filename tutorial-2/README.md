# PicoCTF_2017 : tutorial 2

**Category:** Tutorial
**Points:** 0
**Description:**

>Robin handed me [this](message.txt) the other day. Maybe it will help me find the answer?


**Hint:**

> There are a number of solvers on the internet that can help!


## Write-up
Decrypt the ROT13 cipher text in message.txt (Rotate characters by 13 places)

$echo "Lb, fb unir lbh orra cynlvat gung arj Zrfbcrgf tnzr? Gubfr arj Zrtnybalpuvqnr naq Oenqlcbqvqnr gurl nqqrq ner cerggl pbby. Npghnyyl, V jbhyq tb nf sne nf fnlvat gung vg vf abj zl yvsr'f qrnerfg nzovgvba gb bognva n "Vasyngnoyr Fybgu Zbafgre"!" | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'

>**Yo, so have you been playing that new Mesopets game? Those new Megalonychidae and Bradypodidae they added are pretty cool. Actually, I would go as far as saying that it is now my life's dearest ambition to obtain a Inflatable Sloth Monster!**


## Flag
>Inflatable Sloth Monster
