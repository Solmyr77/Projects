using System;

namespace Circle
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Adja meg a kör átmérőjét mm-ben: ");
            double diameter = Convert.ToDouble(Console.ReadLine());
            double radius = diameter / 2;
            double circumference = 2 * Math.PI * radius;
            double area = Math.PI * Math.Pow(radius, 2);

            Console.WriteLine($"Átmérő: {diameter} mm");
            Console.WriteLine($"Sugár: {Math.Round(radius, 3)} mm");
            Console.WriteLine($"Kerület: {Math.Round(circumference, 3)} mm");
            Console.WriteLine($"Terület: {Math.Round(area, 3)}");
        }
    }
}
