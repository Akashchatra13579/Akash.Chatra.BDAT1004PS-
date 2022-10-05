using System;
public class AreaOfTriangle
{
	public static void Main()
    {
    	int s1 = 2 , s2 = 2 , s3 = 2 ;
        Console.WriteLine($"Value of side1 = {s1}, side2 = {s2}, side3 = {s3}");
        double s = (s1 + s2 + s3) / 2;
        double Area = Math.Sqrt(s * (s - s1) * (s - s2) * (s - s3));
        Console.WriteLine("Area of Triangle is = " + Area);
        Console.ReadLine();
    }
  }


