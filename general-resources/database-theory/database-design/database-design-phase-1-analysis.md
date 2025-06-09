
# Database Design Phase 1: Analysis

This article follows on from [Database Lifecycle](database-lifecycle.md).


Your existing system can no longer cope. It's time to move on. Perhaps the existing paper system is generating too many errors, or the old Perl script based on flat files can no longer handle the load. Or perhaps an existing news database is struggling under its own popularity and needs an upgrade. This is the stage where the existing system is reviewed.


Depending on the size of the project, the designer may be an individual, responsible for the database implementation and coding, or may be a whole team of analysts. For now, the term *designer* will represent all these possibilities.


The following are the steps in the Analysis Phase.


1. Analyze the organization
1. Define any problems, possibilities or constraints
1. Define the objectives
1. Agree on the scope


When reviewing a system, the designer needs to look at the bigger picture - not just the hardware or existing table structures, but the whole situation of the organization calling for the redesign. For example, a large bank with centralized management would have a different structure and a different way of operating from a decentralized media organization, where anyone can post news onto a website. This may seem trivial, but understanding the organization you're building the database for is vital to designing a good database for it. The same demands in the bank and media organizations should lead to different designs because the organizations are different. In other words, a solution that was constructed for the bank cannot be unthinkingly implemented for the media organization, even when the situation seems similar. A culture of central control at the bank may mean that news posted on the bank website has to be moderated and authorized by central management, or may require the designer to keep detailed audit trails of who modified what and when. On the flip-side, the media organization may be more laissez-faire and will be happy with news being modified by any authorized editor.


Understanding an organization's culture helps the designers ask the right questions. The bank may not ask for an audit trail, it may simply expect it; and when the time comes to roll out the implementation, the audit trail would need to be patched on, requiring more time and resources.


Once you understand the organization structure, you can question the users of any existing system as to what their problems and needs are, as well as what constraints will exist then. You need to question different role players, as each can add new understanding as to what the database may need. For example, the media organization's marketing department may need detailed statistics about the times of day certain articles are read. You may also be alerted to possible future requirements. Perhaps the editorial department is planning to expand the website, which will give them the staff to cross-link web articles. Keeping this future requirement in mind could make it easier to add the cross-linking feature when the time comes.


Constraints can include hardware ("We have to use our existing database server") or people ("We only have one data capturer on shift at any one time"). Constraints also refer to the limitations on values. For example, a student's grade in a university database may not be able to go beyond 100 percent, or the three categories of seats in a theatre database are small, medium and large.


It is rarely sufficient to rely on one level of management, or an individual, to supply objectives and current problems, except in the smallest of organizations. Top management may be paying for the database design, but lower levels will need to use it, and their input is probably even more important for a successful design.


Of course, although anything is possible given infinite time and money, this is (usually) never forthcoming. Determining scope, and formalizing it, is an important part of the project. If the budget is for one month's work but the ideal solution requires three, the designer must make clear these constraints and agree with the project owners on which facets are not going to be implemented.


CC BY-SA / Gnu FDL


{% @marketo/form formId="4316" %}
