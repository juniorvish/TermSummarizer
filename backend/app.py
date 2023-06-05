from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "your_openai_api_key"

def summarize_terms(url):
    user_message = f"Summarize the terms of service at this URL: {url} and provide a safety remark."
    prompt = f"User: {user_message}\nAI Developer:"

    message = []
    message.append({"role": "system", "content": "You are a friendly AI Developer"})
    message.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(model="gpt-4",
                                            messages=message,
                                            temperature=0.2,
                                            max_tokens=4000,
                                            frequency_penalty=0.9)
    gpt_message = response.choices[0].message.content

    return gpt_message

@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    data = request.get_json()
    url = data['url']
    gpt_message = summarize_terms(url)

    summary, safety_remark = gpt_message.split("\n")[:2]

    return jsonify({"summary": summary, "safety_remark": safety_remark})

if __name__ == '__main__':
    app.run(debug=True)