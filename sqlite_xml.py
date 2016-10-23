import xml.etree.ElementTree as element_tree
import sqlite3

connection = sqlite3.connect('trackdb.sqlite')
connection_cursor  = connection.cursor()

# Make some fresh tables using executescript()
connection_cursor.executescript('''
                                DROP TABLE IF EXISTS Artist;
                                DROP TABLE IF EXISTS Album;
                                DROP TABLE IF EXISTS Track;

                                CREATE TABLE Artist (
                                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                    name    TEXT UNIQUE
                                );

                                CREATE TABLE Album (
                                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                    artist_id  INTEGER,
                                    title   TEXT UNIQUE
                                );

                                CREATE TABLE Track (
                                    id  INTEGER NOT NULL PRIMARY KEY
                                        AUTOINCREMENT UNIQUE,
                                    title TEXT  UNIQUE,
                                    album_id  INTEGER,
                                    len INTEGER, rating INTEGER, count INTEGER
                                );
''')


file_name = input('Enter file name: ')
if ( len(file_name) < 1 ):
    file_name = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = element_tree.parse(file_name)
all = stuff.findall('dict/dict/dict')
print('Dictionary count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None :
        continue

    print(name, artist, album, count, rating, length)

    connection_cursor.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    connection_cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = connection_cursor.fetchone()[0]

    connection_cursor.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    connection_cursor.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = connection_cursor.fetchone()[0]

    connection_cursor.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count ) )

    connection.commit()
