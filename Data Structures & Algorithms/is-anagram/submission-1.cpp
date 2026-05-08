class Solution {
public:
    bool isAnagram(string s, string t) {
        if (t.length()!=s.length()){return false;}
        int arr[26] = {0};
        for(int i; i<s.length(); i++){
            arr[s[i]-'a']++;
            arr[t[i]-'a']--;
        }
        for (int v : arr){
            if (v != 0){
                return false;
            }
        }
        return true;
    }
};
