# Test Cases and Execution Report

To navigate back to the main README click [here](README.md)

## Validators

### Python Validation
The Python code was checked using the flake8 python linter using the command python3 -m flake8. No errors were reported by the validator in the files I created. The settings.py file did however did contain an error for env being imported but unused, which is a false positive. Similarly, another error in checkout/apps.py however 'checkout.signals' is being passed in and used elsewhere, so is not an issue. I also decided to disregard line too long errors on somelines such as secret keys etc.

* Screenshots of the validator report is [here](static/docs/img/validators/python-validation.png) 


### JavaScript Validation
The JavaScript code was checked using the jshint.com validator available at [jshint.com](https://jshint.com/). No errors were detected within the files I created, however, the quantity-input-script from the Boutique Ado has some errors but not affecting the functionality.

* Screenshot of the validator report is available here:
    * JavaScript
        * [countryfield.js file](/static/docs/img/validators/country-field-js.png)
        * [quantity_input file](/static/docs/img/validators/quantity-input-script.png)
        * [stripe-elements.js file](static/docs/img/validators/stripe-elements-js.png)


### CSS Validation

The full CSS Validator report is available here on the [CSS Validator Site](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fbird-sandr.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#warnings) . When validating by url it discovers a total of 707 warnings relating to imported bootstrap code plus the 3 vendor prefix warnings. When validating by direct input the validator reports three warnings for the main base.css file, the warnings only relate to the use of vendor prefixes can be safely ignored.

* [CSS Validator Report - base.css](static/docs/img/validators/base-css.png)
* [Checkout CSS file results](static/docs/img/validators/checkout-css.png)


### HTML Validation
Due to the way Django templates include Django template code in them, and extend other templates, it is not possible to copy the code for each page out of the source html files. Therefore, in order to validate the code correctly, I used the deployed urls for validating pages which do not require a login. I used the HTML validator site available at [W3C Markup Validation Service](https://validator.w3.org/). When validating the pages accessible by url - those that do not require a login - there were no errors returned from the HTML produced from the templates themselves. 

In order to validate pages which do require a login, I navigated to the site and accessed the rendered html code through the developer tools on Google Chrome. When copying and pasting the code from the brower into the direct input option within the validator, it shows no errors.

Pages with a Summernote text editor will return six (6) HTML validation errors. These errors are generated by the iframe code the summernote editor inserts. One appears to be related to the summernote code having a hidden text area input - whilst the others are related to styling rules that are being applied to the summernote editor field. As they are inserted by the summernote editor they have been ignored.

* [Home](/static/docs/img/validators/home-html.png)
* [News](/static/docs/img/validators/news-html.png)
* [Team](/static/docs/img/validators/team-html.png)
* [Login](/static/docs/img/validators/login-html.png)
* [Register](/static/docs/img/validators/register-html.png)

## Other tests
### Lighthouse Testing
Google's lighthouse testing was utilised to gain an overall assessment of the performance of the site. Whilst all the areas of the test return a green score above 98, the overall performance figure fluctuates depending on the speed of the internet connection when the test is performed, having returned scores as low as 92 and as high as 100 whilst running the test multiple times. The best practice score is impacted by the stripe included javascript files along with the use of the bootstrap and jquery libraries. The SEO score returned a perfect 100.

![Google Lighthouse Results](/static/docs/img/lighthouse.png)

### Accessibility Testing
I verified the sites accessibility using [WAVE](https://wave.webaim.org/report#/https://bird-sandr.herokuapp.com/#) which returned only one alert, with no errors. The alert notified of a redundant link, however this was an intentional choice to have this, therefore I'm happy to disregard this alert:
![WAVE Results](static/docs/img/wave-results.png)

## User Story Testing

All of the below user stories have been tested manually and passed, all documented with screenshots in this [manual testing pdf](static/docs/manual-testing.pdf)

### Viewing and Navigation
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Viewing and Navigation_**                                      |                                                                                       |
| 1   | Customer   | View list of products                                             | Find something to purchase                                                            | Pass |
| 2   | Customer   | View details of product                                           | See Price, Description, Image, and Sizes i/a                                          | Pass |                                                |
| 3   | Customer   | See my bag's total at any time                                   | Avoid spending too much                                                               | Pass |

### Registration and User Accounts
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Registration and User Accounts_**                              |                                                                                       |
| 4   | Reg User   | Register for an account                                           | Save my delivery details and order history                                            | Pass |
| 5   | Reg User   | Quickly login/out                                                 | Access my account                                                                     | Pass |
| 6   | Reg User   | Request a password reset                                          | receive and email to reset my password in case I forget it                            | Pass |
| 7   | Reg User   | Receive an email to verify my registration                       | Verify my account was registered successfully                                         | Pass |
| 8   | Reg User   | Access my user profile                                            | View my order history, manage my personal details                                     | Pass |

### Sorting and Searching
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Sorting and Searching_**                                       |                                                                                       |
| 9   | Customer   | Sort the list of all available products                               | See the products in a list sorted by price, rating, quantity available etc            | Pass |
| 10  | Customer   | Sort a category of products                                       | See the products in a category sorted by name, price, rating, etc                     | [Pass |
| 11  | Customer   | Filter products by category                           | See the products in a specified category | Pass |
| 12  | Customer   | Search for product                                                | Find a specific item I wish to purchase                                               | Pass |
| 13  | Customer   | View a list of search results                                     | See if the product I want is available to purchase                                    | Pass |

### Purchasing and Checkout
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Purchasing and Checkout_**                                     |                                                                                       |
| 14  | Customer   | Easily select the size and quantity whilst purchasing an item     | Ensure I don't accidentally select the wrong product, quantity, or size               | Pass |
| 15  | Customer   | View items in my basket                                           | See what items are in my basket at a glance to ensure the items are correct           | Pass |
| 16  | Customer   | Adjust the quantity of individual items in my bag                 | Easily adjust the amount of an item I intended to purchase (including removing)       | Pass |
| 17  | Customer   | Easily enter my payment information                               | Checkout quickly, without hassle                                                      | Pass |
| 18  | Customer   | Feel my payment and personal information is secure                | Provide the needed payment and personal information, and feel it is handled safely    | Pass |
| 19  | Customer   | View order summary before completing purchase             | Verify I haven't made any mistakes                                                    | Pass |
| 20  | Customer   | Receive confirmation email after checking out                     | To keep my own record of the purchase                                                 | Pass |

### Admin and Store Management
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_Admin and Store Management_**                                  |                                                                                       |
| 21  | Staff      | Add a product                                                     | Add new products to my store                                                          | Pass |
| 22  | Staff      | Edit/update a product                                             | Change the price, description, images etc of a product                                | Pass |
| 23  | Staff      | Delete a product                                                  | Remove items that aren't for sale anymore                                             | Pass |
| 24  | Staff      | Add a team member                                                 | Add new products to my store                                                          | Pass |
| 25  | Staff      | Edit/update a team member                                         | Change the price, description, images etc of a product                                | Pass |
| 26  | Staff      | Delete a team member                                              | Remove items that aren't for sale anymore                                             | Pass |
| 27  | Staff      | Add a news post                                                 | Add new news posts to news section                                                         | Pass |
| 28  | Staff      | Edit/update a news post                                         | Change the title, description, images etc of a post                                | Pass |
| 29  | Staff      | Delete a news post                                             | Remove posts that aren't needed anymore                                             | Pass |

### News Section
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_News Section_**                                                |                                                                                       |
| 30  | Customer   | View list of news articles                                        | Choose a news article to read                                                         | Pass |
| 31  | Customer   | View full news article                                            | Read detailed about latest news and activities                                                   | Pass |

### About Section
| ID  | As A/An    | I want to...                                                      | So I can...                                                                           | Pass |
| --- | ---------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --- |
|     |            | **_About Section_**                                               |                                                                                       |
| 32  | Customer   | View list of team members                                         | Learn about the team                                                         | Pass |


## Notable Bugs

* The summernote widget was displaying a 'Refused to connect', I added X_FRAME_OPTIONS = 'SAMEORIGIN' into settings.py which fixed this issue.

* Quantity input on product details page would not work, this is an issue with Code Institute's code from Boutique Ado which has been discussed with tutor support, it now will let you increase and decrease but will not disable outside of 1-99 range. Unfortunately it is only working on mobile not desktop. I will continue to try fix this after submission.
