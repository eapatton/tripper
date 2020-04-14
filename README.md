# Tripper

## Index:

- [Scope](#Scope)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Data Models](#data-models)
- [Milestones](#milestones)

## Scope
We are planning to create a website for users to plan a trip. We hope to implement the ability for users to create a trip, and then associate things they are planning to do with that trip. The website will all display cities, and each city will have various things that you can do associated with it.

##### Technologies in play
- Django
- Python
- Bootstrap
- JavaScript
- HTML 
- CSS 
- Heroku

## User Stories
- User Story 1: 
    - A user wants to create a new trip. The user clicks on the “create new trip” button on the dash. They are taken to a form which allows them to make a new trip. They enter the location, dates, and budget of their trip and then submit it. The page redirects the user to a page displaying their new trip. 
- User Story 2: 
    - A user wants to add things to do to their trip. They go to a list of all cities. They click on the city they want to go to. They are redirected to a detail page for that city. The detail page displays things that can be done in that city. They click on a thing that they want to do. It is added to their trip. 
- User Story 3: 
    - A user modifies their trip. They click on their profile. They see a list of their trips. They click on a trip and are redirected to the detail page for that trip. They click on an edit button. They modify the trip and then click submit. The new information is saved. They are redirected to the detail page for their trip, which now displays the updated information. 



## Wireframe


## Data Models
- User
    - Will make a trip with an associated city
    - They will add things to do in that city
- Trip
    - Destination
    - Date
    - Budget 
- Destinations
    - Name of city
    - Description
    - Associated things to do
- Things to Do
    - Description
    - Address
    - Cost
    - Hours of operation


## Milestones

#### Sprint 1 
##### April 9
- Get the wireframe, user stories, data models and use Jira for delegation to present the project to Michael and Brock for approval.
- Set up server and database, basic urls and templates. Set up the three models and their associated urls, html templates, make migrations
#### Sprint 2
##### April 10
- Add HTML templates, CSS, Navbar
- Add Destination index page with seeded data
- Start the trip page
#### Sprint 3
##### April 11-12
- Set up basic CRUD functionality for the Trip, be able to add, update and delete
#### Sprint 4
##### April 13-14
- Set up authentication and authorization
- Add more seed data and styling
- Deploy to Heroku

## References
- For color schemes
https://www.canva.com/learn/website-color-schemes/

- Bootstrap sidebar
https://bootstrapious.com/p/bootstrap-sidebar

- Website fonts
https://www.awwwards.com/20-best-web-fonts-from-google-web-fonts-and-font-face.html

- Free Beautiful Photos
https://unsplash.com/t/travel

- Django static
https://docs.djangoproject.com/en/3.0/howto/static-files/
