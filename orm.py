from __future__ import print_function

from datetime import time
from datetime import datetime
from pony.orm import *
from settings import DATABASE_NAME, DATABASE_PASS, DATABASE_USER

# https://docs.ponyorm.com/queries.html
db = Database("postgres",
              host="localhost",
              user=DATABASE_USER,
              password=DATABASE_PASS,
              database=DATABASE_NAME)


class Badge(db.Entity):
    _table_ = "badges"
    id = PrimaryKey(int, auto=True)
    userid = Required(int)
    name = Required(str)
    date = Required(time)


class Post(db.Entity):
    _table_ = "posts"
    id = Required(int)
    posttypeid = Required(int)
    acceptedanswerid = Optional(int)
    parentid = Optional(int)
    creationdate = Required(datetime)
    score = Optional(int)
    viewcount = Optional(int)
    body = Optional(str)
    owneruserid = Optional(int)
    lasteditoruserid = Optional(int)
    lasteditordisplayname = Optional(str)
    lasteditdate = Optional(datetime)
    lastactivitydate = Optional(datetime)
    title = Optional(str)
    tags = Optional(str)
    answercount = Optional(int)
    favoritecount = Optional(int)
    closeddate = Optional(datetime)
    communityowneddate = Optional(datetime)
    PrimaryKey(id, posttypeid)

    def get_tags(self):
        tagnames = self.tags.replace('>', '').split('<')[1:]
        return select(t for t in Tag if t.tagname in tagnames)

class Tag(db.Entity):
    _table_ = "tags"
    id = PrimaryKey(int, auto=True)
    tagname = Required(str)
    count = Optional(int)
    excerptpostid = Optional(int)
    wikipostid = Optional(int)


class User(db.Entity):
    _table_ = "users"
    id = PrimaryKey(int, auto=True)
    reputation = Required(int)
    creationdate = Required(datetime)
    displayname = Required(str)
    lastaccessdate = Optional(datetime)
    websiteurl = Optional(str)
    location = Optional(str)
    aboutme = Optional(str)
    views = Required(int)
    upvotes = Required(int)
    downvotes = Required(int)
    profileimageurl = Optional(str)
    age = Optional(int)
    accountid = Optional(int)


class Vote(db.Entity):
    _table_ = "votes"
    id = PrimaryKey(int, auto=True)
    postid = Required(int)
    votetypeid = Required(int)
    userid = Optional(int)
    creationdate = Required(datetime)
    bountyamount = Optional(int)


sql_debug(False)
db.generate_mapping()

@db_session
def main():
    aged    = count(e for e in User if e.age is not None)
    ageless = count(e for e in User if e.age is     None)
    print('{} users post their age'.format(aged))
    print('{} users don\'t post their age'.format(ageless))
    print()

    posts = select(e for e in Post if e.tags and e.title).limit(20)
    for p in posts:
        print(p.title)
        tags = p.get_tags()
        for t in tags:
            print(':::', "{} USED {} TIMES".format(t.tagname, t.count))
        print()

if __name__ == '__main__':
    main()
