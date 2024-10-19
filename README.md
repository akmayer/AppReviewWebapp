# AppReviewWebapp

A basic flask app that displays a .csv containing information for multiple applicants, one applicant per row with columns as prompts and cells as responses.

Usually taken from a google forms automatically generated csv but should work quite generally if modified.

This one is specifically used for ACM UCSD Projects review which is the reason for some of the filtering in the apps.py.

A `responses.csv` form is needed in the top level directory but is not provided since that is information I should not be sharing.

Run by navigating to the top level directory and running `python app.py` then opening the locally hosted webapp.

The web app will look like this:

![image](https://github.com/user-attachments/assets/7ab8f9ad-981b-4262-a332-bbb8717d907e)


And allow for a reviewer response section which can be used to edit the `responses.csv` directly with the reviewer inputted response:

![image](https://github.com/user-attachments/assets/763ed4f0-b8fa-48ad-a19c-6071cb7777d0)

