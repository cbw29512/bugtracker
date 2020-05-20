# bugtracker
Author:Chris Wilson
Assisted: Koren and Sean
It's important to focus on more things that Django is good at... that may not be immediately obvious as projects that make good websites. When working on any project of reasonable size, bug reports and feature requests are going to come in faster than you can work on them (or keep them in your head). Eventually you'll start forgetting them unless you have a place to write them down... and why not make that a little more full-featured while you go?

Your Task
Write a bug tracker application that:

requires logging in, but people who aren't logged in cannot create accounts (don't want any random person to see bugs in your application!)
use a custom user model to replace the built-in one (you may want to reference 👨‍🔬 Under the Microscope: Custom Users)
has a homepage that shows all tickets, arranged in separate columns according to current ticket status (i.e. New, In Progress, Done, Invalid)
allows filing/creating tickets
has a ticket detail page
allows assigning a ticket to the currently logged in user
allows marking a ticket as invalid
allows marking a ticket as complete
allows editing tickets (we will limit this to Title and Description, do not include other any of the other fields)
has a user detail page where you can see:
the current tickets assigned to a user
which tickets that user has filed
which tickets that user completed
Each ticket should have the following fields:

Title
Time / Date filed
Description
Name of user who filed ticket
Status of ticket (New / In Progress / Done / Invalid) --> hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices (Links to an external site.)Links to an external site.
Name of user assigned to ticket
Name of user who completed the ticket
When a ticket is filed/created, it should have the following settings:

Status: New
User Assigned: None
User who Completed: None
User who filed: Person who's logged in
When a ticket is assigned, these change as follows:

Status: In Progress
User Assigned: person the ticket now belongs to
User who Completed: None
When a ticket is Done, these change as follows:

Status: Done
User Assigned: None
User who Completed: person who the ticket used to belong to
When a ticket is marked as Invalid, these change as follows:

Status: Invalid
User Assigned: None
User who Completed: None
Hint: when you're modifying models, you don't have to serve them in order to modify them; you can modify the fields that you need and save it back with no issues. For example:

article = NewsItem.objects.get(id=1)
article.title = "What's up, Doc?"
article.save()