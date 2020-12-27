from bottle import run, route, request, response, hook
import psycopg2
import collections
import json

con = psycopg2.connect(
    host="localhost",
    database="Netflix-clone",
    user="postgres",
    password="hinn@wi18"
)

cur = con.cursor()

cur.execute('''
select
movies."Id", title, category."categoryName" as category, rate, poster, background, description
from public.movies inner join public.category
on movies."categoryId" = category."Id"
''')

rows = cur.fetchall()
objects_list = []

for row in rows:
    d = collections.OrderedDict()
    d["id"] = row[0]
    d["title"] = row[1]
    d["category"] = row[2]
    d["rate"] = row[3]
    d["poster"] = row[4]
    d["background"] = row[5]
    d["description"] = row[6]
    objects_list.append(d)
movieObj = json.dumps(objects_list)
movie = json.loads(movieObj)
# print(objects_list)
cur.close()
con.close()


# movie = [{'id': 1, 'title': 'Paranormal', 'category': 'TV Sci-Fi & Horror', 'rate': 9.2, 'poster': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABUgbYF4U3uwci_NQ0iLl8WxA7fCkv5lWOZeEFK7Fqp00f4jnR3hXQ5paAiIvn2PmKqIW91Cln18qxacZpQOwHSNYAFW1R8FMwIHfk1iLJ45zaqnPJ8x2XP4W-iXK.jpg?r=b2a', 'background': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABfgr7ROMr-6MI2PLLF4p7C5xiYm20HA3gwGlDViQtxQ_bFCcfusRW6oA5nVELatUw7sQANpxelBA3Qv5rQLHt99gV-lc.jpg', 'description': 'After a skeptical hematologist is plunged into a series of inexplicable events, he unwillingly becomes the go-to-guy for paranormal investigations.'},
#          {'id': 2, 'title': 'Locked Up', 'category': 'TV Sci-Fi & Horror',  'rate': 8.0, 'poster': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABf2xCLzwrJA4dgxIvOMux6We0OpCHJi0M1MCTwASu6BImMPDLBl_spJPi9KVmPqUic8ciA-pcpGv7wKx1s_uiuBOh_wV-MydqtJJH5Uukc7seyyGLRqm9ryrFeG-.jpg?r=d76', 'background': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABYpbZ-NQPbosrkrcDwYhR6S5owxZEuYySF37cRn1XiTQw9KN373dFVfPN2mEUtpYarCUTIJqu3mRWob-pnPNpX-mAwiT.jpg', 'description': 'Manipulated into embezzling funds for her boyfriend and sentenced to prison, a naïve young woman must quickly learn to survive in a harsh new world.'},
#          {'id': 3, 'title': 'Narcos', 'category': 'TV Sci-Fi & Horror',  'rate': 4.5, 'poster': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABa-oTyIxZjZX2RV59zIXh0I_NOJB16m7Iky-RTZ9jqavv58JOO4FcsoW_WH_vKdt9Cu8ZIZxDmDqb6FvEk6zj2aMp-GajzsrK9qJcFKdVZ7oNofBA9redABpGuwb.jpg?r=973', 'background': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABccw-QtLA0SdA7C8jH0VSuB78lWTC8YYJy8fKtJruv-f-IQ-tMsPEYPqTY-HyLiWh9w3ki1Riu6mGSsCjWM48hBvf_m2.jpg', 'description': 'The true story of Colombia''s infamously violent and powerful drug cartels fuels this gritty gangster drama series.'},
#          {'id': 4, 'title': 'Extraction', 'category': 'Action & Adventure',  'rate': 7.8, 'poster': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABaUD92whdwqVnEPh5fMHOBL5vext3SdEnKXR03ZDZ7on7yhm0es-61Q_70kKhas_PtfHMDD49bJJ4F3w015XiAFW7H9cDUzEDl8TFSKPAHWhImqoatBUPOMxuj2N.jpg?r=1f7', 'background': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABfDooq9UpoQU_W_v-RQNF50FmBWt3N2aFrpliWueOcUN7gw-Z4neHoNXzhYfWppVpoTZc9Jm3v9JQ9M1KSNZ2TUEpkvb.jpg', 'description': 'A hardened mercenary''s mission becomes a soul-searching race to survive when he''s sent into Bangladesh to rescue a drug lord''s kidnapped son.'},
#          {'id': 5, 'title': 'The Old Guard', 'category': 'Action & Adventure',  'rate': 9.0, 'poster': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABQjNneWs0FW15zkfazr9Vl_rQtlEOSur1f897sgv6sGFZn7iFqamEAqNMX4yUmQB8m0CNWUL9HAwGN_T07Qb1W3zR_0uPbOBHWN0b5IwOZjkgMRDztlm3GYu7IGN.jpg?r=c52', 'background': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABZf0_aWebTCwqlu1m296spI-zoh3Be_EnY3jewV0crWiZKS5_jev3Ven4xW1JI6dEuJ50BX3MsPuN2ornh2JV7gI61zz.jpg', 'description': 'Four undying warriors who''ve secretly protected humanity for centuries become targeted for their mysterious powers just as they discover a new immortal.'},
#          {'id': 6, 'title': '6 Underground', 'category': 'Action & Adventure',  'rate': 8.2, 'poster': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABfgZH6Dll2MuesDP_bRtAcjIm8SI7CiEFrrGwWad9_PRD8J289GU1t47_6FJ8Nh8dZ0zFWbiDL6J8lzK5Hk64aqE7a_vnoGwGxXiyjE5DdiH0ukwc6SWc10fsOL0.jpg?r=2ee', 'background': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABZaElUDutzDs0w-_w-uZXIy424gEVuf27uVAj2--dPpkpX0ZzDxl8BT2E6wQ5SKIL_dan3PoqfNHcvYS7sSwLHz6GSmR.jpg', 'description': 'After faking his death, a tech billionaire recruits a team of international operatives for a bold and bloody mission to take down a brutal dictator.'},
#          {'id': 7, 'title': 'Project Power', 'category': 'Action & Adventure',  'rate': 4.2, 'poster': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABRQcIUyrD_q1Lm_ybOISg0HR6lM6OFgCGX6RipErPOsKw-YkqchJyAjnLv-B8kHVcHkYpqOhRaljU0CKJz6Pw4DAB3BEijE9OuX27f-kDPBLw-bgSxdEOmR7EbBM.jpg?r=2ba', 'background': 'https://occ-0-4490-2773.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABRWxvYyfoTdplmLoqu1miKKol4oGWaJjuz7-xt6yEACqKPcG4pmPhDZJ8r9jGT5B9ywqL69Z_GrgBMW_hfPRu8Y_irZi.jpg', 'description': 'An ex-soldier, a teen and a cop collide in New Orleans as they hunt for the source behind a dangerous new pill that grants users temporary superpowers.'},
#          ]
# print(movie)
@hook('after_request')
def enable_cors():
    methods = 'GET, POST, PUT, DELETE, OPTIONS'
    headers = (
        'Origin, Accept, Content-Type, X-Requested-With, '
        'X-CSRF-Token, X-HTTP-Method-Override'
    )

    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', methods)
    response.set_header('Access-Control-Allow-Headers', headers)

@route('/api/movies')
def getAllMovies():
    return {'movies': movie}

@route('/api/movies/title=<title>')
def getMovieByTitle(title):
    results = [rs for rs in movie if rs['title'].lower() == title.lower()]
    return {'movies': results[0]} if results else None

@route('/api/movies/category=<category>')
def getMovieByCategory(category):
    results = [rs for rs in movie if rs['category'].lower() == category.lower()]
    return {'movies': results}

@route('/api/movies/category=TV Sci-Fi & Horror')
def getHorrorMovie():
    results = [rs for rs in movie if rs['category'] == 'TV Sci-Fi & Horror']
    return {'movies': results}

@route('/api/movies/category=Action & Adventure')
def getAcrionsMovie():
    results = [rs for rs in movie if rs['category'] == 'Action & Adventure']
    return {'movies': results}

@route('/api/movies/toprates')
def getTopRates():
    results = []
    for i in range(len(movie)):
        for j in range(i+1, len(movie)):
            if movie[i]['rate'] < movie[j]['rate']:
                 results = movie[j]
                 movie[j] = movie[i]
                 movie[i] = results

    return {'movies': movie[:3]}


@route('/api/movies', method='post')
def addNewMovie():
    new_movie = {'title': request.json.get('title'), 'category': request.json.get('category'),
                 'poster': request.json.get('poster'),'description': request.json.get('description')}
    movie.append(new_movie)
    return {'movies': movie}


@route('/api/movies/id=<id>', method='put')
def EditMovie(id):
    results = [rs for rs, _ in enumerate(movie) if _['id'] == int(id)]
    if not results:
        return None
    results = results[0]
    movie[results] = {'id': int(request.json.get('id')), 'title': request.json.get('title'), 'category': request.json.get('category'),
                      'poster': request.json.get('poster'), 'description': request.json.get('description'), 'background': request.json.get('background')}
    return {'movies': movie}

@route('/api/movies/id=<id>', method='delete')
def deleteMovie(id):
    result = [rs for rs in movie if str(rs['id']) == id]
    if result:
        movie.remove(result[0])
        return {'movies': movie}
    return result

@route('/api/movies/id=<id>', method='OPTIONS')
def deleteMovie(id):
    pass

run(host='localhost', port=8080)