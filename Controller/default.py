def index():
    response.menu = []
    return dict()
def welcome():
    response.menu = []
    return dict()

def subject():
    response.menu = []
    return dict()

def alphabetically():
    response.menu = []
    return dict()

def keywords():
    response.menu = []
    return dict()

def libdbs():
    grids = []
    messages = []
    messages.append('Grid')
    invGrid = SQLFORM.grid(db.inventory, fields=(db.inventory.make,db.inventory.model,db.inventory.caryear,db.inventory.pic,db.inventory.priceperday,db.inventory.discription), create=False,editable=False,deletable=False,paginate=20,searchable=True, maxtextlength=1000, exportclasses=dict(tsv=False, xml=False, html=False, json=False, tsv_with_hidden_cols=False, csv_with_hidden_cols=False), details=True,csv=False,buttons_placement = 'right',)
    grids.append(invGrid)
    return dict(grid=invGrid, messages=messages)

@auth.requires_membership('Library-Admins')
def admin():
    response.menu = []
    inv = []
    invStr = ",".join(inv)
    invID = db.inventory.insert(make=request.vars.make,model=request.vars.model,year=request.vars.year,pic=request.vars.pic, priceperday=request.vars.priceperday,discription=request.vars.discription)
    return dict()


@auth.requires_membership('Library-Admins')
def adminlibdbs():
    grids = []
    messages = []
    messages.append('Grid')
    invGrid = SQLFORM.grid(db.inventory, fields=(db.inventory.make,db.inventory.model,db.inventory.caryear,db.inventory.pic,db.inventory.priceperday,db.inventory.discription), create=False,editable=True,deletable=True,paginate=20,searchable=True, maxtextlength=1000, exportclasses=dict(tsv=False, xml=False, html=False, json=False, tsv_with_hidden_cols=False, csv_with_hidden_cols=False), details=False,csv=False)
    grids.append(invGrid)
    return dict(grid=invGrid, messages=messages)



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
