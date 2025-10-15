# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.book"
    _description = "Book"
    _order = "title"
    _rec_name = "title"

    ###################
    # Default methods #
    ###################
    title = fields.Char(string="Book Title",
                       required=True)
    isbn_13 = fields.Char(string="ISBN 13",
                          required=True)

    ######################
    # Fields declaration #
    ######################

    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################
    _sql_constraints = [
        ('unique_isbn_13', 'unique(isbn_13)', 'The ISBN-13 must be unique!'),
    ]
    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
