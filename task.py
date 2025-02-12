# dictionaries and nesting
capitals = {"France": "Paris",
            "Germany": "Berlin" }
capitals["austria"] = "Salzburg"
print(capitals)

#travel_log = { "France": ["Paris", "Lille"], "Germany": ["Berlin", "Munich"] }
#print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])
travel_log = { "France":{
                "total_visits": 8 ,
                "cities":["Paris", "Lille"]},
                "Germany": {
                "total_visits": 10 ,
                "cities":["Berlin", "Munich","Stuttgart"]}}
print(travel_log["Germany"]["cities"][2])
