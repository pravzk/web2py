# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    user credentials
    """
    session.userID=None
    return dict()
    
def signup():
    return dict()

def home():
    	"""
	home page of user
    	"""
        session.friendID=None
    	if not session.userID:
    		session.userID=request.vars.txtUserID  
    		user=db(db.User.userID==session.userID).select().first()  
        	if  user:
       	    		user_details=db(db.Login.userID==session.userID).select().first()
            		if request.vars.txtPassword!=user_details.password:
	        		session.ral = "Please enter a valid password"
        			redirect('index')
        	else:
           		session.ral = "Please enter a valid userID and password"
           		redirect('index')       	
    	else:
    		user=db(db.User.userID==session.userID).select().first()
    		user_details=db(db.Login.userID==session.userID).select().first()
	li=[session.userID]
	form=[]
	posta=[]
	comments=[]
	j=0
	for f in db(db.Friends.friend==session.userID).select(db.Friends.ALL) or db(db.Friends.userID==session.userID).select(db.Friends.ALL):

		if f.addRequestStatus == str(1):

			if f.userID==session.userID:
				li.append(f.friend)
			else:
				li.append(f.userID)
	posts=db().select(db.Post.ALL,orderby=~db.Post.postedOn)
	for post in posts:
	 	if post.userID in li:		 	
	 		posta.append(post)		 	
		 	comments.append(db(db.Comment.postID==post.id).select(db.Comment.ALL,orderby=db.Comment.commentedOn))
		 	form.append(FORM(TABLE(TR(TD(INPUT(_type='hidden',_name='hdnID',_value=post.id),TEXTAREA(_rows='1',_cols='31',_name='txtComment'))),TR(TD(INPUT(_type='submit',_value='comment'))))))		 	
		 	if form[j].accepts(request.vars,session):
		 	    	if form[j].vars.txtComment:
		 			id=db.Comment.insert(postID=form[j].vars.hdnID,commentedBy=session.userID,commentBody=form[j].vars.txtComment)
		 		redirect(URL(r=request,f='home'))
		 	j=j+1		 	
	return dict(posta=posta,u=user_details,comments=comments,form=form) 
    
def post():
	if request.vars.txtPost:
		id=db.Post.insert(userID=session.userID,postBody=request.vars.txtPost)
	redirect(URL('home'))
	
def uploadPhotoVideo():
	user=db(db.User.userID==session.userID).select().first()
    	user_details=db(db.Login.userID==session.userID).select().first()
    	form=FORM(TABLE(TR(TD()),TR(TD(LABEL("  Upload picture/video"))),TR(TD(INPUT(_type='file',_name='photoVideo'))),TR(TD(TEXTAREA(_rows='1',_cols='60',_name='txtDesc'))),TR(TD(INPUT(_type='submit',_value='upload')))))
        if form.accepts(request.vars,session):
		if hasattr(form.vars.photoVideo, "file"):
			id=db.Post.insert(userID=session.userID,postBody=form.vars.txtDesc,photoVideo=form.vars.photoVideo)
		   	session.ral="Image Uploaded"
           		redirect(URL(r=request,f='home'))
           	else:
           		redirect(URL('uploadPhotoVideo'))
    	return dict(form=form,u=user_details)
   
def changeImage():
	user=db(db.User.userID==session.userID).select().first()
    	user_details=db(db.Login.userID==session.userID).select().first()
    	form=FORM(TABLE(TR(TD()),TR(TD(LABEL("Change profile picture"))),TR(TD(INPUT(_type='file',_name='image'))),TR(TD(INPUT(_type='submit',_value='change')))))
        if form.accepts(request.vars,session):
        	id=db(db.User.userID==session.userID).select().first().update_record(image=form.vars.image)
           	redirect(URL(r=request,f='home'))
    	return dict(form=form,u=user_details)
    	
def sendMessage():
	"""
		sendMessages
	"""
	user=db(db.User.userID==session.userID).select().first()
    	user_details=db(db.Login.userID==session.userID).select().first()
    	form=FORM(TABLE(TR(TD()),TR(TD(LABEL(" Send Message"))),TR(TD(INPUT(_type='text',_name='txtMto',_placeholder='To'))),TR(TD(TEXTAREA(_rows='5',_cols='60',_name='messageBody',_placeholder='Your Message'))),TR(TD(INPUT(_type='file',_name='Attachments'))),TR(TD(INPUT(_type='submit',_value='upload')))))
        if form.accepts(request.vars,session):
        	if (form.vars.txtMto and form.vars.messageBody):
        		um=db(db.User.userID==form.vars.txtMto).select().first()
        		if um:
				id=db.Message.insert(mTo=form.vars.txtMto,mFrom=session.userID,body=form.vars.messageBody,readStatus=0,file=form.vars.Attachments)
		   		session.ral="Message sent successfully"
           			redirect(URL(r=request,f='home'))
           		else:
           			session.ral="Enter valid recipient"
           			redirect(URL('sendMessage'))
           	else:
           		redirect(URL('sendMessage'))
    	return dict(form=form,u=user_details)


def inbox():
	messages=db(db.Message.mTo==session.userID).select(db.Message.ALL,orderby=~db.Message.messageSentOn)
	return dict(messages=messages)

def outbox():
	messages=db(db.Message.mFrom==session.userID).select(db.Message.ALL,orderby=~db.Message.messageSentOn)
	return dict(messages=messages)

def inboxDisplay():
	return dict(message=request.args[0])

def outboxDisplay():
	return dict(message=request.args[0])


def createAlbum():
	user=db(db.User.userID==session.userID).select().first()
    	user_details=db(db.Login.userID==session.userID).select().first()
    	forma=FORM(TABLE(TR(TD()),TR(TD(LABEL("  Add picture"))),TR(TD(INPUT(_type='file',_name='image'))),TR(TD(TEXTAREA(_rows='1',_cols='60',_name='txtDesc'))),TR(TD(INPUT(_type='submit',_value='add')))))
        if forma.process(formname='form_one').accepted:
			if hasattr(forma.vars.image, "file"):
				id=db.Album.insert(userID=session.userID,photoBody=forma.vars.txtDesc,photo=forma.vars.image)
			   	session.ral="Image Added"
		   	redirect(URL(r=request,f='createAlbum'))
	form=[]
	posta=[]
	comments=[]
	j=0
	posts=db(db.Album.userID==session.userID).select(db.Album.ALL,orderby=~db.Album.photoOn)
	for post in posts: 	
		name="form"
		name=name+str(j)
 		posta.append(post)		 	
	 	comments.append(db(db.AlbumComment.photoID==post.id).select(db.AlbumComment.ALL,orderby=db.AlbumComment.commentedOn))
	 	form.append(FORM(TABLE(TR(TD(INPUT(_type='hidden',_name='hdnID',_value=post.id),TEXTAREA(_rows='1',_cols='31',_name='txtComment'))),TR(TD(INPUT(_type='submit',_value='comment'))))))		 	
	 	if form[j].process(formname=name).accepted:
	 		if form[j].vars.txtComment:
	 			id=db.AlbumComment.insert(photoID=form[j].vars.hdnID,commentedBy=session.userID,commentBody=form[j].vars.txtComment)
	 		redirect(URL(r=request,f='createAlbum'))
	 	j=j+1		 	
	return dict(posta=posta,u=user_details,comments=comments,form=form,forma=forma) 

def searchFriends():
	validuser=db(db.User.userID==request.vars.txtSearch).select().first()
	if (validuser) and (validuser.userID != session.userID):
		session.friendID=request.vars.txtSearch
		redirect(URL('viewFriends'))
	else:
		session.old_url = request.env.http_referer
		redirect(session.old_url)

def searchFriendsByreq():
	session.friendID=request.args[0]
	redirect(URL('viewFriends'))

def viewFriends():
	fd=db(db.User.userID==session.friendID).select(db.User.ALL)
	return dict(fd=fd)

def viewFriendAlbum():
	form=[]
	posta=[]
	comments=[]
	j=0
	posts=db(db.Album.userID==session.friendID).select(db.Album.ALL,orderby=~db.Album.photoOn)
	for post in posts: 	
		name="form"
		name=name+str(j)
 		posta.append(post)		 	
	 	comments.append(db(db.AlbumComment.photoID==post.id).select(db.AlbumComment.ALL,orderby=db.AlbumComment.commentedOn))
	 	form.append(FORM(TABLE(TR(TD(INPUT(_type='hidden',_name='hdnID',_value=post.id),TEXTAREA(_rows='1',_cols='31',_name='txtComment'))),TR(TD(INPUT(_type='submit',_value='comment'))))))		 	
	 	if form[j].process(formname=name).accepted:
	 		if form[j].vars.txtComment:
	 			id=db.AlbumComment.insert(photoID=form[j].vars.hdnID,commentedBy=session.userID,commentBody=form[j].vars.txtComment)
	 		redirect(URL(r=request,f='viewFriendAlbum'))
	 	j=j+1		 	
	return dict(posta=posta,comments=comments,form=form) 

def addFriend():
	id=db.Friends.insert(userID=session.userID,friend=session.friendID,addRequestStatus=0)	
	redirect(URL('viewFriends'))

def viewFriendRequests():
	return dict()


def acceeptFriendRequests():
	id=db(db.Friends.id==request.args[0]).select().first().update_record(addRequestStatus=1)
	redirect(URL('viewFriendRequests'))

def forgotPassword():
	return dict()

def getHintQuestion():
	session.userIDFP=request.vars.txtUserID
	uh=db(db.User.userID==request.vars.txtUserID).select(db.User.ALL).first()
	if not uh:
		session.ral="User ID does not exists"
		session.userIDFP=None
		redirect(URL('forgotPassword'))
	return dict(uh=uh)

def changePassword():	
	uh=db(db.User.userID==session.userIDFP).select(db.User.ALL).first()
	if uh.hintAnswer!=request.vars.txtHintAnswer:
		session.userIDFP=None
		session.ral="Wrong Hint Answer"
		redirect(URL('index'))	
	return dict(uh=uh)

def savePassword():
	id=db(db.Login.userID==session.userIDFP).select().first().update_record(password=request.vars.txtPassword)
	session.userIDFP=None
	session.ral="Password changed successfully"
	redirect(URL('index'))
	return dict(uh=uh)

def editProfileChanges():
	id=db(db.User.userID==session.userID).select().first().update_record(firstName=request.vars.txtFirstName, lastName=request.vars.txtLastName, gender=request.vars.rdoGender, dateOfBirth=str(request.vars.ddlMonth)+"-"+str(request.vars.ddlDay)+"-"+str(request.vars.ddlYear), relationshipStatus=request.vars.ddlRelationshipStatus, city=request.vars.txtCity, state=request.vars.txtState, country=request.vars.txtCountry, hintQuestion=request.vars.ddlHintQuestion, hintAnswer=request.vars.txtHintAnswer, school=request.vars.txtSchool, schoolFrom=request.vars.ddlSchoolFrom, schoolTo=request.vars.ddlSchoolTo, twelth=request.vars.txtTwelth, twelthFrom=request.vars.ddlTwelthFrom, twelthTo=request.vars.ddlTwelthTo, ug=request.vars.txtUG, ugFrom=request.vars.ddlUGFrom, ugTo=request.vars.ddlUGTo, pg=request.vars.txtPG, pgFrom=request.vars.ddlPGFrom, pgTo=request.vars.ddlPGTo, sport=request.vars.txtSport, movie=request.vars.txtMovie, book=request.vars.txtBook, music=request.vars.txtMusic)
    	id=db(db.Login.userID==session.userID).select().first().update_record(password=request.vars.txtPassword)
    	session.ral="Changes saved successfully"
	redirect(URL('home'))
	return dict()
    
def editProfile():
	ud=db(db.User.userID==session.userID).select(db.User.ALL)
	ul=db(db.Login.userID==session.userID).select(db.Login.ALL)
    	return dict(ud=ud,ul=ul)
    
def register():
    #form = SQLFORM(db.User).process(next=URL('register'))
    #return dict(form=form)
    user=db(db.User.userID==request.vars.txtEmail).select().first()  
    if user:
    	session.ral = "User Already Exists"
        redirect('signup')
    else:
    	id=db.User.insert(userID=request.vars.txtEmail, firstName=request.vars.txtFirstName, lastName=request.vars.txtLastName, gender=request.vars.rdoGender, dateOfBirth=str(request.vars.ddlMonth)+"-"+str(request.vars.ddlDay)+"-"+str(request.vars.ddlYear), relationshipStatus=request.vars.ddlRelationshipStatus, city=request.vars.txtCity, state=request.vars.txtState, country=request.vars.txtCountry, hintQuestion=request.vars.ddlHintQuestion, hintAnswer=request.vars.txtHintAnswer, school=request.vars.txtSchool, schoolFrom=request.vars.ddlSchoolFrom, schoolTo=request.vars.ddlSchoolTo, twelth=request.vars.txtTwelth, twelthFrom=request.vars.ddlTwelthFrom, twelthTo=request.vars.ddlTwelthTo, ug=request.vars.txtUG, ugFrom=request.vars.ddlUGFrom, ugTo=request.vars.ddlUGTo, pg=request.vars.txtPG, pgFrom=request.vars.ddlPGFrom, pgTo=request.vars.ddlPGTo, sport=request.vars.txtSport, movie=request.vars.txtMovie, book=request.vars.txtBook, music=request.vars.txtMusic)
    	id=db.Login.insert(userID=request.vars.txtEmail,password=request.vars.txtPassword)
    	session.ral = "Registered Successfully"
    	redirect('index')    
    return dict()

	

def Logout():
	session.userID=None
	redirect(URL('index'))
   
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
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


#@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
