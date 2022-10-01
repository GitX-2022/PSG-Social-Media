# Eventique

Eventique is a club events management tool for the college and provides a handful of features.

### Admin Tools
- Add Events
- Generate Certificates for Events
- Book Rooms for Events

### User Interface
- View Profile
- View Upcoming Events and have alerts for the same
- View Event Ticket (Gimmick for Event Promotion)
- Enroll for an Event
- View Booked Rooms at the College
- Locker for Issued Certificates
- Readymade certificate template for auto-generation

### Common Features
- Use Server-Based Instant Messaging to interact with one another
- Edit Profile Settings
- Log In//Sign Up
- E-Mail OTP Based Sign Up Verification
- E-Mail OTP Based Forgot Password Feature

## API

The Application Programming Interface for Eventique provides 3 features:
- Retrieve booked rooms
- Log In to the Application in order to
	- Retrive My Events
	- Retrive Event Ticket

### Usage

To use the API, just call the relevant API Endpoints.

```bash
curl {APP_HOST}/api/rooms  # this will fetch a list of all booked rooms

curl --data "rollno={ROLLNUMBER}&password={PASSWORD}" {APP_HOST}/api/login # this will log the user into the app using session cookies. a headless browserr may not achieve the task at all times

curl {APP_HOST}/api/events # this will fetch a list of events the user has signed up for

curl {APP_HOST}/api/ticket/{EVENT_ID} # this will return a PNG of the event ticket, which can be used for promotions
```

## Tech Stack Used
- Python3-Flask
- Python3-json
- Python3-Pillow
- Vanilla HTML
- Material Design Lite for Cascading Style Sheets
- Vanilla Java Script
- GUnicorn
- NGINX Server
- PIL//Pillow (Python Imaging Library)

## Documentation
- <a href="https://getmdl.io/started/index.html">Material Design Lite</a>
- <a href="https://flask.palletsprojects.com/en/2.2.x/">Python3-Flask</a>
- <a href="https://gunicorn.org/#docs">GUnicorn</a>
- <a href="https://nginx.org/en/docs/">NGINX</a>
- <a href="https://pillow.readthedocs.io/en/stable/">Pillow</a>

## Authors
- <a href="https://github.com/aadityarengarajan">@aadityarengarajan | Aaditya Rengarajan</a>
- <a href="https://github.com/RWXogenisis">@RWXogenisis | S Karun Vikhash</a>
- <a href="https://github.com/Sanjaykumaar0603">@Sanjaykumaar0603 | Sanjay Kumaar</a>
- <a href="https://github.com/BoomBoy4U">@BoomBoy4U | Ajay Ramesh</a>
<br/>
THIS REPOSITORY WAS MADE AS A PART OF PSG GITHUB CAMPUS CLUB'S GitX HACKATHON.
