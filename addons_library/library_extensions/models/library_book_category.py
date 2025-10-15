from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'
    _rec_name = "category"

    category = fields.Char(
        string='Category Name',
        required=True,
        unique=True
    )
    ############################
    # Constrains and onchanges #
    ############################
    _sql_constraints = [
        ('unique_category_name', 'unique(category)', 'Category name must be unique!')
    ]
