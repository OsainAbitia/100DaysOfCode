## Summary

Before running this script make sure to configure the following attributes. First, for
Gmail accounts, make sure to turn 2FA so you can create `App Passwords` inside `Settings > 
Manage your Google account > Security >  Signing in to Google > App Passwords`. Create 
Another type of app and enter the name of your app.

Once you've crated a password save it in a secure place and next add to your environment
the following values

+ EMAIL_FROM
+ EMAIL_PASSWORD
+ EMAIL_TO

Run the script.

### Side notes
By default, this script uses Gmail to create the SMTP server, for new providers check your
security settings and after testing the code, check your spam.