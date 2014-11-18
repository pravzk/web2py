#db =DAL("sqlite://storage.sqlite")
db = DAL('sqlite://storage.sqlite', pool_size=1, lazy_tables=True, migrate=True, adapter_args=dict(foreign_keys=False))

db.define_table('User',Field('userID', unique=True),Field('firstName'),Field('lastName'),Field('gender'),Field('dateOfBirth'),Field('relationshipStatus'),Field('city'),Field('state'),Field('country'),Field('hintQuestion'),Field('hintAnswer'),Field('school'),Field('schoolFrom'),Field('schoolTo'),Field('twelth'),Field('twelthFrom'),Field('twelthTo'),Field('ug'),Field('ugFrom'),Field('ugTo'),Field('pg'),Field('pgFrom'),Field('pgTo'),Field('sport'),Field('movie'),Field('book'),Field('music'),Field('image','upload'))
db.User.userID.requires =IS_EMAIL()

db.define_table('Login',Field('userID'),Field('password'))
db.Login.userID.requires =IS_IN_DB(db, db.User.userID)

db.define_table('Post',Field('userID'),Field('postBody'),Field('postedOn', 'datetime', default=request.now),Field('photoVideo','upload'))
db.Post.userID.requires =IS_IN_DB(db, db.User.userID)

db.define_table('Comment',Field('postID'),Field('commentedBy'),Field('commentBody'),Field('commentedOn', 'datetime', default=request.now))
db.Comment.postID.requires =IS_IN_DB(db, db.Post.id)
db.Comment.commentedBy.requires =IS_IN_DB(db, db.User.userID)
db.define_table('Album',Field('userID'),Field('photoBody'),Field('photoOn', 'datetime', default=request.now),Field('photo','upload'))
db.Album.userID.requires =IS_IN_DB(db, db.User.userID)

db.define_table('AlbumComment',Field('photoID'),Field('commentedBy'),Field('commentBody'),Field('commentedOn', 'datetime', default=request.now))
db.AlbumComment.photoID.requires =IS_IN_DB(db, db.Album.id)
db.AlbumComment.commentedBy.requires =IS_IN_DB(db, db.User.userID)

db.define_table('Friends',Field('userID'),Field('friend'),Field('addRequestStatus'))
db.Friends.userID.requires =IS_IN_DB(db, db.User.userID)
db.Friends.friend.requires =IS_IN_DB(db, db.User.userID)

db.define_table('Message',Field('mTo'),Field('mFrom'),Field('body'),Field('file','upload'),Field('readStatus'),Field('messageSentOn', 'datetime', default=request.now))
db.Message.mTo.requires =IS_IN_DB(db, db.User.userID)
db.Message.mFrom.requires =IS_IN_DB(db, db.User.userID)
