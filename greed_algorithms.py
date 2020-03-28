#Greedy Algorithms and Approximation Algorithms are important and 
#useful when you're trying to just get close to an optimal solution
#since the optimal solution would take too much time to compute.

#This task - Calculate the least amount of radio stations required 
#to broadcast to 50 states
#Sets holds only distinct elements - Basically a Set like in Maths.
#Use greedy algorithms when you find out that your problem is a NP-Complete (Nondeterministic Polonomyial time) problem - Approximation will most likely be the 
#better strategy to solve the problem.

#states_needed = set(["Cairo","Alexandria","Dahab","Aswan","Agouza"])
states_needed = set(["ut","ca","az","nv","id","or","wa","mt"])

stations ={}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["id","wa","mt"])
stations["k3"] = set(["or","nv","ca"])
stations["k4"] = set(["nv","ut"])
stations["k5"] = set(["ca","az"])
# stations["NileFM"] = set(["Cairo","Alexandria","Aswan"])
# stations["NogoomFM"] = set(["Cairo","Fayoum","Hurghada"])
# stations["QaheraWelNas"] = set(["Agouza","Aswan","Domyat"])
# stations["AswanFM"] = set(["Aswan","Luxor","Dahab"])
# stations["MamabataFM"] = set(["Agouza","Cairo","Alexandria"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station #The & is a symbol specific to the usage with sets! | is used for UNION. & for INTERSECTION. - for DIFFERENCE
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)


print(final_stations)