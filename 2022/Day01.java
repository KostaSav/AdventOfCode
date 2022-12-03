import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day01 {

    public static void part1() throws IOException {

        int max = 0;
        int sum = 0;
        int len = 0;

        String[] listOfStrings
            = Utils.parseFileToStringArray("day01.txt");
        
        while(len < listOfStrings.length - 1)
        {
            //System.out.println(listOfStrings[len]);

            if (!"".equals(listOfStrings[len]))
            {
                sum += Integer.parseInt(listOfStrings[len]);
            }
            else
            {
                if (sum > max)
                {
                    max = sum;
                }
                sum = 0;
            }
            len += 1;
        }

        System.out.println(max);
        //System.out.println(Arrays.toString(listOfStrings));
    }

    public static void part2() throws IOException {

        int sum = 0;
        int len = 0;
        int sumMaxThree = 0;
        List<Integer> totals = new ArrayList<Integer>();

        String[] listOfStrings
            = Utils.parseFileToStringArray("day01.txt");
        
        while(len < listOfStrings.length - 1)
        {
            //System.out.println(listOfStrings[len]);

            if (!"".equals(listOfStrings[len]))
            {
                sum += Integer.parseInt(listOfStrings[len]);
            }
            else
            {
                totals.add(sum);
                sum = 0;
            }
            len += 1;
        }

        int[] totalsArray = totals.stream().mapToInt(i -> i).toArray();
        Arrays.sort(totalsArray);
        sumMaxThree = totalsArray[totalsArray.length - 1] + totalsArray[totalsArray.length - 2] + totalsArray[totalsArray.length - 3];

        System.out.println(sumMaxThree);
    }

    public static void main(String[] args) throws IOException {
        //part1();
        //part2();
    }
}
