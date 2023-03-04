using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections;

namespace kYa.TaskKiller.Main;
class Program
{
    public static void Main()
    {

        var a = GetInts();

        a.MoveNext();
        a.MoveNext();
        a.MoveNext();
        a.MoveNext();
        
        a = GetInts();
        a.MoveNext();
        a.MoveNext();

        Console.WriteLine();
    }

    static IEnumerator GetInts()
    {
        Console.WriteLine("first");
        yield return 1;

        Console.WriteLine("second");
        yield return 2;
    }
}
