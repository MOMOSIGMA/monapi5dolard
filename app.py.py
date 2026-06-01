from flask import Flask, request, jsonify
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic()

@app.route('/generate', methods=['GET'])
def generate():
    product = request.args.get('product', '')
    keywords = request.args.get('keywords', '')
    
    if not product:
        return jsonify({"error": "product parameter required"}), 400
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[
            {"role": "user", "content": f"Write a short compelling product description for: {product}. Keywords: {keywords}. Max 3 sentences."}
        ]
    )
    
    return jsonify({"description": message.content[0].text})

if __name__ == '__main__':
    app.run()