using System.Text.RegularExpressions;

namespace kYa.Redency.Task;
public static class RedencyTast
{  
    public static string Order(string input)
        => _Order(input, true);

    private static string _Order(string input, bool isIgnoreException = false)
    {
        string result = "";

        if (!string.IsNullOrWhiteSpace(input))
        {
            result = string.Join(" ",
                Regex.Split(input.Trim(), @"(?i)\s+")
                .OrderBy(el => el)
                .OrderBy(el => toInt(el))
                );
        }
        else if (input.Equals(string.Empty))
        {
            result = input;
        }
        else if (!isIgnoreException)
        {
            throw new InvalidOperationException($"Input data exception!\n\tInput string is empty.");
        }

        int toInt(string inStr)
        {
            var lResult = 0;
            var tempNum = 0;

            if (!string.IsNullOrWhiteSpace(inStr))
                foreach (var el in inStr)
                    if (int.TryParse(el.ToString(), out tempNum))
                        lResult += tempNum;

            return lResult;
        };

        return result;
    }
}