# British and International Search and Rescue Dogs (B.I.R.D)

Todo: 
- Wireframes
- Datascheme
- Readme
- Testing
- Validation
- Remove comments
- Check id, class
- Unused css
- Rename files
- Debug mode false
- Peer review

## Introduction

BIRD consists of highly trained volunteers that form a totally self supporting team used to assist in disasters at both home and abroad. They have deployed to many disasters worldwide and also assist the Police, HM Coastguard and Fire Service at home. They have no government funding and exist solely on donations and fund raising. The BIRD website is built on Django using Python, JavaScript, HTML and CSS. The site is used for selling products for fundraising purposes and to update public on their latest activities. Users of the site can search for products via manual keyword search, filter by category or browse through all products available. They can select differing quantities of products for purchase and add them to their shopping cart, and proceed through a purchase process designed to be simple and with minimal steps. The business owner and employees can add, edit and remove products from the site without accessing the admin interface. They can also add, edit and remove News posts to inform site users of new products or provide how to guides and other useful information. The business owner or employees can also respond to reviews that users have left on the site should they deem necessary, or they can delete the review if necessary.

This is the fifth project for the Code Institute Diploma in Software Development with eCommerce.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, Full CRUD functionality for approved users for Products, Categories, News Posts and Categories along with Reviews and Responses.

![Screenshot of homepage](/static/docs/img/responsive-site-image.png)

[View the live website on Heroku](https://druid-computers.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
- [Druid Computers](#druid-computers)
  * [Introduction](#introduction)
  * [Table of Contents](#table-of-contents)
  * [UX](#ux)
    + [Overall Goals](#overall-goals)
    + [The Sites Ideal User](#the-sites-ideal-user)
    + [Site Goals](#site-goals)
    + [User Stories](#user-stories)
    + [Design](#design)
      + [Wireframe mock-ups](#wireframe-mock-ups)
      + [Database Schema](#database-schema)
      + [Visual Design](#visual-design)
  * [Features](#features)
  * [Future Enhancements](#future-enhancements)
  * [Social Media](#social-media-marketing)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## UX

### Overall Goals
* To provide an ecommerce solution for a small business selling computer products to consumers - B2C
* To enable business employees to maintain and update the site content in line with their needs easily.
* To provide the business owner/manager a degree of control over the site.
* To provide users with a simple product selection and purchase experience.

### The Sites Ideal User
* Someone looking support the charity by purchasing products
* Someone looking to learn more about the charity

### Site Goals
* To provide users with a place to purchase their watercooling products
* To promote the product range of Druid Computers
* To promote Druid Computers as the preferred site for users to purchase their watercooling products
* To increase the standing of Druid Computers within the watercooling industry and community.

### User Stories
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
|     |            | **_Viewing and Navigation_**                                      |                                                                                       |
| 1   | Customer    | View list of products                                             | Find something to purchase                                                            |
| 2   | Customer    | View details of product                                           | See Price, Description, Image, and Sizes i/a                                          |                                                |
| 3   | Customer    | See my cart's total at any time                                   | Avoid spending too much                                                               |
|     |            | **_Registration and User Accounts_**                              |                                                                                       |
| 4   | Reg User   | Register for an account                                           | Save my delivery details and order history                                            |
| 5   | Reg User   | Quickly login/out                                                 | Access my account                                                                     |
| 6   | Reg User   | Request a password reset                                          | receive and email to reset my password in case I forget it                            |
| 7   | Reg User   | Receive an email confirming my registration                       | Verify my account was registered successfully                                         |
| 8   | Reg User   | Access my user profile                                            | View my order history, manage my personal details                                     |
|     |            | **_Sorting and Searching_**                                       |                                                                                       |
| 9  | Customer    | Sort the list of available products                               | See the products in a list sorted by price, rating, quantity available etc            |
| 10  | Customer    | Sort a category of products                                       | See the products in a category sorted by name, price, rating, etc                     |
| 11  | Customer    | Sort multiple categories simultaneously                           | Find the best rated or best priced across broad categories such as 'books' or 'honey' |
| 12  | Customer    | Search for product                                                | Find a specific item I wish to purchase                                               |
| 13  | Customer    | View a list of search results                                     | See if the product I want is available to purchase                                    |
|     |            | **_Purchasing and Checkout_**                                     |                                                                                       |
| 14  | Customer    | Easily select the size and quantity whilst purchasing an item     | Ensure I don't accidentally select the wrong product, quantity, or size               |
| 15  | Customer    | View items in my basket                                           | See what items are in my basket at a glance to ensure the items are correct           |
| 16  | Customer    | Adjust the quantity of individual items in my bag                 | Easily adjust the amount of an item I intended to purchase (including removing)       |
| 17  | Customer    | Easily enter my payment information                               | Checkout quickly, without hassle                                                      |
| 18  | Customer    | Feel my payment and personal information is secure                | Provide the needed payment and personal information, and feel it is handled safely    |
| 19  | Customer    | View confirmation of order before completing purchase             | Verify I haven't made any mistakes                                                    |
| 20  | Customer    | Receive confirmation email after checking out                     | To keep my own record of the purchase                                                 |
|     |            | **_Admin and Store Management_**                                  |                                                                                       |
| 21  | Site Owner | Add a product                                                     | Add new products to my store                                                          |
| 22  | Site Owner | Edit/update a product                                             | Change the price, description, images etc of a product                                |
| 23  | Site Owner | Delete a product                                                  | Remove items that aren't for sale anymore                                             |
| 24  | Site Owner | Add a team member                                                 | Add new products to my store                                                          |
| 25  | Site Owner | Edit/update a team member                                         | Change the price, description, images etc of a product                                |
| 26  | Site Owner | Delete a team member                                              | Remove items that aren't for sale anymore                                             |
|     |            | **_News Section_**                                                |                                                                                       |
| 27  | Customer    | View list of news articles                                        | Choose a news article to read                                                         |
| 28  | Customer    | View full news article                                            | Read detailed about latest news and activities                                        |

## Design
### Wireframe mock-ups
Wireframes were produced for the majority of pages, with the exception of pages that were likely to only include a form such as the add product page. A pdf document with the full set of wireframes produced is available [here](/static/docs/wireframes.pdf).

Attention was paid to the elements that would be present on each page such as the header and the footer.
The header allows for multiple levels of navigation providing the user with shortcuts to account information, whilst clearly being seperated from the main navigation options. On mobile or tablet devices, the two are seperated by a horizontal bar within the main menu, whilst on the desktop view the secondary account navigation links appear above the main site navigation.

Home page: The home page provides the user with a clear understanding as to the purpose of the site The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using. There is a clear navigation area located at the top of the screen, with a search icon clearly visible within the header. There are large call to action buttons linking users to search results for popular categories of products for easy access.
Home Page Mobile Wireframe
Home Page All Wireframes
All Products Page: For a page that shows all the products available it was deemed important to enable users to browse the range easily, therefore presenting the individual products in a summary fashion which enables the user to navigate to access more information if required or just add the products that they want to their cart
All Products Page
Individual Product Page: For each individual product three distinct sections were planned to enable product information to be presented clearly to users. An image carousel to allow multiple images to be displayed allows users to see the product from multiple angles. Whilst users can access the overall description and add to cart functionality quickly and easily at the top of the page.
Individual Product Page Wireframe
Shopping Cart: For the shopping cart functionality wireframes were produced for both the page and the preview/confirmation message when a user adds a product to the shopping cart. For the shopping cart it is important to allow users to adjust the items in the cart, increase or decrease individual items quantity or remove items completely.
Shopping Cart Wireframe
Checkout: For the checkout page the user will be required to enter, or confirm their billing/delivery address. The intention from the wireframe design is to include a summary of the users shopping cart along with the form for them to confirm their details. In the lower portion of the page users will be able to enter their payment information which will be based on a payment form provided by Stripe. As it is a page where the user can be charged for the goods, it is important for a good user experience that the total cost is clear to the user.
Checkout Page
Order Confirmation: Provided the users payment is processed successfully, they will be taken to the order confirmation screen which will provide the user with a summary of the entire order as it has been recorded along with their order number. The order number will need to be unique for each order. If the user is a registered user and logged in at the time of order, they should be able to access the order details again at a later date. Non registered users should be able to access their orders status by entering the order number somewhere else on the site.
Order Confirmation page
All News Posts Page: The News posts page is a key page within the site. From a user experience persepective, the News provides an opportunity for the company to directly communicate with its customers, or prospective customers. This communication can be in the form of guides, product reviews, or any other type of communication that they believe their customers might find useful. The content the company can produce for this section of the site is important for SEO purposes also and can assist in their overall marketing efforts. Ideally therefore, users should be able to access the News section of the site easily, and also be able to quickly assess which News posts they are interested in.
All News Posts Page
Individual News Post: For the individual News post page the full details of the post are available. The layout is a clean simple design with an image at the top followed by the main content of the post.
Individual News Post Page
User Account Page: The user account page is a central location from which users can manage their entire account. All potential options need to be easily accessible from this one page. A short menu of available options is located at the top of the page followed by the ability for users to add addresses, or change their default address to another saved address. Finally the option to delete their account is clearly available. By providing the option clearly and not hidden away it promotes trust with the user that they are in full control of their account.
User Account Page

### Database Schema
Several custom models were predicted to be required when building the site. To plan out the models they were sketched out in Figma. Figma was chosen due to the limitations of the free tiers for the online apps available which restrict the field choices available, therefore allowing the fields to be defined correctly whilst planning. The intention to utilise AllAuth for the user authentication system, which utilises the built in Django User Model removed the need to build a custom User model for user authentication, however some custom information is required, therefore a custom user model to override the allauth model is required. In order for users to be able to save multiple addresses to their account, an address model was created with the required fields. A boolean field that records whether it is the default address for the user was also added to aid the checkout process.

For the products a custom model based on the boutique ado walkthrough project was created. This model was adapted by adding the additional fields required for the additional product information expected for this site, whilst several fields were removed as unnecessary given the type of products offered. A seperate image model was created so that additional images for each product could be stored. This allows in theory an unlimited number of images to be stored for each product. Whilst the intention is that each product will have three images in total, one main image associated with the product itself, and two additional images stored in the image model, it would be possible to adjust the site to accomodate many more images per product. By seperating the additional images from the main product model it enables products to be added to the site with only one image. A third product related model to define the product category was created. Based on the model from boutique ado also, the category model contains two fields a name and a friendly name field. No other fields were deemed necessary for the model to customise it further.

The order process is controlled with the use of two models, an Order model and a OrderLineItem model. Both models were based on the models from boutique ado with the changes required for the purposes of this site. Given the information that is required to be sent to Stripe for processing the payments and would be required for business purposes the structure of the models makes sense to be utilised. The changes made include the addition of a status field to enable the recording of the order status and future updates to provide users with additional information.

Two models relating to users creating reviews of products were created, one to record the users review and another to record an employees response to that review.

The final model created records user messages to the company through the contact us page.

### Visual Design

### Colours

Once I was happy with the overall structure of the site, and the layout of the wireframes, I selected a colour scheme based on a desire for a simple and clean aesthetic. The site incorporates two main colours, blue and white, although specific shades were selected for various different areas, they all remained within the blue family. Blue was chosen due to the fictional business base location and the county colours are blue and white. The white or off white shades are tinted with a little blue to maintain consistency. The colour scheme was referenced using the [contrast grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23000000%2C%20Black%0D%0A%2303045E%2C%20Primary%0D%0A%23f2f4f8%2C%20Primary-text%0D%0A%23c7ccdb%2C%20Secondary%0D%0A%23f7c59f%2C%20Accent%0D%0A%2370ae6e%2C%20Success%0D%0A%23ef626c%2C%20Error%0D%0A%231188a0%2C%20Info%0D%0A%23f3c178%2C%20Warning&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18) which provides a grid of colour contrasts to ensure only those which would easily pass the AAA standard were selected to maximise accessibility for users.


![Colour Contrast Grid](/static/docs/img/contrast-grid.png)



### Typography 
Three different fonts were utilised for the site. The main heading font of Orbitron and the smaller subheading font of Economica were selected for their futuristic almost technical feeling whilst Montserrat was chosen as a complimentary font which allowed users the ability to read the text easily and clearly.

##### Images
Background images were acquired from free image sites [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/), product photos were found on manufacturer media pages.

## Features

### Navigation
The main navigation is split into two sections. The first section contains the main navigation for the sites main sections of interest. The second section contains the links for user account management or employee site management. JavaScript was utilised to move the second navigation section into place depending on the size of the screen. On the desktop view the secondary navigation bar appears on the top right of the screen, whilst in the mobile/tablet menu it appears below the main navigation options.


![Navigation desktop view](/static/docs/img/features/nav-desktop.png)



![Navigation mobile menu](/static/docs/img/features/mobile-menu.png)



### Footer
There are also navigation links within the footer from which users can access areas of the site, this includes areas that are not listed in the main navigation such as the privacy policy or social media links. Also included in the footer is a newsletter sign up to a mailchimp controlled email database. The mailchimp supplied sign up form was styled to match the remainder of the site.



![Footer Desktop View](/static/docs/img/features/footer-desktop.png)



### Homepage
The home page greets users with a welcome message overlaid on a close up image of cooling pipes inside a computer system. This provides a welcome to all users whilst indiciating the sites purpose. The clear links within the navigation bar indicate that the site is a shop whilst the call to action cards below the welcome/hero section direct users to specific product categories quickly and easily.



![Homepage View](/static/docs/img/features/home-desktop.png)



![Home page mobile view](/static/docs/img/features/home-mobile.png)



### All Products
The all products page displays summary cards for each product, with a maximum of five products per page pagination was utilised to create multiple pages making up the full list of products.



![All Products Page](/static/docs/img/features/all-products-desktop.png)



### Product Search
Users can search the site for different products through the search bar which is activated by clicking on the search icon located within the main header.



![Search Bar Activated](/static/docs/img/features/search-bar-desktop.png)



When a search is completed by the user, the results will display in summary card format. Pagination is utilised for scenarios where the search results are too large for display on one page. The search criteria is displayed at the top left of the screen for users as a indication that they have filtered the results.



![Search Results](/static/docs/img/features/search-results-desktop.png)



The individual summary card for each product links the user to the full product details. For ease of use, users have the ability to add the product to their shopping cart without accessing the full product details. A quantity selector is also included for those users who wish to purchase in multiples. The summary cards contain the basic information users may require for each product, the product name, the sale price, if it is available, a category indicator and the shopping controls.



![Product Card](/static/docs/img/features/product-card.png)



### Add to Bag
When a user adds a product to their shopping cart they receive a confirmation message that it has successfully been added. The icon for the shopping cart, also gains an indicator that shows the quantity of products they have within the cart as an additional level of confirmation.



![Add to cart confirmation](/static/docs/img/features/add-product-message-desktop.png)



### Shopping Cart
When the user is happy with their selections they can proceed to the shopping cart to confirm the quantity and selections. The user has the ability within this page to adjust the quantity of the products selected, or to remove products entirely before proceeding to the checkout process.



![Shopping Cart Page](/static/docs/img/features/shopping-bag-desktop.png)



### Checkout
When the user is ready to purchase the products that they have selected, they proceed to the checkout page, here they can enter their billing and delivery information. Registered users can save the information they have entered and create a new address record. If they already have address records saved, they have the option to select one of them to use for this purchase. If they have a default address set the form will be prefilled with the default address information. The final part of the form is the payment details, this is taken directly from Stripe - or inserted by Stripe for the purposes of capturing the payment card information. As the Stripe payment system is not fully activated only the test card information can currently be utilised.

The page also includes summary information about the items being purchased so that it is clear to users what they are purchasing. A message also appears next to the complete order button informing the user of the total amount they are agreeing to be charged.



![Checkout page Desktop](/static/docs/img/features/checkout-desktop.png)



### Order Confirmation
When users have successfully processed their payment, they are taken to the order confirmation page which provides the user with a summary of the information their order contains. This page also provides the user with their order number.



![Order Confirmation](/static/docs/img/features/order-confirmation-desktop.png)



At the same time as the user is redirected to the order confirmation page, an email is sent to the email address they provided during the checkout process. This email provides the user with the same details as the order confirmation page, with the full address details summarised as the town and country only.



![Order Confirmation Email](/static/docs/img/features/order-confirmation-email.png)



### Order Status
Registered users can access the status of all previous orders through the order status page. Here they are able to filter and search through their prior orders. Results are presented in the form of summary cards showing the order number, the items ordered, total order value, date of order and its current status.



![My Order History](/static/docs/img/features/order-history.png)



Employees are able to access an update order status page which allows them to update the status of an order. Several predefined options are available covering all common order status stages. When an employee updates an orders status it is then reflected back on the users record with the new status. To access the update order status screen employees have an order management option within their employee actions navigation menu. This page is similar to the My Order History page above, and provides the employee the ability to filter and search through the current orders on the system to find the correct order to update.



![Update Order Status](/static/docs/img/features/update-order-status.png)



### User Account Management
Registered users can access controls for their account through the My profile option in the account menu. In the profile page they have access to options to change their email address, name, password or delete their account entirely. They can also make adjustments to the addresses that are stored with their account, accessing add, edit, delete and make default functionality.



![User Profile Page](/static/docs/img/features/profile.png)



### User Wishlist
Registered users can also save products to their wishlist by clicking on the heart icon within the product details. Once they have added a product to their wishlist they are informed by the heart icon becoming filled in colour. They will also see the product listed on the My Wishlist page. Here users can add the products to their cart without having to search for them, select the quantity to be added. Remove the product from their wishlist, or follow the link to the full product details.



![My Wishlist Page](/static/docs/img/features/wishlist.png)



### News
Users have access to view News post articles written by the company. These articles will form part of the company SEO and web marketing strategies and allows them to include information on topics that will be interesting to their users. Clever use of the News post section of the site will allow the company to incorporate both short tail keywords and long tail keywords, providing answers to target users questions. This will improve their overall search engine ranking performance whilst providing users with beneficial information and improving their overall experience and trust within the company.
Users are able to select which News post to read through the summary list provided on the main News page.



![News Post Page](/static/docs/img/features/News-posts-desktop.png)



The News detail page provides the user with the full News post content



![News post detail page](/static/docs/img/features/News-detail-desktop.png)



Whilst employees will have access to additional options in order to access areas of the site that allow them to add, edit, delete News posts. They also have access to News post category management options that allow them to add, edit and delete categories for News posts.



![Employee view of News posts](/static/docs/img/features/News-category-management.png)



### Product Reviews
Users who have purchased a product from the site are provided access to add a review for that product and a rating. The option exists on the main product detail page for each product. Users are only able to add one review per product, and the employees have the ability to respond to the review directly.
Other users will be able to read other users reviews of a product to aid in their purchase decision making.



![Add a product review](/static/docs/img/features/add-review.png)



Once a user has added a review to a product, they will have the option to edit or delete their review. Employee's get the option to respond to the post or to delete the review. The screenshot below shows all options as the review was added by the logged in employee.



![View a product review](/static/docs/img/features/product-review.png)



### Contact Us
Users have the ability to send a message to the company directly through a contact form provided on the site. When a user sends a message through the website they will also receive a copy of the message to the email address that they provided. The message that the user sends is also delivered via email to the company designated account so that it can be followed up on and answered.



![Contact Page](/static/docs/img/features/contact-page-desktop.png)



## Future Enhancements

## Testing

### Testing Strategy
I utilised an automated and manual testing strategy for the development of the site. A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md).
Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the acceptance criteria of the user stories listed above were met. The commit at which the functionality requirements for each user story were met is listed in the issues section of the repo. It was applied to each issue before it was closed and marked as completed.

#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.

[Testing Schedule Overview](/static/docs/testing-schedule.pdf)

A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md)

#### Validator Testing
All code files were validated using suitable validators for the specific language. The full details can be found in the testing.md file.
All code passed the validation, with only code generated by other parties producing errors or warnings.
* Django built in code within the settings file produced five line length errors. 
* Bootstrap code produced 260 warnings in the CSS validation. 
* Fontawesome cdn produced 6 HTML validation errors relating to css variables within the cdn css code. 
* The HTMX library that is inserted into the HTML template by django produces a warning stating that the link does not need to have the javascript file type declared.

#### Automated Testing
Automated tests were written for the News and profile apps, along with the product forms. A total of 45 different tests were written to test the urls, views and forms and demonstrate my understanding of the testing procedures. In order to run the tests, you will need to clone the repo. In the settings for the project the database is set to point at the specified database when a database url is present within the config variables. Provided that you do not include a database url in the config variables django will run the tests on a test database utilising sqlite3. Django will not run the tests on the postgresql database from a heroku application, therefore you will need to ensure not to include the database url in the config variables.



![Automated testing results](/static/docs/img/features/tests.png)



#### Lighthouse Testing
Google's lighthouse testing was utilised to gain an overall assessment of the performance of the site. Whilst all the areas of the test return a green score above 90, the overall performance figure fluctuates depending on the speed of the internet connection when the test is performed, having returned scores as low as 92 and as high as 100 whilst running the test multiple times. The accessibility score suffered a couple of points due to utilising headings in a non sequential order through out the site. The best practice score is impacted by the mailchimp and stripe included javascript files along with the use of the bootstrap and jquery libraries. The SEO score returned a perfect 100.



![Google Lighthouse Results](/static/docs/img/features/lighthouse.png)



#### Notable Bugs

* Whilst validating the HTML it reported an error that I had included a placeholder for a checkbox field which is not allowed. To fix this error I removed the placeholder from the list within the forms.py file for the relevant address form. Thinking that will sort the error out and its only a placeholder so doesn't affect anything else. It did fix the HTML validation error straight away, however, it created a bug within another part of the code where the fields were checked whether they were required or not. If a field was required it adds '*' to signify it to users, if it is not, it inserts the placeholder. However, now I had removed the placeholder, anytime the form was requested it would return a 500 error. Whilst I appreciated the ability to test the custom 500 error page worked correctly on the production site it was a bug that took me a little while to track down the route cause and fix. The fix was simple enough and achieved by including the default field of the model within the if statement and excluding it from the placeholder assignment.

* Within the News post page employee view, there is a category management section that can be activated. This section allows an employee to edit, delete and create categories for News posts. Forms are inserted via htmx into the html on demand to allow the employee to carry out the task required. As the forms are inserted via htmx, it was possible to insert multiple forms at the same time into the page and edit multiple categories at once, and have the add category form open as well. If the user did this, a HTML validation error would occur as the form is duplicated it contains duplicate ID's. To overcome the HTML validation error possibility, JavaScript was utilised to prevent the user from opening multiple forms at the same time, this was achieved by disabling the other buttons when a user clicks on one of the edit buttons or add buttons, until either the user cancels their action or has completed their task.

* Order Status updates. Within the order management section of the site, employees have the ability to update the status of an order. To help with finding the correct order, multiple filters are available for them to search the orders within the database. One of these filters allows for searching the previous days orders. This works as designed during normal working hours, however when testing the functionality it was discovered that during the first hour of the day, so the time period between midnight and 1am the filter would bring back the previous day plus one's orders, not the previous days. This resolves itself as soon as the time clicks past 1am. As the only time that this will be triggered is in the middle of the night, it was deemed acceptable to leave as it currently is and not attempt to edit the library utilised to include the filters. Should the business operate 24 hours a day and require the functionality to pull the previous days orders during that one hour window it would obviously need to be resolved.

#### Technologies Used

* Python
    * The following python modules were used on this project:
        * asgiref==3.5.2
        * bleach==5.0.0
        * boto3==1.24.18
        * botocore==1.27.18
        * certifi==2022.5.18.1
        * cffi==1.15.0
        * charset-normalizer==2.0.12
        * crispy-bootstrap5==0.6
        * cryptography==37.0.2
        * defusedxml==0.7.1
        * dj-database-url==0.5.0
        * Django==3.2
        * django-allauth==0.50.0
        * django-countries==7.3.2
        * django-crispy-forms==1.14.0
        * django-filter==22.1
        * django-htmx==1.12.0
        * django-storages==1.12.3
        * django-summernote==0.8.20.0
        * gunicorn==20.1.0
        * idna==3.3
        * jmespath==1.0.1
        * oauthlib==3.2.0
        * Pillow==9.1.1
        * psycopg2==2.9.3
        * pycparser==2.21
        * PyJWT==2.4.0
        * python-dateutil==2.8.2
        * python3-openid==3.2.0
        * pytz==2022.1
        * requests==2.27.1
        * requests-oauthlib==1.3.1
        * s3transfer==0.6.0
        * six==1.16.0
        * sqlparse==0.4.2
        * stripe==3.2.0
        * typing_extensions==4.2.0
        * urllib3==1.26.9
        * webencodings==0.5.1

* Django
    * Django was used as the main python framework in the development of this project
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* HTMX
    * HTMX is a JavaScript library that enables forms to be submitted and data to be retrieved from the backend without refreshing the entire page. It was used extensively for pages that included form submission such as the creation of the recipes where creating ingredients in another model, and creating steps in a third model was required. This package provided a simpler approach to using multiple formsets and custom JavaScript.
* JavaScript
    * Custom JavaScript was utilised to enable the colour scheme functionality, the mobile menu, the enabling and disabling of buttons on forms to prevent users inadvertantly causing errors when trying to submit multiple forms at the same time, and to display the current image in the form rather than a hyperlink to the image itself.
* Bootstrap 5.2
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* VS Code was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project
* Balsamiq was utilised to develop wireframes for the site from which the design was based
* Adobe Illustrator was used to adapt images for use within the site.
* Figma was used to develop the database schema during development - I used this instead of a DB app due to the ease with which to document the actual field types rather than some of the online apps which don't include fields that are available.

#### Resources Used

* The Django documentation was used extensively during development of this project
* The HTMX documentation was used as a reference source for the development of the HTMX features
* The Django AllAuth documentation was used as a reference and a guide for implementing the package and its features.
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.

## Deployment
A repository was setup in GitHub using the Code Institute Gitpod [full template](https://github.com/Code-Institute-Org/gitpod-full-template).  Development was completed using Gitpod and code was regularly pushed back to the GitHub repository.  The master branch of this repository is the most current version and has been used for the deployed version of the site.

The current live website is hosted as a [Heroku](https://www.heroku.com) app, however the images and static files are hosted on an [AWS](https://aws.amazon.com) simple storage service (s3).  [Stripe](https://stripe.com) is utilised for the management of financial transactions and [Gmail](https://google.com) is used for emails.  The instructions in this section cover the process to set up and use these services. 

# Running the project locally
To work on the project code locally a clone can be taken by following the steps below or downloading the files as a zip file. To see the options, open the desired repository and select the drop down menu button ‘Code’ (found under the repo name and above the list of files).

## Clone:
To do this you will need Git for Windows installed (for other OS versions see [here]( https://git-scm.com/downloads)).

*   Open Git.
*   Change the current working directory is required. On windows, by default, the files will be downloaded to the users file directory on the C: drive.
*   In the ‘Code’ dropdown menu in GitHub, select either HTTPS or SSH and copy the link.
*   In the GitBash window type ‘git clone’ and then paste the copied link:
```
  git clone https://github.com/chelsea-designs/bird-search-and-rescue.git
```
*   Hit Enter and the files will then be cloned to be worked on locally.

Please see [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) for the GitHub Docs page on this process.

The cloned repository includes the ‘requirements.txt’ to enable the installation of the packages required for this project using the following command in the terminal:
```
  pip3 install -r requirements.txt
```
Once that is successfully complete, setup a super user to log into Django admin and have admin privileges throughout the site, by typing the below into the terminal and following the prompts:
```
  python 3 manage.py createsuperuser
```
## Environment Variables
The following environment variables (in CAPS) must be set within your development environment for the site to function correctly.  These are listed and described below and instructions to obtain these are featured in the following sections.

* DEVELOPMENT
  * Required so that within the development environment, debug = True.
  * *Value: set as **True*** 
* SECRET_KEY
  * Required by Django: A random sequence of characters used to maintain security.  
  * *Value: Django secret key.  A good resource is [miniwebtool – django secret key  generator](https://miniwebtool.com/django-secret-key-generator/) and should be different to the same variable in the Heroku app.*
* STRIPE_PUBLIC_KEY 
  * *Value: from stripe account (see below section [Stripe Setup](#Stripe-Setup))*
* STRIPE_SECRET_KEY
  * *Value: from stripe account (see below section [Stripe Setup](#Stripe-Setup))*
* STRIPE_WH_SECRET
  * *Value: from stripe webhook endpoint (see below section [Create webhook](#Create-new-webhook-end-point)).*  Note that this is different to the one set for Heroku (see below section ?).  

Database migrations will need to be made by following the below commands:
```
  python3 manage.py migrate --plan*
  python3 manage.py migrate
```
The 'makemigrations' command will not need to be run here before the 'migrate' command as all the migration files are within the repository.  Should further changes to the models be made however the below commands will need to be run prior to running migrate:
```
  python3 manage.py makemigrations --dry-run*
  python3 manage.py makemigrations
```
*These commands do not have to be run, but it is best practice, so that the plan migrations can be viewed before completing them.



The project should then be push to your repository using the below commands:
```
  git add <name of file> or <.>
  git commit -m *<commit message>*
  git push
```

The application can now be run locally by typing in a terminal window:
```
  python3 manage.py runserver
```
Data can then be added to the site when signed in with the superuser credentials.

# Heroku Deployment

## Heroku Variables
The following environment variables (in CAPS) must be set within the ‘Config Vars’ section in Heroku for the deployed site to function correctly.   The config variables are added within the Heroku app by selecting the Settings tab, and under the heading 'Config Vars' clicking the button 'Reveal Config Vars' to show the key / value input boxes for the variables.  Instructions to obtain the variables are featured within below sections.

* SECRET_KEY
  * Required by Django: A random sequence of characters used to maintain security.  
  * *Value: Can use Django secret key generator (https://miniwebtool.com/django-secret-key-generator/) and should be different to the same variable in the development environment.*
* STRIPE_PUBLIC_KEY 
  * *Value: from stripe account (see below section [Stripe Setup](#Stripe-Setup))*
* STRIPE_SECRET_KEY
  * *Value: from stripe account (see below section [Stripe Setup](#Stripe-Setup))*
* STRIPE_WH_SECRET
  * *Value: from stripe webhook endpoint. Note that this is different to the one set for the development environment (see below section [Create webhook](#Create-new-webhook-end-point)).*  
* DATABASE_URL
  * *Value: automatically setup during Heroku deployment (can be obtained by viewing your Postgres database within the Heroku dashboard, under Settings Database Credentials).*
* USE_AWS
  * Required so that the deployed app uses AWS for images and static files.
  * *Value: set as **True***
* AWS_ACCESS_KEY_ID
  * Required for connection to the AWS s3 bucket
  * *Value: obtained within the downloaded .csv file generated during user creation in AWS (see below section [Create s3 bucket](#Create-s3-bucket)).*
* AWS_SECRET_ACCESS_KEY
  * Required for connection to the AWS s3 bucket
  * *Value: obtained within the downloaded .csv file generated during user creation in AWS (see below section [Create s3 bucket](#Create-s3-bucket)).*
* EMAIL_HOST_PASS
  * Required by Django to send emails using chosen email account
  * *Value: 16 character password provided by, in this instance; Gmail (see below section [Email Setup](#Email-Setup)).*
* EMAIL_HOST_USER
  * Required by Django to send emails using chosen email account
  * *Value: the email address of chosen email account (e.g. `bob.smith@gmail.com`)*

## Deployment
In order to run properly, Heroku requires:
*	requirements.txt
*	Procfile

Both of these files should be within the cloned repository, so ensure these are pushed to your GitHub repository. 

To deploy the app to Heroku from the GitHub repository you will need to follow the below steps:
*	Go to [Heroku]( https://www.heroku.com/).
*	Log in and click on 'New' > 'create new app'.
*	Enter an App name (do not use spaces and use lower case letters).
*	Choose a region, then click ‘create app’.
* Within the new app select the ‘resources’ tab and under addons type in ‘postgres’ to provision a new Heroku Postgres database (this will also add the required DATABASE_URL variable and value in the Heroku Config variables)

### Setup to auto-deploy when pushed to GitHub:
* Within the Heroku web dashboard, Click on the Deploy tab:  
![Heroku option deploy](assets/readme/heroku_options_deploy.png)
* Select deployment method as ‘GitHub’, and then search for your repository below that.
* Once your repository name is returned, click 'connect'.
* Then click ‘enable automatic deploys’

Within the development environment, in a terminal window, login into Heroku by entering the below command and following the prompts.
```
  heroku login -i
```

Then type the below to setup a superuser: 
```
  heroku run python manage.py createsuperuser
```
Database migrations will need to be made to the Heroku postgres by following the below commands (you will need to be logged into Heroku to perform these):
```
  heroku run python manage.py migrate --plan*
  heroku run python manage.py migrate
```
*This command does not have to be run, but it is best practice, so that the planned migrations can be viewed before completing them.

Once all the configuration variables have been added, the deployed app can then be run from Heroku by selecting it and clicking 'open app'. 

# Amazon Web Services (AWS) Setup
## Create s3 bucket
* Go to [Amazon Web Services](https://aws.amazon.com/) and set up an account if you do not have one.
* Once logged in, under ‘my account’ select ‘AWS Management Console’ and search for the service ‘s3’
* Once in the s3 interface create a new bucket for this project:  
![AWS create bucket button](assets/readme/aws_create_bucket_btn.png)
* Name the bucket and select a region closest to you.
* Uncheck block all public access and acknowledge that the bucket will be public:  
![AWS bucket - block public access settings](assets/readme/aws_create_bucket_public_access.png)
* Select ‘create bucket’ to finish and the bucket will be created.
* Under the bucket properties tab, select to ‘edit’ Static website hosting and select ‘enable’.
* Ensure that ‘host a static website’ is selected and enter a default value for index as this will not be used for this project deployment:  
![AWS bucket - static web hosting](assets/readme/aws_create_bucket_sw_hosting.png)
* Click save.
* Next click permissions tab and select to edit the CORS 
* Enter and save the below cors configuration which will set up the required access between the Heroku app and this s3 bucket.
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
* Next select to edit the bucket policy and select ‘policy generator’ to generate a policy.  Before you do that, copy the ‘Bucket ARN’ as shown below (you will also need this for setting up a group within Identity and Access Management below).  
![AWS bucket - edit policy](assets/readme/aws_create_bucket_edit_policy.png)
* Within the policy generator select policy type of ‘S3 Bucket Policy’
* Within Add Statements, select ‘allow’ for effect and type a star within ‘Principal’:  
![AWS bucket - add statements](assets/readme/aws_create_bucket_add_statements.png)
* For Actions select only ‘GetObject’:  
![AWS bucket - action select](assets/readme/aws_create_bucket_getobject.png)
* Then below that paste in the ‘bucket ARN into the Amazon Resource Name input box.
* Click ‘Add Statement’, then ‘Generate Policy’
* Copy the policy into the bucket policy editor and then so as to allow access to all resources in this bucket, add a slash star onto the end of the resource key:
* Click Save.
* Next select to edit the Access control list and set the list objects permission for everyone under the Public Access section as below:  
![AWS bucket - acl](assets/readme/aws_create_bucket_acl.png)
 
## Create access policy, group and user
### Create Group and Policy
* Within the AWS services menu open Iam (Identity and Access Management) and in the left hand menu click ‘User groups’ to create a new group.
* Name a new group and click ‘create group’.
* Click ‘policies’ so as to create a policy used to access the new bucket.
* Click ‘create policy’ and then select the ‘JSON’ tab and select ‘import managed policy’.
* Within the search input, search for s3 and then select to import the Amazon s3 full access policy:  
![AWS bucket - group policy](assets/readme/aws_group_policy.png)
* Modify the policy by entering the ARN from the bucket policy in s3 as the value for resource as below:  
![AWS bucket - policy modification](assets/readme/aws_modify_policy.png)
* Click ‘Next: Tags’ and then click ‘Next: Review’
* Provide a name and description for the policy and click ‘Create policy’.

### Attach policy to group.
* Within the AWS services menu open Iam and in the left hand menu click ‘User groups’ to view the newly created group.
* Select the new group and click on the permissions tab
* Click the ‘Add permissions’ button and select ‘Attach Policies’ from the drop down.
* Select the policy that was just created, by checking the tick box and click on ‘Add permissions’

### Create User and add to group.
* Within the AWS services menu open Iam and in the left hand menu click ‘Users’ and then select ‘Add users’
* Provide a name for the user, check the tick box to grant the user access and select next.
* Check the tick box next to the group just created to add the user to the group.  Click through the next few pages to create user.
* **!IMPORTANT:** On the success page, click 'Download .csv file' which contains the user access key and secret access key needed to authenticate them from the Django app.

## Connect Django to AWS s3 bucket.
Within the Django app settings python file enter the name and region name for the AWS s3 bucket that you have set up as indicated below:  
![AWS bucket - aws Django settings](assets/readme/django_settings_aws.png)

Within Heroku add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to the config variables and also add a USE_AWS key and set it to true.  The access key and secret key are contained with the **downloaded csv file**.

Once that is done, git add, commit and push the changes which will trigger a deployment to Heroku.  Check the Heroku build log to check that the static files were collected and there should be a 'static' folder within the s3 bucket. 

## Add media files to s3 bucket
The below instructions detail how to do this within the s3 management interface.

* Within the s3 bucket overview click create folder and call it media.
* Inside that folder click on ‘upload’ and then ‘add files’
* Select all of the product images (found within the repo download performed earlier) and click open
* Click next and then under permissions, check the box for ‘grant public-read access’:  
![AWS bucket - add media](assets/readme/aws_bucket_add_media.png)
* Then click upload.
* There should now be a 'media' folder within the s3 bucket containing the images. 

# Stripe Setup
* Create a [Stripe](https://stripe.com) account or log in to existing.
* On the Stripe dashboard, under ‘Developers’ copy the ‘test API key’ and ‘ Secret key’.  Use these as the values for the environment and Heroku variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY as detailed above. 

## Create new webhook end point.
**NOTE:** Two separate webhooks will need to be setup. One for the development environment and one for the Heroku app.
* Run the application to get the address of the site.  Copy this and go to the Stripe dashboard.
* Click ‘Developers’, select ‘webhooks’ and then click ‘Add endpoint’.
* Paste in the site URL and add to the end ‘/checkout/wh/’:  
![Stripe webhook url entry](assets/readme/stripe_wh_url.png)
* Click ‘Select Events’ and select the events to listen to as:
```
  ‘payment_intent_suceeded’ 
  ‘payment_intent_failed’
```
* In the newly created webhook endpoint details the ‘signing secret’ is now available.  Copy this and add it to the value for the environment and Heroku variable STRIPE_WH_SECRET as detailed above.
* Within the Stripe dashboard for that webhook, click ‘send test webhook’ and verify that it is working.

The STRIPE_CURRENCY variable is defined within the Django app 'settings' python file and is set to ‘gbp’.  If a different currency is needed then this will need to be changed.  See this link for [supported currencies](https://stripe.com/docs/currencies#presentment-currencies)

# Email Setup
The below instructions cover the setup using a [Gmail](https://google.com) account.

* Log in to your email account or set one up.
* Click account settings, and select the 'Accounts and Import' option from the top selection
* Under ‘Change account settings’ click ‘Other Google Account settings’
* Click on the ‘security’ option on the left and then under ‘Signing in to Google’ click on ‘2-Step Verification’
* Click ‘get started’, enter password and then work through the verification.
* Once verification is done and 2-Step verification is turned on, a new option now shows under the previous ‘Signing in to Google’ menu screen.
* In this, on the App passwords screen, select from the dropdowns; ‘mail’ for app and ‘other’ for device.  Add an appropriate name and click ‘generate’.
You will then be given a 16 character password which you will need to copy.

## In Heroku.
Within the Heroku Config variables add the 16 character password as the value to the variable ‘EMAIL_HOST_PASS’.  Add another variable called ‘EMAIL_HOST_USER’ and set the value as the gmail account email used.

------


## Credits

Photo by <a href="https://unsplash.com/@rovaniemi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Mauri Karlin</a> on <a href="https://unsplash.com/s/photos/mountain-dog?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

## Ackknowledgements

