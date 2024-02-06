from elasticsearch import Elasticsearch

def perform_search(searchString):
    es = Elasticsearch("http://localhost:9200")
   
    if searchString.startswith("id:"):
        flagID=True
    else:
        flagID=False



        #  Your search query
    if searchString == "all4":
        print("getting trending articles")
        search_query_prim = {
            "query": {
                "match_all": {}
            },
            "size": 4
        }


    elif searchString == "all": 
        print("getting all articles")
        search_query_prim = {
            "query": {
                "match_all": {}
            }
        }
    
    elif flagID == True:
         print("search based on id")
         search_query_prim = {
            "query": {
                "bool": {
                "must": [
                    {
                    "term": {
                        "Article_ID": {
                        "value": searchString.split(":").pop()
                        }
                     }
                    }
                ],
                "filter": [],
                "should": [],
                "must_not": []
                }
            }
            }

    else:
        print("hehehehehehehehheheheheheheh")
        search_query_prim = {
            "query": {
                "bool": {
                    "must": [{
                        "match": {
                            "DocumentTitle": searchString
                        }
                    }],
                    "filter": [],
                    "should": [],
                    "must_not": []
                }
            }
        }


    # Perform the search
    resp = es.search(index="data", body=search_query_prim)
    print(resp)
    return resp