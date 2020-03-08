# Kenmare Car Share

![alt text](https://i.imgur.com/VDbJ15b.jpg "Kenmare Car Share as seen on different devices")

Being a local Kenmare resident, I asked a question on a local Facebook group about any websites that people might find helpful in the community. A 'carpooling' site was one of the ideas given and so I have begun work on Kenmare Car Share.

The aim of the project at the moment is to have the minimum necessary functionality for it to be a live website that people could actually use and gain benefit from. It also needs to meet the requirements of CRUD - create, read, update and delete.

It is hoped that residents from in and around Kenmare will come to see it as a resource for reducing the number of duplicate vehicle journeys being made, raising environmental awareness and fostering community spirit.

There are many prospects for progressive enhancement of the website in the future, which are outlined later in this document.

## UX

The website should do 'exactly what it says on the tin'. The main **Latest Lifts** page will display the most recently posted lift requests or offers, including: the date of the journey; start and finish locations; some further journey details; and the ability to reply, edit or delete.

The ability to reply should be very straightforward for users. Click on one button and they are taken to a form containing all the original details of the lift posting, plus a field for entering their reply. Click 'submit' and they go straight back to the main page, where they can see their reply has been added to the listing. 

Likewise, the same simplicity of functionality should apply to adding and editing a listing. The **Add a Lift** form will have text area, dropdown and select fields, each with some clear explanatory text indicating their purpose. A 'datepicker' is included for added ease of use.

A specific list of **Where from?** and **Where to?** locations have been pre-defined for the introductory phase of the website.

The whole process should be very simple and straightforward - in essence, it could take just three user interactions with the site for a 'car share' to be arranged.
* User adds new lift offer or request
* Second user replies to take up the offer, or say they can provide a lift when a request has been made
* Original user is satisfied with the reply and both parties can agree to make further contact privately

### User Stories

* I make the same journey from Kenmare to Killarney every day. Some days I could do with some company on the drive, some days I could do with not driving at all. Can I find someone else who does the same journey around the same time?

![alt text](https://i.imgur.com/5OaNbf8.jpg "Kenmare Car share screenshot")
* I need to get to Kerry Airport, I wonder if there's anyone who is already driving in that direction on the same day as my flight?

![alt text](https://i.imgur.com/fNhWtBb.jpg "Kenmare Car share screenshot")
* I drive around the area quite a lot, maybe there are people asking for lifts to the same places as me on the same days?

![alt text](https://i.imgur.com/gumjUKv.jpg "Kenmare Car share screenshot")

I used Balsamiq to create some wireframes for the project. They illustrate that the idea was clear from the outset and the development and final product have been consistent with the concept. 
The prospect of a **Browse lifts** page has been moved back to **Features left to implement**.

![alt text](https://i.imgur.com/OYisCQ2.jpg "Kenmare Car Share wireframe")
![alt text](https://i.imgur.com/3vowRyk.jpg "Kenmare Car Share wireframe")

## Features

### Existing features

* The navbar and dropdown burger menu have options to **Offer/request a lift** and also one for **Contact**, which is a simple href link for opening up a user's messaging client with the 'send to' email address field pre-populated.
* The landing page uses Bootstrap card deck functionality to display the latest lifts ordered by most recent. A limit can be applied to the number of cards shown, which was set to 6 at the time of writing.
* On the individual lift cards:
    * Different icons are used for either 'request a lift' or 'offer a lift'.
    * Each listing also contains a date of travel, start and finish locations, some journey details, options to reply/edit/delete and an expandable/collapsible area to show/hide replies.
    * Because authentication was not compulsory for this project, the edit/delete functions of the CRUD requirements are universal and can currently be seen/activated by all users. This is addressed in the **Features left to implement** section of this document.
    * Any replies to lift posts are formatted with a date and timestamp; they appear in chronological order from first down to most recent.
* The main page also features a **Back to top** button which is activated upon a defined window scroll point. When clicked it returns the user to the top of the page. This is primarily a helpful piece of functionality for mobile users.
* The menu option **Offer/request a lift** takes the user to a page for adding a lift, which has a form containing:
    * Three dropdown 'select' menus.
    * A text area for adding some brief journey details.
    * A datepicker.
    * Submit button.
* Upon clicking submit, the user is redirected to the main **Latest lifts** page and their listing will be automatically added at the top as the most recent.
* Selecting 'Reply' from a lift post on the main page takes the user to a page for adding a reply, which has a form containing:
    * Three disabled dropdown menus.
    * A disabled text area.
    * Disabled datepicker.
        * All the above are pre-populated with the relevant details from the original lift post.
    * A text area for entering a reply.
    * Submit button.
* Upon clicking submit, the user is redirected to the main **Latest lifts** page and they will be able to expand the **Show/hide replies** section of the relevant lift to see that their reply has been posted.
* Selecting 'Edit' from a lift post on the main page takes the user to a page for editing a lift, which has a form containing:
    * Three dropdown 'select' menus.
    * A text area for adding some brief journey details.
    * A datepicker.
    * Submit button.
* All these fields can be edited; then, upon clicking submit, the user is redirected to the main **Latest lifts** page where they can see their edits have taken effect and been published.
* Selecting 'Delete' from a lift post completely removes the listing.

### Notes

* The datepicker currently returns lift posts with a date format of MM/DD/YY, whereas the automated date and timestamp returns DD/MM/YY. This is a known issue and will be addressed in the future.
* Editing a lift which has had replies posted on it has a known bug whereby the replies are deleted but the **Posted at** text remains. As and when authentication has been implemented for the site, only the original user will be able to edit/delete their own posts. If this 'deleted replies' bug still remains at this time, the registered user will be advised not to edit the original listing but to post any amendments in the form of another reply.

### Features left to implement

* 'Sort by' checkboxes for the main page, e.g. **show only offers**, **show only requests**, **show all lifts**.
* When a location is selected in the **Where from?** dropdown, it should then either be removed or disabled as an option in the **Where to?** menu.
* The site could have a mapping element, whereby documents in the MongoDB locations collection are given latitude and longitude values, allowing chosen locations for a lift to be pinned on a map using the Google Maps API.
* A **Browse lifts** page could contain all active lift postings, with search filters to narrow the results down by location or date of travel, for example.
* An authentication system for registered users should be set up, so that: 1) only the person who added a lift can edit or delete it, and: 2) for added security and peace of mind for users.
* This system could also be extended to send notifications to registered users when a reply is left on their post.

## Technologies

This project uses HTML, CSS, JavaScript, jQuery, Python/Flask and MongoDB.
It utilises the Bootstrap framework and library, plus a [datepicker from GIJGO](https://gijgo.com/datepicker) and Font Awesome for icons.

## Testing

1. Navbar
    * Clicking on the site logo redirects to the main page.
    * Clicking on **Offer/request a lift** redirects correctly to */add-lift*.
    * Clicking on **Contact** opens the user's default messaging client, with the 'send to' field pre-populated with the correct email address.
    * In mobile view, the burger icon correctly displays the dropdown menu. The menu links behave in the expected way, as above.
    
2. **Latest lifts** page
    * The listings appear and update in 'most recently posted' order, with a limit on the number shown as set in line 24 of the app.py file.
    * Different icons are displayed for **Request a lift** and **Offer a lift**.
    * The **when**, **from** and **to** fields are correctly populated as per the entered database information.
    * **Show journey details** is expandable/collapsible, with a down or up arrow displayed as appropriate. The correct user-inputted text is shown when the section is opened.
    * 'Reply' button redirects to a *reply_to* URL with the relevant document ID.
    * 'Edit' button redirects to an *edit_lift* URL with the relevant document ID.
    * 'Delete' button removes the listing entirely from the site and database.
    * **Show/hide replies** is expandable/collapsible, with a down or up arrow displayed as appropriate. The correct user-inputted comments are shown when the section is opened.
    * The comments are displayed chronologically from first to most recent, with the correct time and date shown.
    * On mobile view (and other devices when the main page content extends beyond the viewport) a **Back to top** button appears at a defined scroll point. When clicked it returns the user to the top of the page.

3. **Add a lift** page
    * Trying to submit the form without completing any of the fields brings up the 'Please select an item in the list' error message. This message is replicated for each incomplete field, until all form requirements have been met and the user can then submit.
    * The first dropdown has options to **Offer a lift** or **Request a lift**.
    * The **Where from?** dropdown has a number of locations to choose from.
    * The **Where to?** dropdown has the same list of locations to choose from.
    * The text area contains some placeholder text which is removed when the user starts typing. There is a 150-character limit and the text area cannot be resized by the user. NB: the limit on number of characters can of course be revisited if user feedback suggests a need to do so.
    * Clicking in the **Select date of journey** field brings up a datepicker. The relevant date can be correctly selected and inputted into the field.
    * Clicking 'Submit' takes the user back to the **Latest lifts** page, where their post has been added to the top of the listings. 

4. **Reply to a lift** page
    * The three dropdown menus, text area and datepicker field are all pre-populated with the relevant lift details. These all have editing disabled on them.
    * The text area contains some placeholder text which is removed when the user starts typing. There is a 150-character limit and the text area cannot be resized by the user.
    * Clicking 'Submit' takes the user back to the **Latest lifts** page. If they click the **Show/hide replies** option, their comment will be displayed with a date and timestamp.

5. **Edit your lift** page
    * The three dropdown menus, text area and datepicker field are all pre-populated with the relevant lift details. 
    * The **Where from?**, **Where to?**, text area and datepicker fields can be amended.
    * Clicking 'Submit' takes the user back to the **Latest lifts** page, where the details of the lift have been updated as per the edits made.
    
6. 'Delete' button
    * Clicking the 'Delete' button on any listing immediately removes it from the website and MongoDB database. The user remains on the **Latest lifts** page, with another older listing coming 'back up' into the view (unless there are no further lifts to display).

The site was manually viewed and tested in the Chrome and Firefox browsers on a Windows 10 laptop, as well on iOS and Android mobile/tablet devices.

This was done with a view to ensuring that: all functions and interactivity respond appropriately on both mobile and desktop; responsive changes in the navbar and site layout are all present and correct for different devices; and the site remains fully functional, useable and well presented across all screen sizes.

I also ran my code through the W3C validator tools for HTML/CSS, as well as JSHint for Javascript and http://pep8online.com for Python.

## MongoDB schema

My database has two collections - lifts and locations.

**Lifts** contains all the keys and values which are mapped over to the listings on the main page of the site, including a 'comments' array containing a number of objects as per the number of replies submitted on a lift posting on the site.

![alt text](https://i.imgur.com/mRi0ztE.jpg "MongoDB database screenshot")

**Locations** includes a number of documents each containing a single location name as a string.

![alt text](https://i.imgur.com/myQRDjb.jpg "MongoDB database screenshot")

## Deployment

* I created a new app in Heroku called *kenmare-car-share* with the region selected as 'Europe'.
* I then ran *heroku login* in the Gitpod CLI and followed the instructions for logging into Heroku.
* I then ran *heroku apps* in the CLI to confirm that *kenmare-car-share* was listed.
* I then ran *heroku git:remote -a kenmare-car-share* in order to set my Heroku app as the remote master branch.
* I then ran *pip3 freeze > requirements.txt* in order for Heroku to know the requirements for running the app.
* I then ran *echo web: python app.py > Procfile*, which tells Heroku to refer to my 'app.py' file in order to begin running the application.
* I then ran *git add*, *git commit* and *git push heroku master* to send everything to the remote repository.
* I then ran *heroku ps:scale web=1* to tell Heroku to start running the app.
* In my Heroku app, I navigated to *Settings > Reveal Config Vars* - I specified my IP and PORT and MONGO_URI here.
* I then clicked 'Open app' and my website was deployed live to https://kenmare-car-share.herokuapp.com.
* I created an *env.py* file containing my MONGO_URI environment variable, with the variable then used in the corresponsing path in my *app.py* file. *Env.py* is also referenced in a *.gitignore* file in order to mask password details.
* In order to clone this project, you should paste https://github.com/digitalstuart/kenmare-car-share.git into your chosen editor's terminal. Then type *git remote rm origin* into the terminal to sever the link with the original.
* You would also need to create your own MONGO_URI variable, env.py and .gitignore file.

## Credits

### Content

* The datepicker was sourced from https://gijgo.com/datepicker/example/bootstrap-4.
* For scrolling to the top with a **Back to top** button, I referred to https://www.w3schools.com/howto/howto_js_scroll_to_top.asp.

### Acknowledgements

Code Institute tutor Tim Nelson was a very wise and patient man as he helped me learn and navigate the worlds of MongoDB, Python, Jinja and Flask. Likewise, my project mentor Aaron Sinnott was a lifesaver with helping me understand how to get show/hide functionality with Jinja auto-generated elements. Thanks also to members of the 'Kenmare Community Chat' Facebook page for being the inspiration behind this project! 