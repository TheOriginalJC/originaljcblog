---
title: "ABAC with custom security attributes"
date: 2026-06-02T00:00:00Z
published: false
---
ABAC With Custom Security Attributes
------------
Intro

If you've worked with Azure admin for any length of time, you're probably familiar with Entra's Security Groups for configuring Role Based Access Control (RBAC).  If you're just getting started, you might have run into it already.

They have the advantage of being pretty intuitive, making them a great start to managing access to Azure resources, particularly with a smaller company.

As your Azure estate grows, the limitations of groups start to become clear.  At scale they become difficult to manage and you may start to think "surely there is a better way?"

Enter Custom Security Attributes

The answer is "yes" (maybe?). By using Custom Security Attributes and Attribute Based Access Control (ABAC).

Custom Security Attributes allow you to define key-value pairs which can then be assigned to Entra ID Objects (users, service principals, managed ID's).  For example, a new project named "cosmic" kicks off, with a team consisiting of "Jonah", "Alice" and "Marcus".

If we were using groups we might create a new group for the team, maybe even multiple groups for higher level access, assign Jonah, Alice and Marcus to the relevant groups, and configure RBAC so each group has the required access level.

What are custom security attributes?

Why do they exist when we already have groups (And how are they different?)


Use case examples
1.
2.
3.
4.

Requirements
Azure P1 or greater


When to use groups

When to use CSA

Understanding ABAC

ABAC vs RBAC


Hands on lab

Common mistakes

Recommended design approach
