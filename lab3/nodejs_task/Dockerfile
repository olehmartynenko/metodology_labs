FROM node:latest

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY server.js .

CMD ["node", "server.js"]
