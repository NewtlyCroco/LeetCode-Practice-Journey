class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> list = new ArrayList<String>();
        for(int i = 1; i < n+1; i++){
            if((i % 5 == 0) && (i % 3 == 0)){
                list.add("FizzBuzz");
            }
            else if(i % 3 == 0){
                list.add("Fizz");
            }
            else if(i % 5 == 0){
                list.add("Buzz");
            }
            else{
                list.add(Integer.toString(i));
            }
        }
        return list;
    }
}