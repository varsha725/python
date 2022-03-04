# Python code to count and display number of vowels
def Check_Vow(string, vowels):
final = [each for each in string if each in vowels]
print("Total Vowels: ", len(final))
print(final, "\n")
# Driver Code
string = "Geeks for Geeks is doing good job"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);
