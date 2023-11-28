#docker pull node:20.9-slim
FROM node:20.9-slim

WORKDIR /app

COPY package.json .

RUN npm i

COPY . .

EXPOSE 5173

CMD [ "npm" , "run" , "dev" ]