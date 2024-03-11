from flask import Flask, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
from core.ocr import *
from utils.filter import *

load_dotenv()

genai.configure(api_key=os.getenv("GENAI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
pipeline = model.start_chat()
app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    # Check if an image file is present in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'})

    image = request.files['image']

    # Process the image here
    # You can use libraries like OpenCV or PIL to handle image processing tasks
    
    data = ocr(image)
    data = pipeline.send_message(data + "\n Seeing this data, extract a list of items from the receipt and put them in a json format like this: {\"items\": {\"item1\": item1_price , \"item2\": item1_price, \"item3\": item1_price}}  Use the exact item names used in the text. If you can't find any items, just put an empty json like this: {\"items\": {}} also IF there are taxes or discounts, add them to the json as well. If you can't find any taxes or discounts, just put an empty json like this: {\"taxes\": {}, \"discounts\": {}}")
    data = filter_json(data.text)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)


