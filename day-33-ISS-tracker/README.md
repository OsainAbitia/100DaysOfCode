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

Run the script. It will keep running and checking every 60 seconds for new updates to notify 
you when the ISS is above you. Once the script is running press `Ctrl + C` to stop its execution.

## What you can learn here

- API Calls

### API credits

- ISS tracker: http://api.open-notify.org
- Sunrise-Sunset: http://api.sunrise-sunset.org

### Side notes
By default, this script uses Gmail to create the SMTP server, for new providers check your
security settings and after testing the code, check your spam.
