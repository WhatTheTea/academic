using System.Security.Cryptography;
using System.Text;

var data = Console.ReadLine();
var bytes = new UTF8Encoding().GetBytes(data);
var hash = SHA1.HashData(bytes);
Console.WriteLine(string.Join("", hash.Select(x => x.ToString("x"))));