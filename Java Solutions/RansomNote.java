/*
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false. 


Each letter in the magazine string can only be used once in your ransom note.


Note:
You may assume that both strings contain only lowercase letters.



canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

*/ 

public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        if(ransomNote.length()!=0 && magazine.length()==0)
           return false;
        else if(ransomNote.length()==0 || magazine.length()==0){
           return true;
         }
           
        int flag=0;
        int[] table=new int[128];
        char[] ransom=ransomNote.toCharArray();
        
        for(char x:ransom){
            
            table[x]++;
        }
        
        int[] magazineTable=new int[128];
        char[] mag=magazine.toCharArray();
        
        for(char y:mag){
            
            magazineTable[y]++;
        }
         
        char[] ransomCheck=ransomNote.toCharArray();
        for(char z:ransomCheck){
           magazineTable[z]--;
           if(magazineTable[z]<0)
           return false;
         }
        return true;

     }
  }