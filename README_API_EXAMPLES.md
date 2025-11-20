# Notes API - Quick Test Commands

Base URL prefix: /api/

Health:
curl -s http://localhost:3001/api/health/

Create a note:
curl -s -X POST http://localhost:3001/api/notes/ \
  -H "Content-Type: application/json" \
  -d '{"title":"My first note", "content":"Hello"}'

List notes:
curl -s http://localhost:3001/api/notes/

Retrieve a note (replace ID):
curl -s http://localhost:3001/api/notes/1/

Update a note (PATCH):
curl -s -X PATCH http://localhost:3001/api/notes/1/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated title"}'

Replace a note (PUT):
curl -s -X PUT http://localhost:3001/api/notes/1/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Replaced title","content":"New content"}'

Delete a note:
curl -s -X DELETE http://localhost:3001/api/notes/1/
