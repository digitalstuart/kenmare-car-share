# Kenmare Car Share

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

![alt text](https://i.imgur.com/iLy9U3h.jpg "Kingdom Come screenshot")
* I need to get to Cork Airport, I wonder if there's anyone who is already driving to Cork on the same day as my flight?

![alt text](https://i.imgur.com/D56Tugb.jpg "Kingdom Come screenshot")
* I drive around the area quite a lot, maybe there are people asking for lifts to the same places as me on the same days?

![alt text](https://i.imgur.com/GGjyC6j.jpg "Kingdom Come screenshot")

I used Balsamiq to create some wireframes for the project. 

![alt text](https://i.imgur.com/6Ro7Wcy.jpg "Kingdom Come wireframe")
![alt text](https://i.imgur.com/SEltWEW.jpg "Kingdom Come wireframe")

## Features

### Existing features

### Features left to implement

## Technologies

This project uses HTML, CSS, JavaScript, jQuery, Python/Flask and MongoDB.
It utilises the Bootstrap framework and library, plus a [datepicker from GIJGO](https://gijgo.com/datepicker) and Font Awesome for icons.

## Testing

## Deployment

## Credits

### Content

* The datepicker was sourced from https://gijgo.com/datepicker/example/bootstrap-4.
* For scrolling to the top with a 'back to top' button, I referred to https://www.w3schools.com/howto/howto_js_scroll_to_top.asp.

### Acknowledgements

Code Institute tutor Tim Nelson was a very wise and patient man as he helped me learn and navigate the worlds of MongoDB, Python, Jinja and Flask. Thanks also to members of the 'Kenmare Community Chat' Facebook page for being the inspiration behind this project! 