#!/usr/bin/env python3
import os
import time
import random
import subprocess
from datetime import datetime, timedelta
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

def setup_git_config():
    """Make sure git is configured properly in the directory."""
    # Check if we're in a git repository
    try:
        subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], 
                      check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Git repository already initialized.")
    except subprocess.CalledProcessError:
        print("Initializing git repository...")
        subprocess.run(["git", "init"], check=True)
    
    # Check if user.name and user.email are configured
    try:
        name = subprocess.run(["git", "config", "user.name"], 
                            check=True, stdout=subprocess.PIPE).stdout.decode().strip()
        email = subprocess.run(["git", "config", "user.email"], 
                             check=True, stdout=subprocess.PIPE).stdout.decode().strip()
        
        if not name or not email:
            raise ValueError("Git user.name or user.email not configured")
            
    except (subprocess.CalledProcessError, ValueError):
        print("Please configure git user.name and user.email:")
        name = input("Enter git username: ")
        email = input("Enter git email: ")
        
        subprocess.run(["git", "config", "user.name", name], check=True)
        subprocess.run(["git", "config", "user.email", email], check=True)
    
    # Check for remote repository
    try:
        remote = subprocess.run(["git", "remote", "-v"], 
                              check=True, stdout=subprocess.PIPE).stdout.decode().strip()
        if not remote:
            raise subprocess.CalledProcessError(1, "git remote")
    except subprocess.CalledProcessError:
        print("No remote repository configured.")
        remote_url = input("Enter remote repository URL (e.g., git@github.com:username/repo.git): ")
        if remote_url:
            subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        else:
            print("Warning: No remote repository set. Commits will be local only.")

def generate_python_qa(model):
    """Generate a Python question and answer using Google Gemini API."""
    prompt = """Create a Python coding question and its detailed solution.
    
    Format your response as follows:
    
    ```python
    # Python Question: [Title of the question]
    '''
    [Detailed problem statement]
    
    Example:
    Input: [example input]
    Output: [expected output]
    '''
    
    # Solution
    def solution():
        # [Your implementation]
        # [Include detailed comments explaining the approach]
        pass  # Replace with actual solution
    
    # Test cases
    def test_solution():
        # [Several test cases to verify the solution]
        pass
    
    if __name__ == "__main__":
        test_solution()
    ```
    
    Make sure the question is challenging but solvable, and the solution is well-commented.
    Only return the code, no explanations outside the code block.
    """
    
    response = model.generate_content(prompt)
    
    # Extract code from response
    content = response.text
    
    # Clean up response to get just the Python code
    if "```python" in content:
        code = content.split("```python")[1].split("```")[0].strip()
    elif "```" in content:
        code = content.split("```")[1].strip()
    else:
        code = content.strip()
    
    return code

def get_next_file_number(python_dir):
    """Determine the next file number by checking existing files in the python directory."""
    if not os.path.exists(python_dir):
        return 1
    
    # Get all python question files
    existing_files = [f for f in os.listdir(python_dir) 
                     if f.startswith("python_question_") and f.endswith(".py")]
    
    if not existing_files:
        return 1
    
    # Extract numbers from filenames
    numbers = []
    for filename in existing_files:
        try:
            # Extract number between "python_question_" and ".py"
            number_str = filename.replace("python_question_", "").replace(".py", "")
            number = int(number_str)
            numbers.append(number)
        except ValueError:
            continue
    
    # Return highest number + 1, or 1 if no valid numbers found
    return max(numbers) + 1 if numbers else 1

def create_python_file(content, file_number):
    """Create a Python file with the generated content in the python directory."""
    # Ensure python directory exists relative to current working directory
    python_dir = os.path.join(os.getcwd(), "Python")
    if not os.path.exists(python_dir):
        os.makedirs(python_dir)
    
    # Get the next available file number
    next_number = get_next_file_number(python_dir)
    filename = os.path.join(python_dir, f"python_question_{next_number}.py")
    
    with open(filename, "w") as f:
        f.write(content)
    
    return filename

def commit_and_push(filename, commit_date=None):
    """Add, commit, and push the file to Git."""
    # Add the file
    subprocess.run(["git", "add", filename], check=True)
    
    # Commit with specified date if provided
    commit_command = ["git", "commit"]
    if commit_date:
        commit_command.extend(["--date", commit_date])
    commit_command.extend(["-m", f"Add Python question: {os.path.basename(filename)}"])
    
    subprocess.run(commit_command, check=True)
    
    # Try to push
    try:
        subprocess.run(["git", "push", "origin", "main"], check=False)
    except subprocess.CalledProcessError:
        try:
            # If main branch doesn't exist, try master
            subprocess.run(["git", "push", "origin", "master"], check=False)
        except subprocess.CalledProcessError:
            print("Warning: Could not push to remote. Check your branch name and remote configuration.")

def get_date_list():
    """Return the hardcoded list of dates."""
    # You can modify this list with your specific dates
    dates = [
        "2024-06-27",
        "2024-06-29",
        "2024-07-02",
        "2024-07-03",
        "2024-07-04",
        "2024-07-07",
        "2024-07-11",
        "2024-07-13",
        "2024-07-14",
        "2024-07-15",
        "2024-07-19",
        "2024-07-21",
        "2024-07-26",
        "2024-07-28",
        "2024-07-29",
        "2024-07-30",
        "2024-08-06",
        "2024-08-07",
        "2024-08-09",
        "2024-08-11",
        "2024-08-14",
        "2024-08-15",
        "2024-08-16",
        "2024-08-20",
        "2024-08-22",
        "2024-08-23",
        "2024-08-26",
        "2024-08-27",
        "2024-08-30",
        "2024-09-01",
        "2024-09-02",
        "2024-09-06",
        "2024-09-09",
        "2024-09-12",
        "2024-09-13",
        "2024-09-18",
        "2024-09-19",
        "2024-09-21",
        "2024-09-26",
        "2024-09-29",
        "2024-10-02",
        "2024-10-05",
        "2024-10-08",
        "2024-10-09",
        "2024-10-10",
        "2024-10-13",
        "2024-10-17",
        "2024-10-18",
        "2024-10-19",
        "2024-10-23",
        "2024-10-26",
        "2024-10-28",
        "2024-10-29",

        # Add more dates as needed
    ]
    return dates

def main():
    print("Python Question Generator with Git Integration")
    print("---------------------------------------------")
    
    # Configure Google Gemini API
    try:
        # Get API key for Google Gemini
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            api_key = input("Enter your Google API key: ")
            os.environ["GOOGLE_API_KEY"] = api_key
        
        # Configure the Google Gemini API
        genai.configure(api_key=api_key)
        
        # Set up safety settings to avoid filtering code
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        }
        
        # Initialize Gemini model (using the free model)
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash", 
            safety_settings=safety_settings,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            }
        )
        print("Successfully connected to Google Gemini API")
    except Exception as e:
        print(f"Error setting up Google Gemini API: {e}")
        return
    
    # Setup Git
    setup_git_config()
    
    # Get the hardcoded list of dates
    date_list = get_date_list()
    print("\nUsing the following commit dates:")
    for i, date in enumerate(date_list):
        print(f"{i+1}. {date}")
    
    # Alternating pattern of files per date (10, 15, 10, 15, ...)
    files_per_date = [14, 16]
    
    # Process each date
    total_files = 0
    
    for date_index, date in enumerate(date_list):
        # Determine how many files to generate for this date
        num_files = files_per_date[date_index % len(files_per_date)]
        print(f"\n====== Date: {date} ======")
        print(f"Generating {num_files} Python questions for this date")
        
        # Generate files for this date
        for i in range(1, num_files + 1):
            total_files += 1
            print(f"\nGenerating Python question {i}/{num_files} for {date} (total: {total_files})...")
            
            # Generate Python Q&A
            content = generate_python_qa(model)
            
            # Create Python file
            filename = create_python_file(content, total_files)
            print(f"Created file: {filename}")
            
            # Add random time to date for more realistic commits
            hour = random.randint(9, 17)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            commit_date = f"{date} {hour:02d}:{minute:02d}:{second:02d}"
            
            # Commit and push
            print(f"Committing with date: {commit_date}")
            commit_and_push(filename, commit_date)
            
    
    print(f"\nAll done! Successfully generated, committed, and pushed {total_files} Python questions.")

if __name__ == "__main__":
    main()