# Saffron

### Summary
Welcome to Saffron! This is a social media we application built using the Django framework, Python, Javascript, and HTML/CSS. The goal is to create a place for foodies and cooking enthusiants to find each other online and share recipes or casual food-related posts, and create groups based on specific interests.

<p style="margin-bottom:30px"><img src='social_project/assets/images/HomePage-min.png' width=700px>


### Introduction
The world of social media is exploding, with demand growing faster than any single application can keep up. After the initial boom of the mid and late 2000s that brought about socially focused/topic independent platforms like Facebook and Twitter, social media's ubiquity began to create demand for more specific and specialized platforms related to certain interests, like video games, art, or even professional interest. This brought about a new, albeit slower wave of platforms, like Twitch, Instagram, Snapchat, and more.

One relatively untapped demographic in this space: foodies. Cooking and appreciation for good food are hardly new concepts, but there are still many new ways to explore it and take advantage in a digital age. There are many emerging platforms streamlining and digitizing food service and delivery, i.e. Doordash, Postmates and the like to Freshly and HelloFresh. But what if we could create a _social media_ platform specifically for food? This was precisely the question that motivated the development of this web application.


Thank you to Jose Portilla's Web Development Course for the primary scaffolding for this application.


### Requirements
**Python Libraries**
```
bcrypt==3.2.0
django==3.2.3
django-bootstrap4==3.0.1
misaka==2.1.1
numpy==1.20.3
pillow==8.2.0
requests==2.25.1

```

**Other**
```
- Bootstrap 4.6.0
- Optional: Jquery 3.5.1
```

### What is Saffron?
In its current stage, the application is a working proof of concept, which will continue to receive updates as soon as I am able to build additional features! Still, the platform provides core functions that users should expect from a social media platform.

<p style="text-align:center; margin:30px"><img src='social_project/assets/images/signup-min.png' width=700px>

Users can create an account with a username and link it to an email address. Through Django's user authentication packages, the signup page will verify that the user has inputted a valid email address, and will ask the user to input their desired password twice, checking to make sure they both match. Once the user has completed these steps and created an account, their information is stored as a new, unique user on a backend SQLite Database that was generated by Django upon creation of this project.

Also available to users and stored on the database are Groups, which allow users to come together based on specific interests in food; for example groups could be "Indian Food", "Afghani Recipes," or a group for one person to share their own personal recipes. Once a user joins a group, they can create a post, which will become visible on the Group page to anyone else who is a member.

<p style="text-align:center; margin:30px"><img src='social_project/assets/images/Groups-min.png' width=700px>

Finally, there is the Recipe of the Day. This is a unique page on the website that is not directly connected to the posting and group features. Each day, this page makes a request to an API called Spoonacular, which contains a database of thousands of dishes, and recipes for them. The request pulls a random dish's title, description, recipe, and image, formats it correctly through HTML/CSS, and deposits it on the Recipe of the Day page. This provides a fun and dynamic landing page for users to check out once a day and potentially get a new idea from!

New features and additional functionality are still going to be added. I'd like to add ways for users to interact, through commenting and liking each others' posts, and a number of other features users might expect from a social media application. Stay tuned!


### Application Backend
This application was built primarily using the Django web framework. Django is an open-source framework that enables the use of Python to streamline the web development process and interact quickly  with HTML/CSS as well as Javascript. This framework allowed me to create a custom template for the site, which included Bootstrap formatting, a specific color style, and a navigation bar. Then, using Django's signature "template tagging," I was able to build out several custom pages for the website that inherited from this template.

Django generates a SQLite database upon app creation, and using Python Objects, I constructed "models" which corresponded to the various types of information that the app would need to store. Each user would have their own instance of the User model, which would contain their username, email, and a password that is automatically encrypted using a PBKDF2 algorithm with a SHA256 hash. As each user created posts and joined groups, this information would be added to their object model and stored in the database. Similarly, each Group created by a user has an object model associated with it on the backend. This contains information on the group's title, description, and the number of current members.

Each page's functionality was created using a combination of Django's "views" functionality and HTML/CSS. You can see all of the code for the web application in the "social_project" folder; but for more information on Django's views and how they interact with HTML/CSS to quickly create clean website functionality, I highly recommend checking out their well-written documentation right here: [Django Docs](https://docs.djangoproject.com/en/3.2/)


### Sources/References
- I took Jose Portilla's Django Web Development Course in order to become familiar with the framework and build the high-level structure for the website; check that out here: [Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/learn/)
- The Spoonacular API was used to create the Recipe of the Day page, it's a great API I also recommend checking out: [Spoonacular API](https://spoonacular.com/food-api)
- Django documentation is very well written and it was also used for reference at every step of this project: [Django Docs](https://docs.djangoproject.com/en/3.2/)
- Bootstrap 4.6.0 was used for style formatting: [Bootstrap 4.6.0](https://getbootstrap.com/docs/4.6/getting-started/introduction/)



Thanks!