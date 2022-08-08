using System;
using System.Diagnostics;

namespace kYa.TaskKiller.Main;
class Program
{
    public static void Main()
    {
    }

    private static void _FiveHundred()
    {
        while(true)
        {
            foreach (var process in Process.GetProcesses().Where(el => el.ProcessName.Contains("ZSA")))
            {
                Console.WriteLine(process.ProcessName);
                process.Kill();
            }

            Thread.Sleep(500);
            Console.Clear();
        }
    }
}
