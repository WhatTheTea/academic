using System.Security.Cryptography;
using System.Text;

var data = Console.ReadLine();
var bytes = UTF8Encoding.Default.GetBytes(data!);
var hash = SHA256.HashData(bytes);
Console.WriteLine(string.Join("", hash.Select(x => x.ToString("x"))));