from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)
client = Groq()

@app.route('/generate', methods=['GET'])
def generate():
    product = request.args.get('product', '')
    keywords = request.args.get('keywords', '')
    
    if not product:
        return jsonify({"error": "product parameter required"}), 400
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": f"Write a short compelling product description for: {product}. Keywords: {keywords}. Max 3 sentences."}
        ],
        model="llama3-8b-8192",
    )
    
    return jsonify({"description": chat_completion.choices[0].message.content})

if __name__ == '__main__':
    app.run()