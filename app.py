from flask import Flask,request
from opensearchpy import OpenSearch
from flask_cors import CORS


app=Flask(__name__)
CORS(app)

host="localhost"
port=9200
auth=("admin","password") #your opensearch password 
index="recipe"

client=OpenSearch(
    hosts=[{"host":host,"port":port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False
)

def filterfunc(data):
    queries=[]
    search=data['searchValue']
    catogory=data['selectedValue']
    slider=data['sliderValue']
    print(search,catogory,slider)
    if slider > 0:
         sValue={
             "range": {
                        "protein": {"gt": slider  }
                        }
         }
         queries.append(sValue)

    if  catogory and len(catogory) > 0:
        cValue={
             "match": {  "categories": catogory}
        }
        queries.append(cValue)
    
    if search and len(search) > 0:
        searchValue={
             "match":{"title":search}
        }
        queries.append(searchValue)
    
    return queries

def queryFun(data):
   query={
       "query" : {
        "bool": {
            "must":data
               }
             }
          }
   print(query)
   return query


@app.route("/",methods=['GET','POST'])
def index():
    filterFields=filterfunc(request.json)
    query=queryFun(filterFields)
    response=client.search(body=query,index="recipe")
    return response

# query example
# q = 'bread'
# querys = {
#   'size': 20,
#   'query': {
#     'multi_match': {
#       'query': q,
#       'fields': ['title']
#     }
#   }
# }

 

# @app.route("/search")
# def search():
#     response=client.search(index="recipe")
#     return response



if  __name__=='__main__':
    app.run(host='0.0.0.0',port="5000" ,debug=True)

