from flask import Flask, request, jsonify


app = Flask(__name__)


Queens = [
    { 

    "Queenid": 1, 
    "QueenName" : "Wu Zetian", 
    "QueenNatioanlity" : "Chinese"
   
    },
    {
     "Queenid" : 2, 
    "QueenName" : "Catherine the great", 
    "QueenNatioanlity" : "Russian"
    
    },
     {
     
     "Queenid" : 3, 
    "QueenName" : "Elizabeth Bathory", 
    "QueenNatioanlity" : "Russian"
    
     }
]

@app.route("/") 
def home(): 
    return "Leading Female Sovereigns of All Ages"

@app.route("/Queens", methods=['GET']) 
def get_Queens(): 
    return jsonify(Queens)

@app.route("/Queens/<int:Queen_id>", methods=['GET'])
def get_Queen(Queen_id): 
    Queen = next((queen for queen in Queens if queen["Queenid"] == Queen_id), None)
    if Queen: 
        return jsonify(Queens)
    return {"error": "Queen not found"}, 404
@app.route("/Queens", methods=['POST']) 
def post_Queen(): 
    new_Queen = request.get_json()
    Queens.append(new_Queen)
    return {"message": "Book added successfully", "book": new_Queen}, 201
@app.route("/crushes/<int:crush_id>", methods= ['PUT']) 
def put_crushes(Queen_id):      
    Queen_data = request.get_json()
    Queen = next(Queen for Queen in Queens if Queen ["crushid"] == Queen_id )
    Queen.update({
        "crushname" : Queen_data["crushName"],
        "crushtype" : Queen_data["crushtype"]
    })
    return {"message:" : "your wives are successfully been track", "crushes":Queen} 


@app.route("/crushes/<int:crush_id>", methods= ['DELETE']) 
def delete_crushes(Queen_id):
    Queen = next(Queen for Queen in Queens if Queen ["crushid"] == Queen_id )
    Queens.remove(Queen)
    return{"message:": "crush remove successfully"}


if __name__== '__main__':
        app.run(debug=True)


