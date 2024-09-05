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




"""
