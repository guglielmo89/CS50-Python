results = ["Mario", "Luigi",]

results.append("Princess")

results.append(["Bowser", "Donkey Kong"]) #nest a list in the existing list (sub-list)
results.remove(["Bowser", "Donkey Kong"])

results.extend(["Bowser", "Donkey Kong"]) #add the elements in the existing list

results.remove("Bowser")

results.insert(0, "Bowser")

results.reverse()

print(results)
