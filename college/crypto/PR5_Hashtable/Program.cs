const int prime = 769;

static int Hash(string word)
{
    int sum = word.Aggregate(0, (accum, x) => accum + x);
    return sum % prime;
}

var hashtable = new string[prime];

void Add(string key, string value) => hashtable[Hash(key)] = value;

string Get(string key) => hashtable[Hash(key)];

// Populating hashtable
while (true)
{
    Console.Write("Enter KeyValue pair (key value) or /next: ");
    var pair = Console.ReadLine()!.Split(' ');
    if (pair.Length != 2 && pair.Contains("/next")) break;
    Add(pair[0], pair[1]);
    Console.WriteLine("Pair has been added!");
}

// Retrieving data
while (true)
{
    Console.Write("Enter key or /exit: ");
    var key = Console.ReadLine();
    if (key.Contains("/exit")) break;
    var val = Get(key);
    Console.WriteLine($"Your data: {val}");
}