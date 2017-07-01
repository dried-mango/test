# PicoCTF_2017 : What Is Web

**Category:** Web Exploitation
**Points:** 20
**Description:**

> Someone told me that [some guy](https://en.wikipedia.org/wiki/Tim_Berners-Lee) came up with the "World Wide Web", using "HTML" and "stuff". Can you help me figure out what that is? [Website](http://shell2017.picoctf.com:52334/).


**Hint:**

> How can you figure out how the webpage is actually built?


## Write-up
By viewing the [source](index.html) of the website, we found the first part of the flag
```
$cat index.html | grep "flag"
<!-- The first part of the flag \(there are 3 parts\) is fab79c49d9e -->
```
The site uses [hacker.css](hacker.css) and [script.js](script.js) also, so...


```
$cat hacker.css | grep "flag"
The second part of the flag is 5ba511a0f24 
.glyphicon-flag:before{content:"\e034"}
```
[script.js](script.js)
```
$cat script.js | grep "flag"
* The final part of the flag is 36308e33e85
```

## Flag
>fab79c49d9e5ba511a0f2436308e33e85


