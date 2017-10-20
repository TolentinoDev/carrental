db.define_table('inventory',
                   Field('make', label="make"),
                   Field('model',label="model"),
                   Field('caryear',label="caryear"),
                   Field('pic','upload'),
                   Field('priceperday',label="priceperday"),
                   Field('discription', 'text', label="discription"))