open("initial_data.json","wb").write(open("locations.json").read().decode("unicode_escape").encode("utf8"))