using System;

namespace Calculus
{
    class Program
    {
        static void Main(string[] args)
        {

            while (true)

            {

                Console.WriteLine("Kalkulusz");

                Console.Write("Adjon meg egy számot: ");
                decimal num1 = Convert.ToDecimal(Console.ReadLine());

                Console.Write("Adja meg a műveleti jelet (+, -, *, /): ");
                string op = Console.ReadLine();

                Console.Write("Adja meg a második számot: ");
                decimal num2 = Convert.ToDecimal(Console.ReadLine());



                if (op == "+")
                {
                    Console.Write("Az összeg: ");
                    Console.Write(num1 + num2);
                    break;
                }

                else if (op == "-")
                {
                    Console.Write("A különbség: ");
                    Console.Write(num1 - num2);
                    break;
                }

                else if (op == "*")
                {
                    Console.Write("A szorzat: ");
                    Console.Write(num1 * num2);
                    break;
                }

                else if (op == "/")
                {

                    Convert.ToDecimal(num1);
                    Convert.ToDecimal(num2);

                    Console.Write("A hányados: ");
                    Console.Write(Math.Round(num1 / num2, 3));
                    break;
                }

                else
                {
                    Console.WriteLine("Kérem érvényes műveleti jelet adjon meg!");
                }

            }
        }
    }
}
