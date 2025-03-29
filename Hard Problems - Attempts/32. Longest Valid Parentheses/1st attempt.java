class Solution {
    public int longestValidParentheses(String s) {
        String character_array[] = s.split("");
        int count = 0;
        int size = character_array.length;

        if(size == 0){
            return 0;
        }

        for(int i = 0 ; i < size; i++){
            if((size - i) == 1){
                return count;
            }
            else if(character_array[i].equals("(") && character_array[i+1].equals(")")){
                count += 2;
            }
        }
        return 0;
    }
}



/*
Got all the test cases, but unfortuntely didn't get the separate cases of double paratheses! (())

Wrong Answer
64 / 231 testcases passed

Editorial
Input
s =
"()(())"

Use Testcase
Output
4
Expected
6
*/