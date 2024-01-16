def dodawanie(x,y):
	return x + y

def odejmowanie(x,y):
	return x - y

def mnozenie(x,y):
	return x * y

def dzielenie(x,y):
	if y != 0:
        	return x / y
	else:
        	return "Nie dziel przez 0!"

while True:
	print("=== KALKULATOR ===")
	print("Jakie działanie chcesz wykonać:")
	print("1. Dodawanie")
	print("2. Odejmowanie")
	print("3. Mnozenie")
	print("4. Dzielenie")
	print("5. Wyjście")

	opcja = input("Podaj numer operacji od 1 do 5:")

	if opcja == '5':
		print("Wyjście z programu.")
		break

	if opcja not in ('1','2','3','4'):
		print("Nie ma takiej operacji. Wprowadz ponownie")
		continue

	liczbaX = float(input("Podaj pierwszą liczbę: "))
	liczbaY = float(input("Podaj drugą liczbę: "))

	if opcja == '1':
		print(liczbaX, " + ", liczbaY, " = ", dodawanie(liczbaX,liczbaY))
	elif opcja == '2':
		print(liczbaX, " - ", liczbaY, " = ", odejmowanie(liczbaX,liczbaY))
	elif opcja == '3':
		print(liczbaX, " * ", liczbaY, " = ", mnozenie(liczbaX,liczbaY))
	elif opcja == '4':
		print(liczbaX, " / ", liczbaY, " = ", dzielenie(liczbaX,liczbaY))

