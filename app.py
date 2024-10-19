from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# Load your main DataFrame (e.g., from a CSV or Google Sheets)
df = pd.read_csv('responses.csv')  # Replace with your DataFrame loading logic
gameDevPrioColumn = "In the case that you are considered as first priority for AI, Hack, or Design, would you prioritize Game Development at the same, lower, or higher level?"

filterCols = ((df[gameDevPrioColumn] != "Lower") & (df["Would you like to opt-in to be considered for Game Development this Fall?"] == "Yes") & (df["Have you previously participated in ACM Projects?"] == "No"))

generalColumns = df.columns[:18]
aiColumns = df.columns[18:18+8]
designColumns = df.columns[26:26+9]
hackColumns = df.columns[35:40]
gameDevColumns = df.columns[40:43]
otherColumns = df.columns[43:]

# Filtered DataFrame (this can be based on any logic, preserving the original indices)
filtered_df = df[filterCols]

# Index to track current response being viewed
current_index = 0

@app.route('/')
def index():
    global current_index, filtered_df
    
    # Get the current person's responses
    person_responses = filtered_df.iloc[current_index].to_dict()

    # Render the template with responses
    return render_template('index.html', responses=person_responses, index=current_index + 1, total=len(filtered_df))

@app.route('/next')
def next_entry():
    global current_index, filtered_df
    
    # Move to the next entry
    current_index += 1
    if current_index >= len(filtered_df):
        current_index = 0  # Loop back to the first entry
    
    # Redirect to index to display the next entry
    return redirect('/')

@app.route('/back')
def previous_entry():
    global current_index, filtered_df
    
    # Move to the previous entry
    current_index -= 1
    if current_index < 0:
        current_index = len(filtered_df) - 1  # Loop back to the last entry
    
    # Redirect to index to display the previous entry
    return redirect('/')

@app.route('/save_comment', methods=['POST'])
def save_comment():
    global df, filtered_df
    
    # Get the new comment and the current index in filtered_df
    new_comment = request.form['comment']
    filtered_index = int(request.form['index'])  # Index in filtered_df
    
    # Get the corresponding index in the original df
    original_index = filtered_df.index[filtered_index]
    
    # Update the original df at the correct row and column
    df.at[original_index, 'Comments (Alan):'] = new_comment

    # Save the updated original df back to the CSV file
    df.to_csv('responses.csv', index=False)

    # Update the filtered_df with the latest data from df to reflect the changes
    filtered_df = df[filterCols]
    
    # Redirect back to the current page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
