---
title: "Intoducing Custom Security Attributes in Entra"
date: 2026-11-07T00:00:00Z
published: false
---
Intoducing Custom Security Attributes in Entra
----------------------------------------------
At the time of writing it's only 6 weeks till Christmas, and all the children are asking Santa for the ability to save business attributes to their Entra Objects. You can tell them from me that letter to santa is wasted, because thanks to the magic of Custom Security Attributes you can not only assign that data to your Entra Objects already, but you can also enforce fine grained control over access. A bona fide Christmas cracker!

So what are Custom Security Attributes anyway?
---------------------------------------------
Custom security attributes are key value pairs that can be assigned to Entra ID's such as users.  For example, if you want to record data such an employee's hourly rate, you can create an attribute for that, assign it to the user, and apply a value.

INSERT EXAMPLE

A better use though may be to record which project someone is working on, but what if they are working on several projects at the same time?  No problem, when creating your security attributes, you have the option to allow single or multiple values to be assigned, unless you create it as a boolean, because then you won't know if you're coming or going.


Pre-Requisites
--------------
Before you can create and manage attribute sets, you will need the Attribute Definition Administrator or Attribute Assignment Administrator roles.  These can be assigned through Entra -> Manage-> Roles and Administrators section.  There is a bit of a gotcha where you have to click the role name, and not the juicy tick box competing for your attention.

STATIC IMAGE OF ROLE LIST

Get past that and you will be on the Attribute Definition Administrator or Attribute Assignment Administrator role screen where you can search for a user and assign the role.

STATIC IMAGE OF USER SEARCH

With the correct role assigned, you can create 

Creating Attribute Sets
-----------------------
Before you can start creating and using Custom Security Attributes, you need to create an Attribute Set, a bit like a resource group, but specifically for Custom Security Attributes.  This is done from Entra -> Manage -> Custom Security Attributes

STATIC IMAGE OF NEW ATTRIBUTE SET

Managing Attribute Sets
-----------------------
Following the creation of the 1st Attribute set, returning to Entra -> Manage -> Custom Security Attributes


How is this different from tags?
--------------------------------




