class Solution {
    public int pivotInteger(int n) {
        int left_hand_sum = 1;
        int right_hand_sum;
        if(n == 1){ //this is the extrenuating case
            return 1;
        }
        for(int i = 1; i < n + 1; i++){
            left_hand_sum += (i + 1);
            right_hand_sum = 0;
            System.out.println(left_hand_sum);
            for(int j = (i + 1); j < n + 1; j++){
                right_hand_sum += j;
            }
            
            if(left_hand_sum == right_hand_sum){
                return i + 1;
            }
           
        }
        return -1;   
    }
}