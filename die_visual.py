import pygal
from die import Die

die = Die()
die2 = Die()
results =[]
x = int(input("ile ma być powtórzeń"))
for roll_num in range(x):
    result = die.roll()+die2.roll()
    results.append(result)
print(results)

frequencies = []
for value in range (2,13):
    frequency = results.count(value)
    frequencies.append(100*frequency/x)
    print("szansa uzyskania ", value, " to ", 100*frequency/x, " procent")


hist = pygal.Bar()
hist.force_uri_protocol = "http"

hist.title = "Prawdopodobieństwo wypadnięcia poszczególnych wyników dwóch rzutów kością"
hist.x_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "wynik"
hist.y_title = "prawdopodobieństwo w procentach"
hist.add("D1", frequencies)
hist.render_to_file("die_visual.svg")
