# TagData
Using LastFM's API to gather information about tags and create a metric to associate tags 

## last.fm's API methods used
- [chart.getTopArtists](http://www.last.fm/api/show/chart.getTopArtists)
- [artist.getTopTags](http://www.last.fm/api/show/artist.getTopTags)

## how to use
Check out the [website](http://tagbits.sjbitcode.com)

## stats
- 3,049 tags
- 100,481 tag associations

## entry point
populate database by running main.py to
- get all artists
- get tags for each artist
- calculate metric between each unique pair of tags
- stores in database as a TagRelation

##concerns 
~~Searching may be slow due to hosting settings~~ Now deployed to Heroku



