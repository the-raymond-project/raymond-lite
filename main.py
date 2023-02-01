from flask import Flask, request
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Meditation Instruction Website!"

@app.route("/meditation_instructions", methods=["GET", "POST"])
def meditation_instructions():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).get("choices")[0].text
        return response
    return "Please provide a prompt to generate meditation instructions."

if __name__ == "__main__":
    app.run()
