# Test Cases and Execution Report

To navigate back to the main README click [here](README.md)

## Validators

### Python Validation
The Python code was checked using the flake8 python linter using the command python3 -m flake8. No errors were reported by the validator in the files I created. The settings.py file did however did contain an error for env being imported but unused, which is a false positive. Similarly, another error in checkout/apps.py however 'checkout.signals' is being passed in and used elsewhere, so is not an issue.

* Screenshots of the validator report is [here](static/docs/img/validators/python-validation.png) 


### JavaScript Validation
The JavaScript code was checked using the jshint.com validator available at [jshint.com](https://jshint.com/). No errors were detected within the files I created, however, the quantity-input-script from the Boutique Ado has some errors but not affecting the functionality.

* Screenshot of the validator report is available here:
    * JavaScript
        * [countryfield.js file](/static/docs/img/validation/country-field-js.png)
        * [quantity_input file](/static/docs/img/validation/quantity-input-script.png)
        * [stripe-elements.js file](static/docs/img/validators/stripe-elements-js.png)


### CSS Validation

The full CSS Validator report is available here on the [CSS Validator Site](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fbird-sandr.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#warnings) . When validating by url it discovers a total of 707 warnings relating to imported bootstrap code plus the 3 vendor prefix warnings. When validating by direct input the validator reports three warnings for the main base.css file, the warnings only relate to the use of vendor prefixes can be safely ignored.

* [CSS Validator Report - base.css](static/docs/img/validators/base-css.png)
* [Checkout CSS file results](static/docs/img/validators/checkout-css.png)


### HTML Validation
Due to the way Django templates include Django template code in them, and extend other templates, it is not possible to copy the code for each page out of the source html files. Therefore, in order to validate the code correctly, I used the deployed urls for validating pages which do not require a login. I used the HTML validator site available at [W3C Markup Validation Service](https://validator.w3.org/). When validating the pages accessible by url - those that do not require a login - there were no errors returned from the HTML produced from the templates themselves. 

In order to validate pages which do require a login, I navigated to the site and accessed the rendered html code through the developer tools on Google Chrome. When copying and pasting the code from the brower into the direct input option within the validator, it shows no errors.

Pages with a Summernote text editor will return six (6) HTML validation errors. These errors are generated by the iframe code the summernote editor inserts. One appears to be related to the summernote code having a hidden text area input - whilst the others are related to styling rules that are being applied to the summernote editor field. As they are inserted by the summernote editor they have been ignored.

* [Home](/static/docs/img/validation/home-home.png)


#### Lighthouse Testing
Google's lighthouse testing was utilised to gain an overall assessment of the performance of the site. Whilst all the areas of the test return a green score above 98, the overall performance figure fluctuates depending on the speed of the internet connection when the test is performed, having returned scores as low as 92 and as high as 100 whilst running the test multiple times. The best practice score is impacted by the stripe included javascript files along with the use of the bootstrap and jquery libraries. The SEO score returned a perfect 100.

![Google Lighthouse Results](/static/docs/img/lighthouse.png)



#### Notable Bugs

*