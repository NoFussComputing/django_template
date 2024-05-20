---
title: Device
description: No Fuss Computings Django Template ITAM Device
date: 2024-05-15
template: project.html
about: https://gitlab.com/nofusscomputing/infrastructure/configuration-management/django_app
---

This component within ITAM is intended to display information about a device, be it a computer, router or switch etc.


## Features

For each device within your inventory, the following fields/tabs are available to track items:

- Name

- Operating System

- Software

- Configuration

- Inventory


### Operating System

This tab shows the operating system selected as installed on the device. the version `name` is intended to be full [semver](https://semver.org/).


### Software

- Configuration key `software`

- Format `list of dict`

- Ansible Module `ansible.builtin.apt`

This tab displays both software actions and installed software. Software install details are added/updated by uploading an [inventory report](../api.md#inventory-endpoint).

You can specify a software action for any piece of software within the ITAM database. You can do this by pressing the `dd software action` button or if the software is installed clicking on the `+ Add` button on the row of the software to add the action to. An action can be set to either `Install` or `Remove` and you can also select a software version from the database if you choose to do so. Software actions are added to config management and can be pulled from the API for use within an Ansible playbook.

Display of both installed software and software actions is within a single row, if it's for the same software. Any software that you add an action to, will be displayed at the top of the list of software tab.

!!! info
    If you add a software action for software that is already installed using the `add software action` button, an additional row will not be added as the applications logic is smart enough to check if the software is already installed.


### Configuration

Although, configuration is generally part of config management. This tab displays in `JSON` format configuration that is ready for use. The intended audience is Ansible users with the fields provided matching established Ansible modules, if they exist.

This configuration can also be obtained from API endpoint `/api/config/<machine-slug>` where `<machine-slug>` would match the Ansible `inventory_hostname`.


### Inventory

It's possible for a machine to be inventoried and have the report passed to the [inventory endpoint](../api.md#inventory-endpoint). This report will update the device within the interface and provides the option to use scheduled inventory gathering to keep the device up to date.

The report can contain the following information:

- device:

    - `name` Device name

    - `serial number` Device serial number

    - `GUID/UUID` Device GUID/UUID

- operating System

    - `name` Operating system name

    - `version major` Operating system Major version number

    - `installed version` Full [semver](https://semver.org/) of the installed operating system

- software

    - `name` Software Name

    - `category` Software Category

    - `version` Software version

        !!! info
            When the software is added to the inventory, a regex search is done to return the [semver](https://semver.org/) of the software. if no semver is found, the version number provided is used.
