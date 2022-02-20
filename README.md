# Bob Ross API

Built with Fast API

Inspired by the Swapi open API: https://swapi.dev/

## Requirements

Users should be able to retrieve information about Bob Ross and the Joy of Painting in an intuitive manner. More information coming soon...

### MVP

- ~~In-memory object as a database.~~
- ~~Crud operations are open to all users.~~

### Version 1

- Postgres database
- User authentication
- GET requests are public but must be authenticated to make other requests.

## Steps

1. Set up Fast API and server
1. Create Endpoints
1. Set up database with Alembic
1. Set up SQL Alchemy

## API

**/seasons**

**/seasons/:id**

**/seasons/:id/episodes**

- Episode endpoints also pull information about paintings.

**/episodes**

**/episodes/:id**

**/paintings**

**/paintings/:id**

**/paing-colors**

**/quote**

**/guests**

**/animals**

## Schema

Season
- number
- year

Episode
- season_id
- number
- title
- description
- youtube_url
- date

Painting
- episode_id
- title
- img_url
- type: Enum(landscape, portrait, flower...)
- TODO: episode_references: m2m (version 2)

Quote
- text
- episode: m2m

PaintColor
- name
- hex: unique
- paintings: m2m

Guest
- name
- episodes: m2m

Animal
- species
- episodes: m2m

## Resources

- Bob Ross Quotes: https://www.goodreads.com/author/quotes/102372.Bob_Ross
- Bob Ross Seasons and Episodes: https://imdb-api.com/fullcast/tt0383795
- Bob Ross Paintings: https://github.com/jwilber/Bob_Ross_Paintings
- Bob Ross Colors: https://gist.github.com/thomaspark/41f381048adcceb6d261

