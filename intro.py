'''
    We will be using:
    - DRF
    - REQUESTS
    - Django cors headers
'''
"""
    Day Whatever
    -Mixins and GenericView: using class based views
    -- I learnt how classed based API views worked and how functions can be written off the inherited class
    Day Next whatever
    - Sessions Authentication
    --Permission_class and authentication_class: mostly used for django projects and not an API Service
    DAY 3
    - User and Group Permissions with DjangoModelPermissions
    DAY 4
    - Custom Permissions:
        some custom permissions will not suffice for our python client: e.g permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] 
    DAY 5
    - Token Authentication:
        to allow our client interact with the backend
        we want to be able to create the tokens at anytime and also delete them at any point
        we must consider deleting the tokens also
        tokens can be used and deleted after a matter of time
        celery can be used to clear tokens out each time, we can enforce and allow users to pick their authentication
    DAY 6
    - Default django rest framework settings
    - we can allow read-only for unauthenticated uses
    - we can declare default settings for rest framework in settings.py
    - if in our views.py, the permission class is left empty. It means there are no permissions on that class
    based view, even when a default permissions or authentications namespace is put in the settings

    - THROTTLING
        - can be used to limit the amount of users on
        - it is advisable to use nginx for more advanced throttling features

    DAY 7
        - USING MIXINS FOR PERMISSIONS
        - instead of clogging up our views with multiple permission_classes
        - we can use mixins for query sets and for serializers also
        - it is also risky
    DAY 8
    - Viewsets and Routers
        -viewsets are typically in views.py
        -routers are also typically in the urls.py
        -the routers allow for a different series of api views
        -there is really no good way to see our url endpoints while using routers
        - we can have class based views in viewsets
        - not so recommended, we might want to stick to manually tuned api views instead
    DAY 9
    - URLs, Reverse, & Serializers
        THE WRONG WAY XXX
            -we can add a url to our serializers: serializers.py and add a get_url to pint to the detailed view endpoint
            -this method is flawed because we can not use the v2 url with it
        THE RIGHT WAY 1
            -we can do this using reverse and configuring the endpoint
            * Note: in the serializers.py, if a serializer variable is url, the function name must be " get_<field_name> "
        THE RIGHT WAY 2
            -using serializers.hyperlinkedidentityfield, which only works for Modelserializers
        - in some case, we might not want the urls to show up, we might need to create a new serializer
    DAY 10
    -   Model Serializer Create & Update Methods
        - to create an email instance whenever we create a product: the email will not be in the models initially (it will be a write only parameter)
        - Because of the email field, It will not create a new object (You may need to make the field read-only, or override the ProductSerializer.create() method to handle this correctly.)
        - we can manually edit the create method and remove the email from the validated_data
        - we can write the create method in the views and the models also
    DAY 11
    - Custom Validators
        - we can write custom validators in our serializers.py and use it to check data before saving it
        - we  can also have various filters on any product (iexact)
        - we can import the validators from a custom module (validators.py) and use it in a model field of choice in the serializers.py
        
    """
