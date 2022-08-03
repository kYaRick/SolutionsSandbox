using System;
using System.Diagnostics;
using System.Linq;
using System.Threading;

namespace kYa.TaskKiller.Main;
class Program
{
    public static void Main()
    {
        new Thread(_FiveHundred).Start();
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
