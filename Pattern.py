**Five real-world example of abserver pattern**
(will be used "Update" function)
"""
    -(1)Messenger Group
        Whenever any person sends any message in the group_chat, all the people who are in the group get notified and accepted these message.
        In this case,observer pattern will be used.
    -(2)Electronic Store
        When new electronic devices were arrived,it(the program used observevr pattern) will be sent about this noti and updating to all their customer.
    -(3)Newspaper boy
        The boy will shot the newspaper to all house having along his path.
    -(4)Facebook following
        When we follow the celebrity,updating photo,posting status,uploading photo etc about him will be known.
        This is because of abserver pattern.
    -(5)Website subscriber
        When we subscibe the one website,we will get the noti  and updated  news from this website cause of using abserver pattern in website.

"""
**Five real_world example of prototype pattern
(will be used "clone function")
"""
    -(1)Math 
        When we want to draw circle,triangle or square etc,we must first to build shape(gettype(),getid(),sellid(),clone()).
        Then we can build circle,triangle or square from this shape clone.
    -(2)A possible real world application must be, when we need to create a spreadsheet containing many cells. Rather than set the style for each newly created cell to override the default stylings, 
    we'd use a Prototype pattern to create a template cell, and clone that cell when creating new cells.
    -(3)Build airplane company
        When we want to code that the building airplane program.
        This will be many type(Biplane,Wide passenger plane,Business jet,Military Drone etc.)
        For this problem,we will not build each class for each type,we must first build the class include the main feature and then coping this and build for each class of the types ny clone funciton.
    -(4)Car company
        First the design the new car and then, clone the class function of this car and manufacture the large amount.
    -(5)Medician company
        First experiment the drug (for example,headache),then produce this drug by cloning it and testing for another drug by experiment it. 

"""


**Five real_world example of builder pattern
"""
    -(1)House building
        When we want to build house with full luxuriated features such as with garage,swimming pool,statues,garden etc.
        Then we must first build the simple house class consisting windows,doors etc.
        And then filling the facilites features by using builder pattern.
    -(2)Luxury Car building
        First must build simple car,and then adding the luxury accessories to this car by the nature of builder function.
    -(3)Game hero
        When we want to decorate our game hero in mobile legends,we must set the hero with set-item.
        This is about builder pattern.
    -(4)Building Hotel
        Must be build hotet without full_facilated,then added item such as coffee bar,skyview,simming pool,cat parking etc. by the using of builder pattern.
    -(5)Limited watch
        Adding each facilated features to simple watch.This is also by term of builder pattern.
"""
