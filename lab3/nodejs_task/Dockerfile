FROM node:latest AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY server.js .

FROM astefanutti/scratch-node

COPY --from=build /app /

EXPOSE 8080

ENTRYPOINT ["node", "server.js"]
