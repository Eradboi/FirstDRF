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

"""
