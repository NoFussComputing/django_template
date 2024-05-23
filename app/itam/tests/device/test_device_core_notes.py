
from django.test import TestCase, Client

import pytest
import unittest
import requests



@pytest.mark.skip(reason="to be written")
def test_note_device_no_blank_note():
    """ The field is set to blank=true, ensure that a blank note cant be saved
    
        field had to be set blank=true so that other forms on same page could be saved.
    """
    pass


@pytest.mark.skip(reason="to be written")
def test_note_new_correct_device():
    """ On creation of device note the device must be added """
    pass


@pytest.mark.skip(reason="to be written")
def test_note_auth_view_device():
    """ Ensure that if the user doesn't have view permissions for notes, they can't see any notes
    
    user must also have view permissions for the opject the note is for
    """
    pass


@pytest.mark.skip(reason="to be written")
def test_note_auth_add_device():
    """ Ensure that if the user doesn't have add permissions for notes, they can't add any notes
    
    user must also have view permissions for the opject the note is for
    """
    pass


@pytest.mark.skip(reason="to be written")
def test_note_auth_edit_device():
    """ Ensure that if the user doesn't have edit permissions for notes, they can't edit any notes
    
    user must also have view permissions for the opject the note is for
    """
    pass


@pytest.mark.skip(reason="to be written")
def test_note_auth_delete_device():
    """ Ensure that if the user doesn't have delete permissions for notes, they can't delete any notes
    
    user must also have view permissions for the opject the note is for
    """
    pass
