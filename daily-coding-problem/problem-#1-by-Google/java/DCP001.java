import java.util.*; 
public class DCP001 {
    public boolean soluton(int[] list_nums, int target) {
        Set<Integer> cache = new HashSet<Integer>();
        for (int i=0; i < list_nums.length; i ++) {
            int num = list_nums[i];
            if (cache.contains(target - num)) {
                return true;
            } else {
                cache.add(num);
            }
        }
        return false;
    }

    public static void main(String[] args){
        DCP001 dcp001 = new DCP001();
        int[] test_list = new int[]{10, 15, 3, 7} ;
        int k = 17;
        System.out.println(dcp001.soluton(test_list, k));
    }
}