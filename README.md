# British and International Search and Rescue Dogs (B.I.R.D)

## Introduction

BIRD consists of highly trained volunteers that form a totally self supporting team used to assist in disasters at both home and abroad. They have deployed to many disasters worldwide and also assist the Police, HM Coastguard and Fire Service at home. They have no government funding and exist solely on donations and fund raising. The BIRD website is built on Django using Python, JavaScript, HTML and CSS. The site is used for selling products for fundraising purposes and to update public on their latest activities. Users of the site can search for products via manual keyword search, filter by category or browse through all products available. They can select differing quantities of products for purchase and add them to their shopping bag, and proceed through a purchase process designed to be simple and with minimal steps. The business owner and employees can add, edit and remove products from the site without accessing the admin interface. They can also add, edit and remove news posts to inform site users of new activities and missions or other useful information. They can also add, edit and remove team member biographies.

This is the fourth project for the Code Institute Diploma in Software Development.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, Full CRUD functionality for approved users for Products, Categories, News Posts and Categories along with Team Member Profiles.

![Screenshot of homepage](/static/docs/img/responsive-site.png)

[View the live website on Heroku](https://bird-sandr.herokuapp.com/)

Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

## Table of Contents
- [British and International Search and Rescue Dogs (B.I.R.D)](#british-and-international-search-and-rescue-dogs-(B.I.R.D))
  * [Introduction](#introduction)
  * [Table of Contents](#table-of-contents)
  * [UX](#ux)
    + [Overall Goals](#overall-goals)
    + [The Sites Ideal User](#the-sites-ideal-user)
    + [User Stories](#user-stories)
    + [Design](#design)
      + [Wireframe mock-ups](#wireframe-mock-ups)
      + [Database Schema](#database-schema)
      + [Visual Design](#visual-design)
  * [Features](#features)
  * [Future Enhancements](#future-enhancements)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

## UX

### Overall Goals
* To provide an ecommerce solution for a small charity selling fundraising products to consumers - B2C
* To enable business employees to maintain and update the site content in line with their needs easily.
* To provide the business owner/manager a degree of control over the site.
* To provide users with a simple product selection and purchase experience.
* To provide users with a place to learn about B.I.R.D.
* To increase the standing of B.I.R.D within the charity sector and community.

### The Sites Ideal User
* Someone looking support the charity by purchasing products
* Someone looking to learn more about the charity


### User Stories
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
|     |            | **_Viewing and Navigation_**                                      |                                                                                       |
| 1   | Customer   | View list of products                                             | Find something to purchase                                                            |
| 2   | Customer   | View details of product                                           | See Price, Description, Image, and Sizes i/a                                          |                                                |
| 3   | Customer   | See my bag's total at any time                                   | Avoid spending too much                                                               |
|     |            | **_Registration and User Accounts_**                              |                                                                                       |
| 4   | Reg User   | Register for an account                                           | Save my delivery details and order history                                            |
| 5   | Reg User   | Quickly login/out                                                 | Access my account                                                                     |
| 6   | Reg User   | Request a password reset                                          | receive and email to reset my password in case I forget it                            |
| 7   | Reg User   | Receive an email verifying my registration                       | Verify my account was registered successfully                                         |
| 8   | Reg User   | Access my user profile                                            | View my order history, manage my personal details                                     |
|     |            | **_Sorting and Searching_**                                       |                                                                                       |
| 9   | Customer   | Sort the list of all available products                               | See the products in a list sorted by price, rating, quantity available etc            |
| 10  | Customer   | Sort a category of products                                       | See the products in a category sorted by name, price, rating, etc                     |
| 11  | Customer   | Filter products by category                           | See the products in a specified category |
| 12  | Customer   | Search for product                                                | Find a specific item I wish to purchase                                               |
| 13  | Customer   | View a list of search results                                     | See if the product I want is available to purchase                                    |
|     |            | **_Purchasing and Checkout_**                                     |                                                                                       |
| 14  | Customer   | Easily select the size and quantity whilst purchasing an item     | Ensure I don't accidentally select the wrong product, quantity, or size               |
| 15  | Customer   | View items in my basket                                           | See what items are in my basket at a glance to ensure the items are correct           |
| 16  | Customer   | Adjust the quantity of individual items in my bag                 | Easily adjust the amount of an item I intended to purchase (including removing)       |
| 17  | Customer   | Easily enter my payment information                               | Checkout quickly, without hassle                                                      |
| 18  | Customer   | Feel my payment and personal information is secure                | Provide the needed payment and personal information, and feel it is handled safely    |
| 19  | Customer   | View  order summary before completing purchase             | Verify I haven't made any mistakes                                                    |
| 20  | Customer   | Receive confirmation email after checking out                     | To keep my own record of the purchase                                                 |
|     |            | **_Admin and Store Management_**                                  |                                                                                       |
| 21  | Staff      | Add a product                                                     | Add new products to my store                                                          |
| 22  | Staff      | Edit/update a product                                             | Change the price, description, images etc of a product                                |
| 23  | Staff      | Delete a product                                                  | Remove items that aren't for sale anymore                                             |
| 24  | Staff      | Add a team member                                                 | Add new products to my store                                                          |
| 25  | Staff      | Edit/update a team member                                         | Change the price, description, images etc of a product                                |
| 26  | Staff      | Delete a team member                                              | Remove items that aren't for sale anymore                                             |
| 27  | Staff      | Add a news post                                                 | Add new news posts to news section                                                         | Pass |
| 28  | Staff      | Edit/update a news post                                         | Change the title, description, images etc of a post                                | Pass |
| 29  | Staff      | Delete a news post                                             | Remove posts that aren't needed anymore                                             | Pass |
|     |            | **_News Section_**                                                |                                                                                       |
| 27  | Customer   | View list of news articles                                        | Choose a news article to read                                                         |
| 28  | Customer   | View full news article                                            | Read detailed about latest news and activities
|     |            | **_About Section_**                                               |                                                                                       |
| 29  | Customer   | View list of team members                                         | Learn about the team                                                         |

## Design
### Wireframe mock-ups
Low fidelity wireframes were created with Figma for the basic prototyping structure of the main site pages, with the exception of pages that were likely to only include a form such as the add product page. A pdf document with the full set of wireframes produced is available [here](/static/docs/wireframes.pdf).

Attention was paid to the elements that would be present on each page such as the header and the footer.
The header allows for multiple levels of navigation providing the user with shortcuts to account information, whilst clearly being seperated from the main navigation options. On mobile or tablet devices, the two are seperated, with main site navigation in a mobile menu toggle, and call to action buttons viewable at all times.

Home page: The home page provides the user with a clear understanding as to the purpose of the site The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using. There is a clear navigation area located at the top of the screen, with a search icon clearly visible within the header. There are large call to action buttons linking users to search results for popular categories of products for easy access.

All Products Page: For a page that shows all the products available it was deemed important to enable users to browse the range easily, therefore presenting the individual products in a summary fashion which enables the user to navigate to access more information if required.

Individual Product Page: For each individual product three distinct sections were planned to enable product information to be presented clearly to users. An product image, product details and call to action buttons.

Shopping Bag: For the shopping bag it is important to allow users to adjust the items in the bag, increase or decrease individual items quantity or remove items completely.

Checkout: For the checkout page the user will be required to enter, or confirm their billing/delivery address. The intention from the wireframe design is to include a summary of the users shopping bag along with the form for them to confirm their details. In the lower portion of the page users will be able to enter their payment information which will be based on a payment form provided by Stripe. As it is a page where the user can be charged for the goods, it is important for a good user experience that the total cost is clear to the user.

All News Posts Page: The News posts page is a key page within the site. From a user experience persepective, the news provides an opportunity for the charity to directly communicate with its customers, or prospective customers. The content the company can produce for this section of the site is important for SEO purposes also and can assist in their overall marketing efforts. Ideally therefore, users should be able to access the news section of the site easily, and also be able to quickly assess which news posts they are interested in.

About: The about page provides an opportunity for the charity to explain it's purpose and give details of staff involved. 

User Account Page: The user account page is a central location from which users can manage their profile details and also view their order history.

### Database Schema
![Schema](static/docs/img/data-schema.svg)
Several custom models were predicted to be required when building the site. The intention to utilise AllAuth for the user authentication system, which utilises the built in Django User Model removed the need to build a custom User model for user authentication, however some custom information is required, therefore a custom user model to override the allauth model is required.

For the products a custom model based on the boutique ado walkthrough project was created. This model was adapted by adding the additional fields required for the additional product information expected for this site, whilst several fields were removed as unnecessary given the type of products offered. A second product related model to define the product category was created. Based on the model from boutique ado also, the category model contains two fields a name and a friendly name field. No other fields were deemed necessary for the model to customise it further.

The order process is controlled with the use of two models, an Order model and a OrderLineItem model. Both models were based on the models from boutique ado with no changes required for the purposes of this site. Given the information that is required to be sent to Stripe for processing the payments and would be required for business purposes the structure of the models makes sense to be utilised. 

One model was created relating to staff adding news posts to the website.

The final model created records information about team members for the charity to display in the about page.

### Visual Design

### Colours

Once I was happy with the overall structure of the site, and the layout of the wireframes, I selected a colour scheme based on a desire for a simple and clean aesthetic. The site incorporates two main colours, black and white and their shades. A black and white color scheme is a popular choice in web design. It can make typography, images, and other visual elements stand out. I felt this colour scheme allowed the hero image to stand out.

### Typography 
The project uses Google Fonts for the delivery of the main font styling. The main font used was Poppins which is clear and crisp which allowed users the ability to read the text easily and clearly.

### Logo
I created a new logo for the charity as their old one needed modernising. The new one incorporates an optical illusion for a dog and a bird.
![Old Logo](static/docs/img/logo/old-logo.jpg)
![New Logo](static/docs/img/logo/new-logo.jpg)

### Icons
All icons were provided by the Font Awesome library.

##### Images
Background images were acquired from free image site [Unsplash](https://unsplash.com/), product photos were created on the [manufacturer webpage](https://www.clothes2order.com/).

## Features

### Navigation
The main navigation is split into two sections. The first section contains the main navigation for the sites main sections of interest. The second section contains the links forsearch, user account management and the shopping bag. On the desktop view the secondary navigation bar appears on the top right of the screen with primary centered underneath, whilst in the mobile/tablet menu the primary menu appears in a mobile dropdown toggle menu.

![Navigation desktop view](/static/docs/img/features/desktop-nav.png)

![Navigation mobile menu](/static/docs/img/features/mobile-nav-1.png)

![Navigation mobile menu](/static/docs/img/features/mobile-nav-2.png)


### Footer
Included in the footer is a copyright statement and a hyperlink for email address. This was done to allow an email/contact to be easily navigated to at any time.

![Footer Desktop View](/static/docs/img/features/desktop-footer.png)

![Footer Mobile View](/static/docs/img/features/mobile-footer.png)


### Homepage
The home page greets users with a welcome message overlaid on an image of a dog in nature. This provides a welcome to all users whilst indiciating the sites purpose. The clear links within the navigation bar indicate that the site is a shop whilst the call to action button below the welcome/hero section direct users to donate, which emphasises the shop is for charitable purposes.

![Homepage View](/static/docs/img/features/home-desktop.png)

![Home page mobile view](/static/docs/img/features/home-mobile.png)


### All Products
The all products page displays summary cards for each product, with a maximum of four products per row on desktop, two on tablet and one on mobile. The all products page includes a sort by filter and a back to top button.

![All Products Page](/static/docs/img/features/all-products-desktop.png)

![All Products Page](/static/docs/img/features/all-products-tablet.png)

![All Products Page](/static/docs/img/features/all-products-mobile.png)


### Product Search
Users can search the site for different products through the search bar which is activated by typing in the search bar on desktop or clicking on the search icon located within the main header on mobile.

![Search Bar Activated](/static/docs/img/features/search-bar-desktop.png)

![Search Bar Activated](/static/docs/img/features/search-bar-mobile.png)

When a search is completed by the user, the results will display in summary card format. Pagination is utilised for scenarios where the search results are too large for display on one page. The search criteria is displayed at the top left of the screen for users as a indication that they have filtered the results.

![Search Results](/static/docs/img/features/search-results.png)

The individual summary card for each product links the user to the full product details. The summary cards contain the basic information users may require for each product, the product name, the sale price, if it is available, a category indicator and the shopping controls.

### Product Details page
The product details page includes the product image, title, description, quantity input, rating, size options (where relevant) and add to bag buttons.

![Product Details](/static/docs/img/features/product-details-desktop.png)

![Product Details](/static/docs/img/features/product-details-mobile.png)


### Add to Bag
When a user adds a product to their shopping bag they receive a confirmation message that it has successfully been added. The grand total beneath the shopping bag item is incremented to reflect the new total.

![Add to bag confirmation](/static/docs/img/features/add-to-bag.png)

![Add to bag confirmation](/static/docs/img/features/bag-icon.png)


### Shopping bag
When the user is happy with their selections they can proceed to the shopping bag to confirm the quantity and selections. The user has the ability within this page to adjust the quantity of the products selected, or to remove products entirely before proceeding to the checkout process.

![Shopping bag Page](/static/docs/img/features/shopping-bag-desktop.png)


### Checkout
When the user is ready to purchase the products that they have selected, they proceed to the checkout page, here they can enter their billing and delivery information. Registered users can save the information they have entered. If logged in and they already have address records saved, this will be pre-populated for them to use for this purchase. The final part of the form is the payment details, this is taken directly from Stripe - or inserted by Stripe for the purposes of capturing the payment card information. As the Stripe payment system is not fully activated only the test card information can currently be utilised.

The page also includes summary information about the items being purchased so that it is clear to users what they are purchasing. A message also appears next to the complete order button informing the user of the total amount they are agreeing to be charged.

![Checkout page Desktop](/static/docs/img/features/checkout-desktop.png)


### Order Confirmation
When users have successfully processed their payment, they are taken to the order confirmation page which provides the user with a summary of the information their order contains. This page also provides the user with their order number.

![Order Confirmation](/static/docs/img/features/order-confirmation.png)

At the same time as the user is redirected to the order confirmation page, an email is sent to the email address they provided during the checkout process. This email provides the user with the same details as the order confirmation page, with the full address details summarised as the town and country only.


### User Profile
Registered users can access a log of all previous orders through the My Profile page. Here they are able to filter and search through their prior orders. Results are presented in the form of summary cards showing the order number, the items ordered, total order value and date of order.

![My Profile](/static/docs/img/features/my-profile.png)

Registered users can also access controls to make adjustments to the address that is stored with their account.


### News
Users have access to view News post articles written by the company. These articles will form part of the company SEO and web marketing strategies and allows them to include information on topics that will be interesting to their users. Clever use of the News post section of the site will allow the company to incorporate both short tail keywords and long tail keywords, providing answers to target users questions. This will improve their overall search engine ranking performance whilst providing users with beneficial information and improving their overall experience and trust within the company.
Users are able to select which News post to read through the summary list provided on the main News page.

![News Post Page](/static/docs/img/features/news-posts-desktop.png)

The News detail page provides the user with the full news post content

![News post detail page](/static/docs/img/features/news-detail-desktop.png)

Whilst employees will have access to additional options in order to access areas of the site that allow them to add, edit, delete News posts. 

![Employee view of News posts](/static/docs/img/features/employee-news-posts.png)


### About
The about page features a brief description of the charity and also gives details of the team members.

![EAbout Page](/static/docs/img/features/about-page.png)

Whilst employees will have access to additional options in order to access areas of the site that allow them to add, edit, delete team members.

![Employee view of Team](/static/docs/img/features/employee-team.png)


## Future Enhancements
The site has been launched with a minimal viable product phase in mind. Future developments would include:
* Product image carousels
* Product reviews
* Comments for news articles
* Donations page including recurring payments
* Account deletion on front end
* Extra payment methods
* Automated testing
* Update password from My Profile
* Login with social accounts


## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site. A full detailed breakdown of the testing procedures and methodology can be found in the testing.md file [here](TESTING.md).


## Technologies Used

* Python
* Django
    * Django was used as the main python framework in the development of this project
    * Django AllAuth was utilised to provide enhanced user account management functionality.
* Heroku
    * Was used as the cloud based platform to deploy the site on
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* JavaScript
* Bootstrap
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.
* Gitpod was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project
* Figma was utilised to develop wireframes for the site from which the design was based
* Affinity Photo was used to adapt images for use within the site.
* GraphViz was used to develop the database schema during development.

#### Resources Used

* The Django documentation was used extensively during development of this project
* The Django AllAuth documentation was used as a reference and a guide for implementing the package and its features.
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.

## Deployment
A repository was setup in GitHub using the Code Institute Gitpod full template.  Development was completed using Gitpod and code was regularly pushed back to the GitHub repository.  The master branch of this repository is the most current version and has been used for the deployed version of the site.

The current live website is hosted as a Heroku app, however the images and static files are hosted on an AWS simple storage service (s3).  Stripe is utilised for the management of financial transactions and Gmail is used for emails.  The instructions in this section cover the process to set up and use these services. 

# Running the project locally
To work on the project code locally a clone can be taken by following the steps below or downloading the files as a zip file. To see the options, open the desired repository and select the drop down menu button ???Code??? (found under the repo name and above the list of files).

## Clone:
To do this you will need Git for Windows installed.

*   Open Git.
*   Change the current working directory is required. On windows, by default, the files will be downloaded to the users file directory on the C: drive.
*   In the ???Code??? dropdown menu in GitHub, select either HTTPS or SSH and copy the link.
*   In the GitBash window type ???git clone??? and then paste the copied link:
```
  git clone https://github.com/chelsea-designs/bird-search-and-rescue.git
```
*   Hit Enter and the files will then be cloned to be worked on locally.

Please see [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) for the GitHub Docs page on this process.

The cloned repository includes the ???requirements.txt??? to enable the installation of the packages required for this project using the following command in the terminal:
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
  * *Value: Django secret key.  A good resource is [miniwebtool ??? django secret key  generator](https://miniwebtool.com/django-secret-key-generator/) and should be different to the same variable in the Heroku app.*
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
The following environment variables (in CAPS) must be set within the ???Config Vars??? section in Heroku for the deployed site to function correctly.   The config variables are added within the Heroku app by selecting the Settings tab, and under the heading 'Config Vars' clicking the button 'Reveal Config Vars' to show the key / value input boxes for the variables.  Instructions to obtain the variables are featured within below sections.

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
  * *Value: the email address of chosen email account (e.g. `john.smith@gmail.com`)*

## Deployment
In order to run properly, Heroku requires:
*	requirements.txt
*	Procfile

Both of these files should be within the cloned repository, so ensure these are pushed to your GitHub repository. 

To deploy the app to Heroku from the GitHub repository you will need to follow the below steps:
*	Go to [Heroku]( https://www.heroku.com/).
*	Log in and click on 'New' > 'create new app'.
*	Enter an App name (do not use spaces and use lower case letters).
*	Choose a region, then click ???create app???.
* Within the new app select the ???resources??? tab and under addons type in ???postgres??? to provision a new Heroku Postgres database (this will also add the required DATABASE_URL variable and value in the Heroku Config variables)

### Setup to auto-deploy when pushed to GitHub:
* Within the Heroku web dashboard, Click on the Deploy tab.
* Select deployment method as ???GitHub???, and then search for your repository below that.
* Once your repository name is returned, click 'connect'.
* Then click ???enable automatic deploys???

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
* Once logged in, under ???my account??? select ???AWS Management Console??? and search for the service ???s3???
* Once in the s3 interface create a new bucket for this project.
* Name the bucket and select a region closest to you.
* Uncheck block all public access and acknowledge that the bucket will be public.
* Select ???create bucket??? to finish and the bucket will be created.
* Under the bucket properties tab, select to ???edit??? Static website hosting and select ???enable???.
* Ensure that ???host a static website??? is selected and enter a default value for index as this will not be used for this project deployment.
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
* Next select to edit the bucket policy and select ???policy generator??? to generate a policy.  Before you do that, copy the ???Bucket ARN??? (you will also need this for setting up a group within Identity and Access Management below).
* Within the policy generator select policy type of ???S3 Bucket Policy???
* Within Add Statements, select ???allow??? for effect and type a star within ???Principal???:  
* For Actions select only ???GetObject???:  
* Then below that paste in the ???bucket ARN into the Amazon Resource Name input box.
* Click ???Add Statement???, then ???Generate Policy???
* Copy the policy into the bucket policy editor and then so as to allow access to all resources in this bucket, add a slash star onto the end of the resource key:
* Click Save.
* Next select to edit the Access control list and set the list objects permission for everyone under the Public Access section as below:  
 
## Create access policy, group and user
### Create Group and Policy
* Within the AWS services menu open Iam (Identity and Access Management) and in the left hand menu click ???User groups??? to create a new group.
* Name a new group and click ???create group???.
* Click ???policies??? so as to create a policy used to access the new bucket.
* Click ???create policy??? and then select the ???JSON??? tab and select ???import managed policy???.
* Within the search input, search for s3 and then select to import the Amazon s3 full access policy.  
* Modify the policy by entering the ARN from the bucket policy in s3 as the value for resource.
* Click ???Next: Tags??? and then click ???Next: Review???
* Provide a name and description for the policy and click ???Create policy???.

### Attach policy to group.
* Within the AWS services menu open Iam and in the left hand menu click ???User groups??? to view the newly created group.
* Select the new group and click on the permissions tab
* Click the ???Add permissions??? button and select ???Attach Policies??? from the drop down.
* Select the policy that was just created, by checking the tick box and click on ???Add permissions???

### Create User and add to group.
* Within the AWS services menu open Iam and in the left hand menu click ???Users??? and then select ???Add users???
* Provide a name for the user, check the tick box to grant the user access and select next.
* Check the tick box next to the group just created to add the user to the group.  Click through the next few pages to create user.
* **!IMPORTANT:** On the success page, click 'Download .csv file' which contains the user access key and secret access key needed to authenticate them from the Django app.

## Connect Django to AWS s3 bucket.
Within the Django app settings python file enter the name and region name for the AWS s3 bucket that you have set up.

Within Heroku add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to the config variables and also add a USE_AWS key and set it to true.  The access key and secret key are contained with the **downloaded csv file**.

Once that is done, git add, commit and push the changes which will trigger a deployment to Heroku.  Check the Heroku build log to check that the static files were collected and there should be a 'static' folder within the s3 bucket. 

## Add media files to s3 bucket
The below instructions detail how to do this within the s3 management interface.

* Within the s3 bucket overview click create folder and call it media.
* Inside that folder click on ???upload??? and then ???add files???
* Select all of the product images (found within the repo download performed earlier) and click open
* Click next and then under permissions, check the box for ???grant public-read access???.
* Then click upload.
* There should now be a 'media' folder within the s3 bucket containing the images. 

# Stripe Setup
* Create a [Stripe](https://stripe.com) account or log in to existing.
* On the Stripe dashboard, under ???Developers??? copy the ???test API key??? and ??? Secret key???.  Use these as the values for the environment and Heroku variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY as detailed above. 

## Create new webhook end point.
**NOTE:** Two separate webhooks will need to be setup. One for the development environment and one for the Heroku app.
* Run the application to get the address of the site.  Copy this and go to the Stripe dashboard.
* Click ???Developers???, select ???webhooks??? and then click ???Add endpoint???.
* Paste in the site URL and add to the end ???/checkout/wh/???.
* Click ???Select Events??? and select the events to listen to as:
```
  ???payment_intent_suceeded??? 
  ???payment_intent_failed???
```
* In the newly created webhook endpoint details the ???signing secret??? is now available.  Copy this and add it to the value for the environment and Heroku variable STRIPE_WH_SECRET as detailed above.
* Within the Stripe dashboard for that webhook, click ???send test webhook??? and verify that it is working.

The STRIPE_CURRENCY variable is defined within the Django app 'settings' python file and is set to ???gbp???.  If a different currency is needed then this will need to be changed.  See this link for [supported currencies](https://stripe.com/docs/currencies#presentment-currencies)

# Email Setup
The below instructions cover the setup using a [Gmail](https://google.com) account.

* Log in to your email account or set one up.
* Click account settings, and select the 'Accounts and Import' option from the top selection
* Under ???Change account settings??? click ???Other Google Account settings???
* Click on the ???security??? option on the left and then under ???Signing in to Google??? click on ???2-Step Verification???
* Click ???get started???, enter password and then work through the verification.
* Once verification is done and 2-Step verification is turned on, a new option now shows under the previous ???Signing in to Google??? menu screen.
* In this, on the App passwords screen, select from the dropdowns; ???mail??? for app and ???other??? for device.  Add an appropriate name and click ???generate???.
You will then be given a 16 character password which you will need to copy.

## In Heroku.
Within the Heroku Config variables add the 16 character password as the value to the variable ???EMAIL_HOST_PASS???.  Add another variable called ???EMAIL_HOST_USER??? and set the value as the gmail account email used.

------


## Credits

* Hero image by [Mauri Karlin on Unsplash](https://unsplash.com/@rovaniemi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

## Acknowledgements
* Tutor support
