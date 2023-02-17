using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace kYaSandbox.PingerSpace;

public static class Pinger
{
    public static bool IsPing(string url) => !String.IsNullOrEmpty(url);
}
