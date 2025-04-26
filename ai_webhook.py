from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# ضع هنا مفتاح OpenAI الخاص بك
openai.api_key = "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"

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    # إرسال السؤال إلى OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",  # أو gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "أنت مساعد ذكي لموظفي Odoo."},
            {"role": "user", "content": question}
        ]
    )

    answer = response['choices'][0]['message']['content']

    # نرجع الإجابة
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
