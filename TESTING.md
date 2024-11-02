# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

Feature-by-Feature Testing:

Go through each feature of your portfolio site and detail the testing process for each.

Explain the functionality and demonstrate how it aligns with the intended purpose. This could include:

- Navigation: Ensuring smooth transitions between pages, links directing to the correct destinations.
- Responsive Design: Checking for compatibility across various devices and screen sizes.
- Portfolio Display: Verifying that projects are properly showcased with accurate descriptions, images, and links.
- Contact Form: Testing the form submission process, ensuring the user receives a confirmation, and you receive the message.

User Experience Testing:

- Usability Testing: Have users (or simulated users) interact with the site and provide feedback. Document any issues encountered and the resolutions implemented.
- Accessibility Testing: Confirm compliance with accessibility standards (e.g., screen reader compatibility, proper alt text for images, keyboard navigation).

Compatibility Testing:

- Browser Compatibility: Testing on different browsers (Chrome, Firefox, Safari, Edge, etc.) to ensure consistent performance.
- Device Compatibility: Ensuring functionality across various devices (desktops, laptops, tablets, and mobile phones).
- Performance Testing (optional):
	- Speed and Load Testing: Tools like PageSpeed Insights or GTmetrix to check page load times and optimize where necessary.
	- Scalability Testing: Assess how the site handles increased traffic or usage.

Regression Testing:

After implementing fixes or updates, ensure that previous features and functionalities still work as intended. This prevents new changes from breaking existing features.

Documentation and Logs:

Maintain records of testing procedures, results, and any bugs encountered along with their resolutions. This helps demonstrate a systematic approach to testing and problem-solving.
User Feedback Incorporation:

If applicable, mention how user feedback has been taken into account and implemented to enhance the user experience.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Code Validation

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use the space to discuss code validation for any of your own code files (where applicable).
You are not required to validate external libraries/frameworks, such as imported Bootstrap, Materialize, Font Awesome, etc.

**IMPORTANT**: You must provide a screenshot for each file you validate.

**PRO TIP**: Always validate the live site pages, not your local code. There could be subtle/hidden differences.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| guidetrip | all_trips.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| home | index.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| templates | banner.html | ![screenshot](documentation/validation/path-to-screenshot.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | base.css | ![screenshot](documentation/validation/path-to-screenshot.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| guideflyfishing | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/guideflyfishing/settings.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| guideflyfishing | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/guideflyfishing/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| guidetrip | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/guidetrip/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| guidetrip | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/guidetrip/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| guidetrip | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/guidetrip/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| guidetrip | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/guidetrip/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| home | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/home/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| home | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/home/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/home/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/home/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/Project-guideFlyFishing/main/manage.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |

## Browser Compatibility

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various browsers.

Consider testing AT LEAST 3 different browsers, if available on your system.

You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the tested browsers, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time.
Some of these are paid services, but some are free.
If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

Sample browser testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-chrome-edge.png) | ![screenshot](documentation/browsers/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-etc.png) | Minor CSS differences |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-about.png) | ![screenshot](documentation/browsers/browser-brave-contact.png) | ![screenshot](documentation/browsers/browser-brave-etc.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-about.png) | ![screenshot](documentation/browsers/browser-opera-contact.png) | ![screenshot](documentation/browsers/browser-opera-etc.png) | Minor differences |
| repeat for any other tested browsers | x | x | x | x | x |

## Responsiveness

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is for the following 3 tests:
- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of the tested responsiveness, to "prove" that you've actually tested them.

Using the "amiresponsive" mockup image (or similar) does not suffice the requirements.
Consider using some of the built-in device sizes in the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well.
It showcases a higher level of manual tests, and can be seen as a positive inclusion!

Sample responsiveness testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-about.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-etc.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-about.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-etc.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-about.png) | ![screenshot](documentation/responsiveness/responsive-desktop-contact.png) | ![screenshot](documentation/responsiveness/responsive-desktop-etc.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsiveness/responsive-xl-home.png) | ![screenshot](documentation/responsiveness/responsive-xl-about.png) | ![screenshot](documentation/responsiveness/responsive-xl-contact.png) | ![screenshot](documentation/responsiveness/responsive-xl-etc.png) | Scaling starts to have minor issues |
| Google Pixel 7 Pro | ![screenshot](documentation/responsiveness/responsive-pixel-home.png) | ![screenshot](documentation/responsiveness/responsive-pixel-about.png) | ![screenshot](documentation/responsiveness/responsive-pixel-contact.png) | ![screenshot](documentation/responsiveness/responsive-pixel-etc.png) | Works as expected |

| repeat for any other tested devices | x | x | x | x | x |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| All Trips | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Some minor warnings |
| Detail trips  | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| Bag  | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| checkout  | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| checkout | | | | | |
| | All customer fields on this page are mandatory with the exception of "street addres 2", and county and postcode | Tested by entering data in ome dtaa field at a time and then trying to submit the form | The feature behaved as expected, was prompted to complete fields | Test concluded and passed | ![screenshot](documentation/img/testing/checkout1.jpg) |
| | Credit card field and CC data fileds are mandatory | Tested by completing address fields and then trying to submit the form without CC details| The feature behaved as expected, was prompted to complete fields | test concluded and passed | ![screenshot](documentation/img/testing/checkout2.jpg) |
| profile  | | | | | |
| | You should only be able to see your own order history in profile | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Admin | | | | | |
| | User who are not setup a s superuser cannot logon onto the admin page  | Tested the feature by logging out  | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | users who are not logged in cannot access the admin page or brute force to it | Tested the feature by logging out and then entering the admin URL manaually in the browser | Behaved as expected, I was taken to the logon page and barred access unless I entered credentials | Test concluded and passed| ![screenshot](documentation/img/testing/admin_acc1.jpg) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Automated testing 
As part of my testing of pages I created some automated tests in Django for the purpose of testing urls and views were working Eg i could load the page, the following points explain there purpsoe in more detail.

- Automated test to test URL links (as in views.py/urls.py) in Guideflyfishing 
- Regression testing when I made changes these were still functioning as expected 
- The pages would load e.g. no 404 errors 

![screenshot](documentation/img/testing/autotest.jpg)



# Bugs

## Bootstrap Errors Not Targeting Navbar Elements Correctly   

When i first setup Boot strap navbar using version 5.3, the drop down menus did not function correctly, as when you clickd on the 
the menu it did not drop down. After some very extensive research and collaboration, this was found to be a problem with changes
in bootstrap version 4.0 used in walkthrough and version 5.3    
the data target element in html has been updated in bootstrap 5.3 from
data-target 
to 
data-bs-target

Once corrected with data-bs-target in main.nav to define as a target this all worked  
This change was made in 5.3 to allow mutiple styling frameworks to be used. 

## Receiving Errors When I Push My Code To Github
    After Renaming my project in gitpod - to conform with naming guidance I started receiving the following error when I pushed code. 
    ```shell
            remote: Resolving deltas: 100% (1/1), completed with 1 local object.
            remote: This repository moved. Please use the new location:
            remote:   https://github.com/Coelecanth/Project4-guideflyfishing.git
            To https://github.com/Coelecanth/Project-guideFlyFishing.git
    ```
    The error is quite self explanatory, once I had correctly renamed the github site the errors were removed and and push worked without errors 

## Couldn’t Deploy App In Heroku With Auto Deploy     
    Received the following error in the Heroku log when trying to build app in heroku   

    	```shell
		    Collecting django-allauth==0.41.0 (from -r requirements.txt (line 4))
            Downloading django-allauth-0.41.0.tar.gz (545 kB)
            Preparing metadata (setup.py): started
            Preparing metadata (setup.py): finished with status 'error'
            error: subprocess-exited-with-error
    
            × python setup.py egg_info did not run successfully.
            exit code: 1
            [6 lines of output]
            Traceback (most recent call last):
            File "<string>", line 2, in <module>
            File "<pip-setuptools-caller>", line 34, in <module>
            File "/tmp/pip-install-ilh6jue2/django-allauth_02d68af6a9de44a490287dfb398a4bbe/setup.py", line 8, in <module>
            from setuptools import convert_path, find_packages, setup
            ImportError: cannot import name 'convert_path' from 'setuptools' (/app/.heroku/python/lib/python3.12/site-packages/setuptools/__init__.py)
            [end of output]
    
            note: This error originates from a subprocess, and is likely not a problem with pip.
            error: metadata-generation-failed
            
            × Encountered error while generating package metadata.
            See above for output.
    	```
    Heroku would not build and deploy python app, using Autodeploy in Heroku.  
    The above log excerpt from heroku build shows there is an issue with Allauth app, this was corrected by 
    moving from version 0041 as prescribed in the project walkthrough and moving to later version of 0054
    this was installed using the following command  pip3 install django-allauth==0.54.0
    

## The Update Button In The Bag Page Does Not Update The Values

the Update function in the bag does not work and behaves like there is no link. This wwas found to be a problem with the location of the tags in Bag.html,
which intiate the JS script to implement this function. Moved the a calls elelemts containing the JS scipt listeners outside the form element. 
the following code snippets show the before and after for bag.html 

```html
<!-- Original code -->
            <button class="increment-qty btn btn-sm btn-black rounded-0"
                    data-item_id="{{ item.item_id }}" id="increment-qty_{{ item.item_id }}">
                    <span><i class="fas fa-plus fa-sm"></i></span>
            </button>
            </div>
            </div>
        </div>
    <a class="update-link text-dark float-left"><small>Update</small></a>
    <a class="remove-item text-danger float-rig ht" id="remove_{{ item.item_id }}"><small>Remove</small></a>
    </form>    

<!-- Revised fix     -->
             <button class="increment-qty btn btn-sm btn-black rounded-0"
                    data-item_id="{{ item.item_id }}" id="increment-qty_{{ item.item_id }}">
                    <span><i class="fas fa-plus fa-sm"></i></span>
            </button>
            </div>
            </div>
        </div>
        </form>
        <!-- Do not put links inside the form as this break the update function it should remain outside the form tag -->
        <a class="update-link text-dark float-left"><small>Update</small></a>
        <a class="remove-item text-danger float-right" id="remove_{{ item.item_id }}"><small>Remove</small></a>
```

## Toast messages in the Application did not apply corectly  

    Following the course guidance on implementing toasts in the project walk through, the explanation omitted details 
    on the implementation of toast messages. In particualr it was not explained that the implemetation 
    described would produce a toast message only on the first addition of an item to the bag. It was not clear 
    if was an oversite or by design. In my implementation I wanted the toast message to appear 
    everytime an item was added to the bag.    

    To fix this i amended/added the following code to views.py in Bag app 
```python

# Original code - where toast is only raised on the first 
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = trips.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        # missing code element here here to 
        # call toast message on subsequent additions
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.venue} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

# Revised code to provide toasts on all additions to the bag
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = trips.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        # call toast message on subsequent additions
        messages.success(request, f'Added {product.venue} to your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.venue} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


```

## The Sorting Functionality from The Main Navigation Did Not Work

When selecting the sort function code would run but return no values were returned in the list. 
This was found to be a problem I had inadvertently introduced when correcting an earlier problem with getting viewing items by category to work and using specific variables to make the code easier to understand. In doing I had precluded myself from making the code compatible with sorting. 
So the image below show the original commented out code (in greeen)  followed by the amendments made to correct it directly following each commented out line 
So, in essence this recreates a new value called all_trips_rec instead of redefining all_trips  

![screenshot](documentation/img/errors/code-1.jpg)


## Web log returning error 404 for site URL for webhooks 

```log
[26/Oct/2024 12:54:20] "GET /trips/ HTTP/1.1" 200 32726
[26/Oct/2024 12:54:24] "GET /trips/4 HTTP/1.1" 200 17764
[26/Oct/2024 12:54:25] "POST /bag/add/4/ HTTP/1.1" 302 0
[26/Oct/2024 12:54:26] "GET /trips/4 HTTP/1.1" 200 20326
[26/Oct/2024 12:54:29] "GET /checkout/ HTTP/1.1" 200 21063
[26/Oct/2024 12:54:29] "GET /static/js/stripe_elements.js HTTP/1.1" 304 0
Not Found: /wh
[26/Oct/2024 12:54:29] "POST /wh HTTP/1.1" 404 2743
[26/Oct/2024 12:55:00] "POST /checkout/cache_checkout_data/ HTTP/1.1" 200 0
Not Found: /wh
[26/Oct/2024 12:55:01] "POST /wh HTTP/1.1" 404 2743
Not Found: /wh
[26/Oct/2024 12:55:01] "POST /wh HTTP/1.1" 404 2743
[26/Oct/2024 12:55:02] "POST /checkout/ HTTP/1.1" 302 0
[26/Oct/2024 12:55:03] "GET /checkout/checkout_success/B6221586515F45EFA645B4D92F3C1DBB/ HTTP/1.1" 200 16424
Not Found: /wh
[26/Oct/2024 12:55:03] "POST /wh HTTP/1.1" 404 2743

```
On closer inspection this was found to be a configuration error made in Stripe, where the endpoint webhook created stripe 
need to be amended

```log
- https://8000-coelecanth-projectguide-5jtcemqmdr7.ws.codeinstitute-ide.net/wh  
  to 
- https://8000-coelecanth-projectguide-5jtcemqmdr7.ws.codeinstitute-ide.net/checkout/wh
```


## Missing alternate image caused site to crash 

While I was regression testing checkout app,  I added an item to the bag with with a missing image file, this caused the site to crash.
I received the following error message  
```log
ValueError at / The 'image' attribute has no file associated with it. 
Request Method: GET Request URL: http://8000-coelecanth-projectguide-5jtcemqmdr7.ws.codeinstitute-ide.net/ 
Django Version: 3.2 Exception Type: ValueError Exception Value: The 'image' attribute has no file associated with it.

``` 
Refering to a line in the checkout template  

Th error was caused by a missing image file and no logic to handle this situation. 
This was corrected by adding an if statement around {{ item.product.image.url }}, with an latertive to the noimage image of {% static 'img/noimage.jpg' %}
To correct this I added the following code below checkout template, and then also had to add the load "static" statement on the toasts success page as this was 
also using a product image. 

```html
            <p class="logo-font bg-toast py-1">Your Bag ({{ product_count }})</p>
            <div class="bag-notification-wrapper">
                {% for item in bag_items %}
                    <div class="row">
                         <div class="col-3 my-1">
                        <!-- the below line was replaced by the following code -->
                        <!-- <img class="w-100" src="{{ item.product.image.url }}"> -->
                            <!-- replaced code start -->
                            {% if item.product.image %}
                                <img class="w-100" src="{{ item.product.image.url }}" alt="{{ item.product.venue }}">
                            {% else %}
                                <img class="w-100" src="{% static 'img/noimage.jpg' %}" alt="Default image">
                            {% endif %}
                            <!-- replaced code end -->
                        </div>
                        <div class="col-9">
                            <p class="my-0"><strong>{{ item.product.venue }}</strong></p>
                            <p class="my-0 ">Qty: {{ item.quantity }}</p>
                        </div>
                    </div>
                {% endfor %}
            </div>

``` 
## Site producing duplicate orders when submitting from checkout  

Site was producing duplicate orders when purchasing with Stripe, 2 orders were created in the orders database but one payment was produced in Stripe. 
After some investigation into this, the reason for this was in the implementation of the webhooks I had used, 
I had used only one set of details for the customer, e.g. as I was not shipping any products to people as they were buying a service. 
For this reason I had implemented just the billing Information only to validate the webhook's order against. This caused an issue when the 
test data being used, As I was using a different postcode for credit card and the billing address (e.g. the validation field for stripe credit card) 
which caused duplicate orders when in the database as the postcodes did not match. 
To avoid this error I changed the code in webhooks_handler.py to not evaluate the using postcode 
but continued to use all the other fields to validate the order, this would still allow strong validation of the user and payment but successfully resolved the issue.


the below code is shown from Webhook_handler.py shows the line thats was removed (commented out). 
```python
order_exists = False
attempt = 1
while attempt <= 5:
    try:
        order = Order.objects.get(
            full_name__iexact=billing_details.name,
            email__iexact=billing_details.email,
            phone_number__iexact=billing_details.phone,
            street_address1__iexact=billing_details.address.line1,
            street_address2__iexact=billing_details.address.line2,
            town_or_city__iexact=billing_details.address.city,
            # the following commented out line was removed 
            # postcode__iexact=billing_details.address.postal_code
            county__iexact=billing_details.address.state,
            country__iexact=billing_details.address.country,
            grand_total=grand_total,
            original_bag=bag,
            stripe_pid=pid,
        )
        order_exists = True
        break

```


## Web Server Errror 500 and no reverse route found for Page 

When creating edit capability for the products page, I received the following message where the reverse was route failing, detailing it had received no product.Id 
After making sure that views.py was receiving and passing the product.id to the template 

![screenshot](documentation/img/errors/reverse_err.jpg)


The problem was eventually traced to the template edit_procuct,html and where the product id in the django field was incorectly specified with "_" instead of ".". 
This was fixed with the following changes showing the before an after in the code.   



```html
    <!-- the following line was changed form the below to uncommneted out line to corect the issue -->
<!-- <form method="POST" action="{% url 'edit_product'  product_id %}" class="form mb-2" enctype="multipart/form-data"> -->
     <form method="POST" action="{% url 'edit_product'  product.id %}" class="form mb-2" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form | crispy }}
        <div class="text-end my-2">
            <a href="{% url 'alltrips' %}"
                class="shop-now-button-small btn btn-outline-black rounded-1 btn-lg text-uppercase"">
                    <span class=" icon"><i class="fas fa-chevron-left"></i></span>
                <span>Cancel</span>
            </a>
            <button class="shop-now-button-small btn btn-outline-black rounded-1 btn-lg text-uppercase"
                type="submit">Update Product</button>
        </div>

    </form>

```





    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.











## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
