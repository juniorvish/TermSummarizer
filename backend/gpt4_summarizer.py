import openai

def summarize_terms(url):
    openai.api_key = "your_openai_api_key"

    user_message = f"Summarize the terms of service and provide a safety remark for the following URL: {url}"
    prompt = f"User: {user_message}\nAI Developer:"

    message = []
    message.append({"role": "system", "content": "You are a friendly AI Developer"})
    message.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        temperature=0.2,
        max_tokens=4000,
        frequency_penalty=0.9
    )

    gpt_message = response.choices[0].message.content

    summary, safety_remark = extract_summary_and_safety_remark(gpt_message)

    return summary, safety_remark


def extract_summary_and_safety_remark(gpt_message):
    lines = gpt_message.split("\n")
    summary = ""
    safety_remark = ""

    for line in lines:
        if line.startswith("Summary:"):
            summary = line[len("Summary:"):].strip()
        elif line.startswith("Safety Remark:"):
            safety_remark = line[len("Safety Remark:"):].strip()

    return summary, safety_remark