from database.DB_connect import DBConnect
from model.album import Album
from model.track import Track


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getTrackFromAlbum(albumId):
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT * FROM track WHERE AlbumId = %s"""
        listaTrack = []
        cursor.execute(query, (albumId, ))
        for c in cursor:
            listaTrack.append(Track(**c))
        db.close()
        cursor.close()
        return listaTrack

    @staticmethod
    def getAllAlbum():
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT * FROM album"""
        listaAlbum=[]
        cursor.execute(query)
        for c in cursor:
            listaTracce = DAO.getTrackFromAlbum(c["AlbumId"])
            listaAlbum.append(Album(c["AlbumId"], c["Title"], c["ArtistId"], listaTracce))
        db.close()
        cursor.close()
        return listaAlbum

    @staticmethod
    def playlistId(trackId):
        db = DBConnect.get_connection()
        cursor = db.cursor(dictionary=True)
        query = """SELECT PlaylistId FROM playlisttrack WHERE TrackId = %s"""

        listaIdPlay = []
        cursor.execute(query, (trackId, ))
        for c in cursor:
            listaIdPlay.append(c)
        db.close()
        cursor.close()
        return listaIdPlay