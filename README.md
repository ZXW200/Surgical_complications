Datasource from https://www.openml.org/search?type=data&status=active&id=45648

At present, only four groups have been divided into whether there are complications and whether there is death
Use the following code to access four datasets separately/n
df[df["GROUP"] == "Death_with_complication"]/n
df[df["GROUP"] ==  "Normal_death_no_complication"]/n
df[df["GROUP"] == "Alive_no_complication"]/n
df[df["GROUP"] == "Alive_with_complication"]/n
