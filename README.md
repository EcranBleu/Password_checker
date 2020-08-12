# Password checker

Takes passwords as arguments and returns if they have been exposed, and if so, how many times.

The HaveIBeenPwned API takes the first 5 characters of the password's sha1 hash, and returns
a list of suffixes (the hash without the first 5 characters) that have these 5 characters as a prefix.
Each suffix is followed by a colon and a number, which is the number of times the password was leaked.

This program:
 
 - takes each password; 
 - creates a sha1 hash of it;
 - truncates that hash to its first 5 characters;
 - sends a query to the HaveIBeenPwned API;
 - receives the answer;
 - analyzes if our hash's suffix is present in the answer;
 - outputs an answer depending on this previous condition.
 
