# [PROJECT GUIDEFLYFISHING](https://p4guideflyfishing-879a54f37efc.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Coelecanth/Project-guideFlyFishing)](https://github.com/Coelecanth/Project-guideFlyFishing/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Coelecanth/Project-guideFlyFishing)](https://github.com/Coelecanth/Project-guideFlyFishing/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Coelecanth/Project-guideFlyFishing)](https://github.com/Coelecanth/Project-guideFlyFishing)

So for my commercial Website project (called "Guide Fly Fishing"), I took the idea that I had used in my previous projects and developed this into further extension of the idea and business of a fly fishing business which would complement my previous. In the the previous iterations I had a site advertising a fly fishing destination in Alaska and a flyfishing blog. I took this idea and thought about how this would be further developed, I came up with the idea of having a commercial site where you could visit and purchase guided fly fishing days, as an end user. The site is primarily targetted at UK based customers, to allow them to purchase guided fly fishing (it does however cater for people and business outisde the Uk guided fly fishing as well). 

![screenshot](documentation/img/gen/screen-mockup.jpg)

### Who is this aimed at?
The site is primarily aimed at fly fisher looking for expert knowledge at a venue or trip they would like make and then fish at. There are sites out there currently offering something similar, but they are not able to aggreagte a wholw host of trips from different vendors/individuals into a singel place with conveiniece to purchase difrectly.
The thypical vendor who would use this is intended to be small business to single inviduals offering there services to fly fishing audience.

### How would it work 
The site works on the principal that guides or even lodges could potentially offer there service and then customer can purchase directly guided trips from the site. 
So the guide or venue, can crete a "trip" that advertises a particualr place/venue, spacess avaiable,  with dates ,and number of days duration and cost.
The purchase mechansim works very much like the big commercial websites (amazon, ebay as an example) where the money is paid to the host organaisation and then supplier of the service is paid. The payment of service supplier is beyond the scope of this.      

## UX
I started creating the site to try and make a site that was pleasing to the user, but also easy to use without any need for instruction, and the site to be as informative as possible as users interacted with it, such as add items to the bag, etc.
The overall design of the site I wanted to depart from previous ideas of reflecting the natural world and so went for a more water-based colour theme, but still keeping the site as user friendly as possible by standardising on elements such as making the buttons have good contrast where ever they are used. 

### Navigation bar
I based the design of my site on some of the elements of the teaching material in the course, I particularly liked the navigation bar that was used, for several reasons 
 - First it has good responsiveness across screens 
 - Provides all the information for user navigation and interaction in one place  
 - Used Bootstrap which I had found to be a highly configurable and stable solution to the give CSS and styling I wanted. I have used materialize in previous projects and found this to be troublesome in some areas.

### Creating user Focus
I chose to represent content using a container (banner) which was placed over the scenic river image, this visaul approach is highlighted in the image below showing how the content can be contained in this and so drawing the users focus to this.  

| Description | Image | 
| --- | --- | 
| Image protraying the visual approach used with the blue container overlaid on the image so focusing the users attention |![screenshot](documentation/img/gen/ind-contianer.jpg)|  


This provided many benefits other than just focus element, some of these are listed below:
 - It allowed me to create the strong sense of theme i wanted for the site, with colours and image visibility.
 - The container could easily be adjusted to accommodate placement based on changing size of the navbar and its height, and screen size.
 - The banner concept fitted readily into Django idea of includes and could be made to be part of framework to seperate its formatting and therefor styling easily.
 - The width and height of the content could be easily adjusted with this banner approach to help with smaller screens, in making it wider or longer or both.
 - The banner provided a high contrast background for the content of the site, stopping any problesm to overlay text on the image and having to make this visible on ana individual basis. 
 - The construcion of the banner allows it to resize with the content being displayed. 


### Colour Scheme

So I chose quite a dark colour scheme 9reflecting water, one of the key themes for a fishing site, so I could create a good contrast on the pages between text and background.  

- `#000000` used for primary text on alternate backgrounds 
- `#FFFFFF` used alternate backgrounds 
- `#001242` used for background colour primary text image contianer.
- `#00537C` used for border on primary text image contianer.
- `#0094c6` used for links and focus items.

I used [coolors.co](https://coolors.co/e84610-009fe3-4a4a4f-445261-d63649-e6ecf0-000000) to generate my colour palette.

![screenshot](documentation/img/gen/color-pal-final.jpg)

### Typography

I used the fontjoy website to create a palete of fonts for selection but after experimenting with these and font effects. 
I decided to use just one fornt and created differentation by using text effect like all captials or strong which i found gave me the variety and imapct i needed just using a single font 
In the end I used the just the following font. 

- [Titillium Web](https://fonts.google.com/specimen/Titillium+Web) was used throughout site
with variations using,  all capitals, bold effect, heavier font.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the  icons for chevrons or padlocks.

## User Stories

### New Site Users

- As a new site user, I would like to be able register for an account, so that I can my save my order details and order history.
- As a new site user, I would like to be able to view all trips, so that I can purchase.
- As a new site user, I would like to be able to search for trips, so that I can review them and purchase.
- As a new site user, I would like to be able to sort trips by category, rating, price, so that I can review them and purchase.
- As a new site user, I would like to purchase through the site.
- As a new site user, I would like to receive notification by email of registration and purchase.

### Returning Site Users

- As a returning site user, I would like to be able register for an account, so that I can my save my order details and order history.
- As a returning site user, I would like to be able to view all trips, so that I can purchase.
- As a returning site user, I would like to be able to search for trips, so that I can review them and purchase.
- As a returning site user, I would like to be able to sort trips by category, rating, price, so that I can review them and purchase.
- As a returning site user, I would like to purchase securely through the site.
- As a returning site user, I would like to receive notification by email of registration and purchase.

### New Guide Users

- As a new guide user, I would like to be able register for an account, so that I can my save my details.
- As a new guide user, I would like to be able to view all trips.
- As a new guide user, I would like to be able to search for trips.
- As a new guide user, I would like to be able to sort trips by category, rating, price, so that I can review.
- As a new guide, I would like to purchase securely through the site.
- As a new guide, I would like to receive notification by email of registration and purchase.

### Returning Guide Users 

- As a returning guide user, I would like to be able to view all trips.
- As a returning guide user, I would like to be able to search for trips.
- As a returning guide user, I would like to be able to sort trips by category, rating, price, so that I can review.
- As a returning guider, I would like to purchase securely through the site.
- As a returning guide, I would like to receive notification by email of registration and purchase.

### Site Admin

- As a site administrator, I should be able to administer using Django admin site.
- As a site administrator, I should be able to review all trips and amend.
- As a site administrator, I should be able to amend categories.
- As a site administrator, I should be able to manage images for trips.
- As a site administrator, I would like to be able to sort trips by category, rating, price, so that I can review them and purchase.
- As a site administrator, I would like to purchase securely through the site.
- As a site administrator, I would like to receive notification by email of registration and purchase.

## Wireframes


I've used [Microsoft Visio](https://img.shields.io/badge/Microsoft_Visio-blue) to design my site wireframes.

### Mobile Wireframes

<details >
<summary> Click here to see the Mobile Wireframes </summary>

**All trips** 
  - ![screenshot](documentation/img/wireframes/mob-trips.jpg)

**Login** 
  - ![screenshot](documentation/img/wireframes/mob-logon.jpg)

**Register** 
  - ![screenshot](documentation/img/wireframes/mob-reg.jpg)

**Bag**
  - ![screenshot](documentation/img/wireframes/mob-bag.jpg)

</details>

### Tablet Wireframes

<details>

<summary> Click here to see the Desktop Wireframes </summary>

**All trips** 
 - ![screenshot](documentation/img/wireframes/tab-trips.jpg)

**Bag**
 - ![screenshot](documentation/img/wireframes/tab-bag.jpg) 

**Login** 
 - ![screenshot](documentation/img/wireframes/tab-logon.jpg)

**Register** 
 - ![screenshot](documentation/img/wireframes/tab-reg.jpg)

</details>

### Desktop Wireframes

<details>

<summary> Click here to see the Desktop Wireframes </summary>

**All trips** 
 - ![screenshot](documentation/img/wireframes/dsk-trips.jpg)

**Bag**
 - ![screenshot](documentation/img/wireframes/dsk-bag.jpg) 

**Login** 
 - ![screenshot](documentation/img/wireframes/dsk-logon.jpg)

**Register** 
 - ![screenshot](documentation/img/wireframes/dsk-reg.jpg)

</details>




## Features

### Existing Features

**SORTING AND FILTERING OF AVAIABLE TRIPS**

The site provides a functionality from the navbar menu to refine the trips shown by filtering them by category, or sorting them highest to lowest 
for both rating and price.

| Description | Image | 
| --- | --- | 
| The following image shows the find categories function of the site and categries you can seach by |![screenshot](documentation/img/gen/find-by-cats.jpg)| 
| The following image shows the find categories function show as a link on the item itself (eg Rivers - selecting this would show all rivers trips wit he category river)  |![screenshot](documentation/img/gen/search-gray.jpg)| 
| The following image shows the sort capability to either sort by rating or price as driven by the dropdown from the navabar|![screenshot](documentation/img/gen/sort-by.jpg)|


**FULL TRIP SEARCH**

The site provides a functionality from the navbar menu to search all trips recorded and searches the description and venue fields for words in the search criteria.  

| Description | Image | 
| --- | --- | 
| The following image shows the full text search for the veneu and description works, as in this example we search for the word grayling |![screenshot](documentation/img/gen/search-gray.jpg)| 	

**SITE CONTIANER**
The site container was discussed at length in the UX design section explaining the many benefits it brings to the presentation and user experience 
and how it helps in various ways.

| Description | Image | 
| --- | --- | 
| The following image shows the continaer sized for a large screen and as can bee seen the cotainer is sized to consume 75% of screen width|![screenshot](documentation/img/gen/cont1.jpg)|
| The following image shows the continaer sized for a small screen and as can bee seen the cotainer is sized to consume 95% of screen width|![screenshot](documentation/img/gen/cont2.jpg)|

**USER PROFILES**

The profiles page contains all the information for the logged on user and allows them to edit there personal details, (we dont store credit card number for the user) and also provides a complete order history for the user.

| Description | Image | 
| --- | --- | 
| The following image shows profile complete with user detaild and order history |![screenshot](documentation/img/gen/profile.jpg)|	

**MOBILE BAG VIEW**

The main bag view for the site is based on a HTML table and this does not work well as user experience for users on small/mobile screen, as they are constantly scrolling left and right. 
So the view for this has been changed to present a much more pleasing user experience with the total price and Navigation buttons 
placed at the top of the screen next to the total price.
as you scroo, down you can review your order items and there is a button a the bottom of the page to jump to the top, this may seem some waht superflous but if the bag 
3 or more items in it, then scrolling up and down becomes excessive so this button was placed to remove this need.
the images for this can be seen in the testing document.

See [TESTING.md - Section Responsiveness ](TESTING.md) to see the view


**INTERACTIVE ACKNOWLEDGEMENTS**

The site provides a functionality when the user makes an action it provides an acknowldegemnt of this such as
- success or failure on purchase 
- Alert you are editing trips

This confirms or ascerts to the user the user action they have undertaen rather leaving actions unconfirmed. 

| Description | Image | 
| --- | --- | 
| The following image shows the success message delivered by bootstrap toasts |![screenshot](documentation/img/gen/toast-s.jpg)| 
| TThe following image shows the alert message delivered by bootstrap toasts |![screenshot](documentation/img/gen/toast-a.jpg)| 

**STATUS MESSAGE ON EMPTY SEARCH**

When searching the site using the seach capability, i noticed that inthe event that no results were returned from the search the output was not a good user experience e.g. it was was just an empty contianer on screen. I added some Jinja Syntax and message to handle and the results in the all_trips template as shown below.

```html
<!-- the following Html handles the result if there is no results retunred for the search  -->
{% empty %}
	<div class="text-center">
		<h4>No results returned for your Search</h4>
		<a href="{% url 'alltrips' %}" class="shop-now-button-small btn btn-outline-light rounded-1 mt-3">
			<span class="icon"><i class="fas fa-chevron-left"></i></span>
			<span class="text-uppercase">Keep Looking for Trips</span>
		</a>
	</div>
```

![screenshot](documentation/img/gen/empty_srch.jpg)

### Future Features

**ADD FILE WIDGET FOR MORE APPEALING USE** 
I could not get the Django Custom Clearable File Input, even after after working with tutor support. It was beleived to be an issue with versions on the project. for this reason the cuurent widget was not replced. The current widget is rather clunky nad has also intoduced other issues (see testing, section on unresolved bugs), and given the necessary time I would revise this and get it working with something more befitting the site.  

**USER MANAGEMENT FOR “GUIDES”** 

One of the features which was not completed fully was the ability to almost have a second level of super user in the site where guides would be able to perfrom CRUD functions without the need to be a superuser, so hence could not logon to the admin portal but could perfrom the CRUD functions through the pages on there own trips they had created. This feature was mostly completed but and is in a partially comapleted state in the project. 
The feature was envisaged to work in the following where you would have to register for the site and then be placed in the Django group called guide, then on access to features such as product management, you would be checked for membership of this group using a decorator type function and template logic. Then access to Edit and Delete records would be granted using a similar mechanism (eg logged as au ser, and membership of the guide group), and filtering on the user_id for individual records is recorded in trip record on creation.     


## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.

- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.

- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) used as my local IDE for development. using VSCode to work offline when I was preparing README.md and TESTING.md as a for instance. 

- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) used for online secure payments of ecommerce products/services.
- [![Gmail API](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) used for sending emails in my application.
- [![AWS S3](https://img.shields.io/badge/AWS_S3-grey?logo=amazons3&logoColor=569A31)](https://aws.amazon.com/s3) used for online static file storage.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Canva](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) used for creating wireframes.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.
- [![Microsoft Visio](https://img.shields.io/badge/Microsoft_Visio-blue)](https://www.microsoft.com/en-gb/microsoft-365/visio/flowchart-software) Microsoft Visio for creating wireframes and any other diagrams.
- [![Pygraphviz](https://img.shields.io/badge/Pygraphviz-grey)](https://django-extensions.readthedocs.io/en/latest/graph_models.html)
Django App extension to generte ERD diagram for current the project.
- [![Squoosh](https://img.shields.io/badge/Squoosh-grey)](https://squoosh.app/) Squooosh was used to convert the images from jpg to Avif, Also to resize (reduce pixel count) the images to a more manageable size to improve download speed.
- [![GoogleFonts](https://img.shields.io/badge/GoogleFonts-grey?logo=googlefonts&logoColor=EA4335)](https://squoosh.app/) Google Fonts Google fonts was used to source the fonts that were selected from Fontjoy.
- [![FontJoy](https://img.shields.io/badge/FontJoy-grey)](https://fontjoy.com/)
FontJoy Font joy was used in the design process to create a palette of fonts, to be empathic with the site topic, and provide contrast between various type styling.
	- Quote from https://fontjoy.com/
	The goal of font pairing is to select fonts that share an overarching theme yet have a pleasing contrast. Which fonts work together is largely a matter of intuition, but we approach this problem with a neural net.

 - [![Temp-mail](https://img.shields.io/badge/Temp-mail-grey)](https://temp-mail.org/en/) Temp mail was used for testing of the registration and authentication process for users for the site 
 - [![Temp-mail](https://img.shields.io/badge/coolors.co-grey) ](https://coolors.co/) Used as a colour palette selection tool 

## Database Design

### Database models  

The following diagram depicts the main databases are envisioned a the design stage of project for Guide fly fishing site 
This further developed in the ERD diagram shown below for the project as genereted by `pygraphviz`                    
![User DB Model](documentation/img/erd/erd-1.png) 

The below diagram is the ERD for the complelted project
I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
	- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
	- then type `Y` to proceed
	- then: `pip3 install django-extensions pygraphviz`
	- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- Back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- Drag the new `erd.png` file into my `documentation/` folder
- Remove the `'django_extensions',` from my `INSTALLED_APPS` in settings.py
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![erd](documentation/img/erd/erd.png)
source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

I have also used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
	UserProfile {
		int id
		int user
		string default_phone_number
		string default_street_address1
		string default_street_address2
		string default_town_or_city
		string default_county
		string default_postcode
		string default_country
	}
	UserProfile ||--o{ Order : has
	Order {
		int id
		string order_number
		int user_profile
		string full_name
		string email
		string phone_number
		string country
		string postcode
		string town_or_city
		string street_address1
		string street_address2
		string county
		datetime date
		decimal delivery_cost
		decimal order_total
		decimal grand_total
		text original_bag
		string stripe_pid
	}
	Order ||--o{ OrderLineItem : contains
	OrderLineItem {
		int id
		int order
		int product
		int quantity
		decimal lineitem_total
	}
	OrderLineItem }o--|| trips : references
	trips {
		int id
		string rec_owner
		int categories
		string venue
		text description
		decimal day
		decimal spaces
		decimal cost
		date dates
		string location
		string locale
		decimal rating
		string image_url
		string image
	}
	trips }o--|| categories : belongs_to
	categories {
		int id
		string name
		string friendly_name
	}
	User ||--|| UserProfile : owns
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqNVU2PmzAQ_SvI52S1hITsct5LpUqtVPVSRUJeeyBWjU39sd004b93AqRrAiHlkMC8-XxvMEfCNAeSETAvgpaGVjsV4fXdgvlqdCEkRMfOdL6EcpHgw2ePrh8W64xQZcShoF66vN5rBbny1euMEz4CuJxybsDa-D_9Vjf9nP6tcm1yJtzhphPTXs3AtbbuTM18vOkTNGPWTqflUh-jL4aDibJoT23n0xlmOO3r6LPfiLkL4XndlRmFFV7KXNFqjEBFhRxZZwUazBgG3SJnlvl7Mt-T91oxTh04UUF7E5iBiYpK_JfiDcwBlbJuDHf8Ou2oHIP4Iih-DTp4dxgmSqGozF9pOTWBqCGvL3I2oeThQnwWCj45qHAxmFaOChVuxz_0zpvXjjA04Vpwz9zQ-MtT5QaKXOaUWElgpXDUZqqTRi-Xp1N0ns9i0wYKMKAY9G139vtLbYDluCLXXTMUsERmL-mCiDdQHq404GAZFnRCqwnZ6cSctqYsTH6xX60GttH-jNuQGnsc1AsAObF9Bt3VeEMQKyH3Rk4jAwU6UnvmPyhC-l9BalVaVK3zDMD7GkweDgUGKy4PwdERnGnt7mIT4fmWRSgkEkUWpAKDZwvHr0hbfUfcHjALyfCWU_NzR3aqQT_qnf52UIxkznhYEF-fye6_OyQrqLRoraki2ZG8k2yVbh_SNNnE68d0naTb7YIcSLZM44c4STfb5zhGaLVuFuSP1pgA7atk85Q8r57QIXlcb9tsP1qwK2m0L_d9qeYvUXAz4Q)



## Testing
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://p4guideflyfishing-879a54f37efc.herokuapp.com).

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Signed-in to the CI LMS using my email address.
- An email was sent to me with my new Postgres Database.

> [!CAUTION]  
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method
> if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
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

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-project-guideflyfishing` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: `policy-project-guideflyfishing` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for project-guideflyfishing static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-project-guideflyfishing".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-project-guideflyfishing") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-project-guideflyfishing` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-project-guideflyfishing`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://p4guideflyfishing-879a54f37efc.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or Project-guideFlyFishing
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | user's own value |
| `AWS_SECRET_ACCESS_KEY` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |
| `USE_AWS` | True |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.19`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Coelecanth/Project-guideFlyFishing) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/Coelecanth/Project-guideFlyFishing.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Coelecanth/Project-guideFlyFishing)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Coelecanth/Project-guideFlyFishing)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment


## Credits

### Content

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | entire site responsive HTML/CSS/JS |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

All of the images in this site that were used in the adverts were provided by myself and I own all copyright of these images 
The only exception to this is the background image used in the site which was sourced from Pexels.com, is a commercial image and is accredited to Mathew Monton on Pexels  

### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Font Awesome](https://www.pexels.com) | Icons in buttons etc across entire site | image | Alo favicon on all pages |
| [Pexels.com](https://www.pexels.com/photo/body-of-water-and-green-field-under-blue-sky-photo-1179225/)  | background for entire site  | image | River image for the site |
| [Mathew Montron](https://www.pexels.com/photo/body-of-water-and-green-field-under-blue-sky-photo-1179225/)  | background for entire  | image | Mathew Montron author of the above image |
| [Lorem Picsum](https://picsum.photos) | trips pages | images |  Used for initial testing in trips for image content  |
| [Lorem Ipsum](https://loremipsum.io/) | trips pages | text | Used for initial testing in trips for text content |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging project issues.
	In particualr I would like to thank Sarah from the tutor team,  for her invaluable contribution to my understanding and better diagnosis of code errors and this project. 
- I would like to thank my tutor Ben Smith at Bristol college for his help and advice. 
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for showing "I'm not the only one", and persisting. 
- Thanks to my family for putting up with "Mr. Grumpy" and the many hours I spent working on this and other projects 
