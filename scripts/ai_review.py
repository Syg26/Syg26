import os
from openai import OpenAI

# Initialize client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_code(diff):
    prompt = f"""
You are a senior DevOps engineer.

Review the following code diff and:
- Identify bugs
- Suggest improvements
- Highlight security risks

Code:
{diff}
"""

    # Use new SDK interface
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert DevOps reviewer"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    # Extract AI response text
    return response.choices[0].message.content

if __name__ == "__main__":
    # Read code diff from file
    with open("diff.txt", "r") as f:
        diff = f.read()

    # Get AI review
    review = review_code(diff)

    # Save review to file
    with open("review.txt", "w") as f:
        f.write(review)
