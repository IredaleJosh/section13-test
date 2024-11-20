from app import app

# When Deploying - Ensure NOT calling app.run()
# Why? will crash app and give 504 error, as not using Flask's built-in
# server
# PythonAnywhere uses WSGI instead

# Makes it so only run when file itslef ran directly
# Can run locally when using "flask run" command

if __name__ == '__main__':
    app.run(debug=True)