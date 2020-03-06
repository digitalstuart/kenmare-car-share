# Kenmare Car Share

![alt text](https://i.imgur.com/VDbJ15b.jpg "Kenmare Car Share as seen on different devices")

Being a local Kenmare resident, I asked a question on a local Facebook group about any websites that people might find helpful in the community. A 'carpooling' site was one of the ideas given and so I have begun work on Kenmare Car Share.

The aim of the project at the moment is to have the minimum necessary functionality for it to be a live website that people could actually use and gain benefit from. It also needs to meet the requirements of CRUD - create, read, update and delete.

It is hoped that residents from in and around Kenmare will come to see it as a resource for reducing the number of duplicate vehicle journeys being made, raising environmental awareness and fostering communmity spirit.

There are many prospects for progressive enhancement of the website in the future, which are outlined later in this document.

## UX

The website should do 'exactly what it says on the tin'. The main 'Latest Lifts' page will display the most recently posted lift requests or offers, including: the date of the journey; start and finish locations; some further journey details; and the ability to reply, edit or delete (see footnote *1).

The ability to reply should be very straightforward for users. Click on one button and they are taken to a form containing all the original details of the lift posting, plus a field for entering their reply. Click 'submit' and they go straight back to the main page, where they can see their reply has been added to the listing. 

Likewise, the same simplicity of functionality should apply to adding and editing a listing. The 'Add a Lift' form will have text area, dropdown and select fields, each with some clear explanatory text indicating their purpose. A 'datepicker' is included for added ease of use.

A specific list of 'where from' and 'where to' locations have been pre-defined for the introduction of the website.

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

I used Balsamiq to create some wireframes for the project. They illustrate that the project idea was clear from the outset and the development and final product have been consistent with the concept. 
The prospect of a 'Browse lifts' page has been moved back to 'Features left to implement'.

![alt text](https://i.imgur.com/OYisCQ2.jpg "Kenmare Car Share wireframe")
![alt text](https://i.imgur.com/3vowRyk.jpg "Kenmare Car Share wireframe")

## Features

### Existing features

* The navbar and dropdown burger menu have options to 'Offer/request a lift' and also one for 'Contact', which is a simple href link for opening up a user's messaging client with the 'send to' email address field pre-populated.
* The landing page uses Bootstrap card deck functionality to display the 'latest lifts' ordered by most recent. A limit can be applied to the number of cards shown, which was set to 6 at the time of writing.
* On the individual lift cards:
    * Different icons are used for either 'request a lift' or 'offer a lift'.
    * Each listing also contains a date of travel, start and finish locations, some journey details, options to reply/edit/delete and an expandable/collapsible area to show/hide replies.
    * Because authorisation was not compulsory for this project, the edit/delete functions of the CRUD requirements are universal and can currently be seen/activated by all users. This is addressed in the 'Features left to implement' section of this document.
    * Any replies to lift posts are formatted with a date and timestamp; they appear in chronological order from first down to most recent.
* The main page also features a 'back to top' button which is activated upon a defined window scroll point. When clicked it returns the user to the top of the page. This is primarily a helpful piece of functionality for mobile users.
* The menu option 'Offer/request a lift' takes the user to a page for adding a lift, which has a form containing:
    * Three dropdown 'select' menus.
    * A text area for adding some brief journey details.
    * A datepicker.
    * Submit button.
* Upon clicking submit, the user is redirected to the main 'Latest lifts' page and their listing will be automatically added at the top as the most recent.
* Selecting 'Reply' from a lift post on the main page takes the user to a page for adding a reply, which has a form containing:
    * Three disabled dropdown menus.
    * A disabled text area.
    * Disabled datepicker.
        * All the above are pre-populated with the relevant details from the original lift post.
    * A text area for entering a reply.
    * Submit button.
* Upon clicking submit, the user is redirected to the main 'Latest lifts' page and they will be able to expand the 'show/hide replies' section of the relevant lift to see that their reply has been posted.
* Selecting 'Edit' from a lift post on the main page takes the user to a page for editing a lift, which has a form containing:
    * Three dropdown 'select' menus.
    * A text area for adding some brief journey details.
    * A datepicker.
    * Submit button.
* All these fields can be edited; then, upon clicking submit, the user is redirected to the main 'Latest lifts' page where they can see their edits have taken effect and been published.
* Selecting 'Delete' from a lift post completely removes the listing.

NB: the datepicker currently returns lift posts with a date format of MM/DD/YY, whereas the automated date and timestamp returns DD/MM/YY. This is a known issue and will be addressed in the future.

### Features left to implement

* The site could have a mapping element, whereby documents in the MongoDB locations collection are given latitude and longitude values, allowing chosen locations for a lift to be pinned on a map using the Google Maps API.
* A 'browse lifts' page could contain all active lift postings, with search filters to narrow the results down by location or date of travel, for example.
* An authentication system for registered users should be set up, so that: 1) only the person who added a lift can edit or delete it, and: 2) for added security and peace of mind for users.
* This system could also be extended to send notifications to registered users when a reply is left on their post.

## Technologies

This project uses HTML, CSS, JavaScript, jQuery, Python/Flask and MongoDB.
It utilises the Bootstrap framework and library, plus a [datepicker from GIJGO](https://gijgo.com/datepicker) and Font Awesome for icons.

## Testing

## MongoDB schema

## Deployment

## Credits

### Content

* The datepicker was sourced from https://gijgo.com/datepicker/example/bootstrap-4.
* For scrolling to the top with a 'back to top' button, I referred to https://www.w3schools.com/howto/howto_js_scroll_to_top.asp.

### Acknowledgements

Code Institute tutor Tim Nelson was a very wise and patient man as he helped me learn and navigate the worlds of MongoDB, Python, Jinja and Flask. Thanks also to members of the 'Kenmare Community Chat' Facebook page for being the inspiration behind this project! 