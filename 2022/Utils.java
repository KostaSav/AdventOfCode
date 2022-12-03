// import necessary packages
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
 
public class Utils {
    // include throws to handle some file handling exceptions
    public static String[] parseFileToStringArray(String input_filename)
        throws IOException
    {
        String line = "";

        Scanner file = new Scanner(new File("2022/"+input_filename)).useDelimiter("\r\n");

        List<String> calories = new ArrayList<String>();

        while(file.hasNext())
        {
            line = file.next();
            calories.add(line);
        }
        file.close();

        String[] caloriesArray = calories.toArray(new String[0]);

        // for(String s : caloriesArray)
        // {
        //     System.out.println(s);
        // }

        return caloriesArray;
    }
}
