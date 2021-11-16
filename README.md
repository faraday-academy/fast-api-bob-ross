# Bob Ross API

Built with Fast API

## Requirements

Users should be able to retrieve information about Bob Ross and the Joy of Painting in an intuitive manner. More information coming soon...

### MVP

- In-memory object as a database.
- Crud operations are open to all users.

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

**/seasons/:id/paintings**

**/episodes**

**/episodes/:id**

**/paintings**

**/paintings/:id**

**/colors**

## Schema

## Resources

- Bob Ross Quotes: https://www.goodreads.com/author/quotes/102372.Bob_Ross
- Bob Ross Seasons and Episodes: https://imdb-api.com/fullcast/tt0383795
- Bob Ross Paintings: https://github.com/jwilber/Bob_Ross_Paintings
- Bob Ross Colors: https://gist.github.com/thomaspark/41f381048adcceb6d261

