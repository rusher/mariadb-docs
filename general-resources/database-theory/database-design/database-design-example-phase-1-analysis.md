
# Database Design Example Phase 1: Analysis

This article follows on from [Database Design Phase 6: Maintenance](database-design-phase-6-maintenance.md).


## Real-world example: creating a publishing tracking system


Now let's walk through the database design process with a step-by-step example. The Poet's Circle is a publisher that publishes poetry and poetry anthologies. It is keen to develop a new system that tracks poets, poems, anthologies and sales. The following sections show the steps taken from the initial analysis to the final, working database.


### Poet's circle database phase 1: analysis


The following information is gleaned from speaking to the various stakeholders at Poet's Circle. They want to develop a database system to track the poets they have recorded, the poems they write, the publications they appear in, as well as the sales to customers that these publications make.


The designer asks various questions to get more detailed information, such as "What is a poet, as far as the system goes? Does Poet's Circle keep track of poets even if they haven't written or published poems? Are publications recorded even before there are any associated poems? Does a publication consist of one poem, or many? Are potential customer's details recorded?" The following summarizes the responses in our example:


* Poet's Circle is a publisher that bases its choices of publications on an active poetry community on its website. If enough of the community wants a poem published, Poet's Circle will do so.
* A poet can be anybody who wants to be a poet, not necessarily someone who has a poem captured in the system or someone who has even written a poem.
* Poems can be submitted through a web interface, by email or on paper.
* All captured poems are written by an associated poet, whose details are already in the system. There can be no poems submitted and stored without a full set of details of the poet.
* A publication can be a single poem, a poetry anthology, or a work of literary criticism.
* Customers can sign up through a web interface and may order publications at that point in time, or express interest in receiving updates for possible later purchases.
* Sales of publications are made to customers whose details are stored in the system. There are no anonymous sales.
* A single sale can be for one publication, but many publications can also be purchased at the same time. If more than one customer is involved in this sale, Poet's Circle treats it as more than one sale. Each customer has their own sale.
* Not all publications make sales — some may be special editions, and others simply never sell any copies.


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
