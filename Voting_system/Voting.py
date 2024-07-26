
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dictionary to store candidate votes
candidate_votes = {
    "Candidate1": 0,
    "Candidate2": 0,
    "Candidate3": 0
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    candidate_name = request.form.get('candidate')
    if candidate_name in candidate_votes:
        candidate_votes[candidate_name] += 1
        return jsonify({"message": f"Vote for {candidate_name} recorded."})
    else:
        return jsonify({"message": "Invalid candidate name."}), 400

@app.route('/results', methods=['GET'])
def results():
    return jsonify(candidate_votes)

if __name__ == '__main__':
    app.run(debug=True)





# import tkinter as tk
# from tkinter import messagebox

# # Dictionary to store candidate votes
# candidate_votes = {
#     "Candidate1": 0,
#     "Candidate2": 0,
#     "Candidate3": 0
# }

# def vote_for_candidate():
#     candidate_name = candidate_var.get()
#     if candidate_name in candidate_votes:
#         candidate_votes[candidate_name] += 1
#         messagebox.showinfo("Success", f"Vote for {candidate_name} recorded.")
#     else:
#         messagebox.showerror("Error", "Invalid candidate name.")

# def get_results():
#     results = "\n".join(f"{candidate}: {votes}" for candidate, votes in candidate_votes.items())
#     messagebox.showinfo("Results", results)

# # Create the main window
# root = tk.Tk()
# root.title("Voting System")

# # Create and place widgets
# tk.Label(root, text="Select a candidate to vote:").pack(pady=10)

# candidate_var = tk.StringVar(value="Candidate1")
# candidates = ["Candidate1", "Candidate2", "Candidate3"]

# for candidate in candidates:
#     tk.Radiobutton(root, text=candidate, variable=candidate_var, value=candidate).pack(anchor=tk.W)

# tk.Button(root, text="Vote", command=vote_for_candidate).pack(pady=5)
# tk.Button(root, text="Show Results", command=get_results).pack(pady=5)

# # Run the application
# root.mainloop()


