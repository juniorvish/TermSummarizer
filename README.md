# TermSummarizer

TermSummarizer is an app that takes a terms of service URL as input and provides a summary along with a safety remark, indicating whether it's safe to sign up for the product or not.

## Installation

1. Clone the repository:

```
git clone https://github.com/juniorvish/TermSummarizer.git
```

2. Change directory to the project folder:

```
cd TermSummarizer
```

3. Install the required Python packages:

```
pip install -r backend/requirements.txt
```

## Usage

1. Start the backend server:

```
python backend/app.py
```

2. Open the `frontend/index.html` file in your web browser.

3. Enter the terms of service URL in the input field and click the "Submit" button.

4. The app will display a summary of the terms of service and a safety remark.

## Project Structure

- `frontend/index.html`: The main HTML file for the frontend.
- `frontend/css/tailwind.css`: The Tailwind CSS file for styling the frontend.
- `frontend/js/main.js`: The JavaScript file for handling user interactions and API requests.
- `backend/app.py`: The main Python file for the backend server.
- `backend/requirements.txt`: The list of required Python packages.
- `backend/gpt4_summarizer.py`: The Python file for interacting with the GPT-4 model.

## Shared Dependencies

1. Exported variables:
   - summary (from app.py to main.js)
   - safety_remark (from app.py to main.js)

2. Data schemas:
   - API request: {url: string}
   - API response: {summary: string, safety_remark: string}

3. ID names of DOM elements:
   - terms_url_input (input field for terms of service URL)
   - submit_button (button to submit the URL)
   - summary_output (div to display the summary)
   - safety_output (div to display the safety remark)

4. Message names:
   - user_message (input from the user)
   - gpt_message (response from GPT-4)

5. Function names:
   - summarize_terms (in app.py)
   - submit_url (in main.js)
   - display_summary (in main.js)
   - display_safety_remark (in main.js)